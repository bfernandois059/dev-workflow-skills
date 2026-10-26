# Superficie alcanzable y controles fuera del repositorio — MarcoZen

Esta referencia cubre el punto ciego estructural de cualquier auditoría *evidence-first* que
lea solo el repositorio: **los controles de seguridad que no viven en el código**.

Aplica en **Modo 2 (pre-producción)** y **Modo 4 (seguridad)**. No se ejecuta en una auditoría
general de orden del repo ni en mantenimiento periódico, salvo que el usuario lo pida.

---

## 1. El problema que resuelve

Un control que vive en la consola de un proveedor **no deja rastro en el repositorio**. Para
una auditoría que solo lee archivos, ese control no aparece como ausente: no aparece en
absoluto. El resultado es un informe que declara la seguridad revisada habiendo mirado solo
una mitad del sistema.

El caso canónico: una plataforma de acceso restringido cuyo registro público quedó abierto en
el proveedor de autenticación. El código es correcto —hay login, hay sesiones, hay políticas—
y el repositorio no contiene ninguna línea equivocada. La puerta abierta es una casilla en un
panel.

De ahí las dos reglas duras de esta referencia:

> **1. Un control que no se puede verificar leyendo el repositorio no se omite: se reporta
> como `No verificado — verificación externa requerida`, con el lugar exacto donde se
> comprueba.**
>
> **2. Omitir un control porque no hay evidencia en el repositorio es un fallo de auditoría,
> no un `N/A`.**

`N/A` se reserva para lo que no corresponde al tipo de producto (un control de pagos en un
sitio sin cobro). Un control que sí corresponde y no se pudo comprobar es `No verificado`, y
`No verificado` es un resultado que se entrega al usuario, no un silencio.

---

## 2. Premisa: el modelo de acceso declarado

Ningún hallazgo de autorización es formulable sin esta premisa. *«Cualquiera puede
registrarse»* es una vulnerabilidad en una plataforma interna y es el comportamiento correcto
en un SaaS de autoservicio. La misma evidencia, severidades opuestas.

Antes de auditar la superficie alcanzable, establece el **modelo de acceso declarado**:

| Modelo | Quién debe poder entrar |
|---|---|
| `Público sin cuentas` | Cualquiera; no hay sesiones ni datos por usuario |
| `Registro abierto` | Cualquiera puede crear su cuenta (autoservicio) |
| `Registro restringido` | Solo invitados, o solo dominios de correo autorizados |
| `Provisión por administrador` | Nadie se registra; las cuentas las crea un administrador |
| `Interno / red privada` | Solo miembros de la organización, normalmente tras SSO |

Fuentes válidas para el modelo, en este orden:

1. El usuario en la conversación.
2. El blueprint del proyecto o `docs/permissions-matrix.md` (donde `project-blueprint` lo
   declara como decisión).
3. El README u otra documentación vigente del repositorio.

Si ninguna fuente lo declara, **pregúntalo**: es una sola pregunta y gobierna la severidad de
todo el dominio. Mientras no haya respuesta, audita contra el modelo más restrictivo que la
evidencia sugiera y dilo explícitamente.

**La ausencia de un modelo de acceso declarado es en sí misma un hallazgo P2** en cualquier
producto con usuarios: una propiedad de seguridad que nadie escribió no la puede verificar
nadie, ni una persona ni un agente. En un producto de acceso restringido con datos de
terceros, es P1.

---

## 3. Inventario de la superficie alcanzable

La superficie alcanzable es el conjunto de puntos por los que alguien puede entrar o pedir
datos. Vive en tres lugares y **los tres se auditan**:

```text
En el repositorio       En la consola del proveedor    En el despliegue respondiendo
rutas y páginas         registro y proveedores de      cabeceras realmente servidas
endpoints y actions     identidad                      métodos que el servidor acepta
tablas y vistas         políticas efectivas en la BD   destinos de redirección
buckets y rutas         visibilidad de buckets         mensajes de login y recuperación
webhooks entrantes      protección de entornos         páginas de error
jobs programados        alcance de las claves          sourcemaps publicados
                        reglas de red y CORS           DNS y subdominios vivos
```

La tercera columna no se audita leyendo archivos ni mirando un panel: se comprueba con una
petición. Lo declarado y lo servido divergen con facilidad, y **un control declarado no es un
control servido**. El pase de sondas está en [`deployed-surface.md`](deployed-surface.md).

Para cada punto, la pregunta es siempre la misma, y se responde para **tres visitantes**:

1. **Anónimo** — sin sesión. ¿Qué obtiene?
2. **Autenticado ajeno** — con sesión válida, pero sin relación con el recurso (otro usuario,
   otra empresa, otro expediente). ¿Puede leerlo o mutarlo cambiando un identificador?
3. **Autenticado con rol menor** — usuario normal donde se espera un administrador. ¿La
   restricción vive en el servidor o solo en la interfaz?

El segundo visitante es el que detecta IDOR/BOLA y las fugas entre inquilinos; es también el
que más se escapa, porque todas las pruebas manuales se hacen con la cuenta propia.

### Enumerar, no muestrear

Para que esto sea una verificación y no una impresión, enumera desde el código la lista de
rutas, endpoints, tablas y buckets, y marca cada uno con el control que lo protege. Un
inventario con huecos explícitos (`sin control identificado`) es evidencia; una frase como
*«las rutas protegidas usan middleware»* no lo es.

---

## 4. Controles fuera del repositorio, por proveedor

Catálogo **condicionado al stack detectado**: si el proyecto no usa el proveedor, la fila no
existe. No preguntes por todos.

> **No afirmes el valor por defecto de un proveedor de memoria.** Los defaults cambian entre
> versiones, planes y fechas de creación del proyecto. Verifica con la comprobación indicada,
> o reporta `No verificado` nombrando dónde se mira. Si una respuesta no tiene la forma que
> esperabas, informa lo que viste en vez de interpretarlo.

### Autenticación gestionada (Supabase Auth, Clerk, Auth0, Cognito, Firebase Auth)

| Control | Por qué importa | Cómo se comprueba |
|---|---|---|
| **Registro abierto o cerrado** | Decide si un externo puede crear cuenta. Es el control que convierte una plataforma restringida en una pública | Sonda de solo lectura (abajo) o panel del proveedor |
| **Restricción por dominio de correo o invitación** | Único mecanismo que hace cumplible un modelo `Registro restringido` | Panel del proveedor; a veces también un hook o trigger en el repositorio |
| **Confirmación de correo** | Con autoconfirmación, una cuenta es usable sin probar que el correo existe | Sonda o panel |
| **Proveedores OAuth habilitados** | Un proveedor social activo es una puerta de registro paralela: cerrar el registro por correo y dejar Google abierto no cierra nada | Sonda o panel |
| **Redirect URLs permitidas** | Una lista laxa (comodines, `localhost` en producción) permite robo de tokens en el callback | Panel del proveedor |
| **Quién puede invitar o crear usuarios** | En `Provisión por administrador`, define el perímetro completo | Panel + código del flujo de invitación |
| **Protección anti-abuso (CAPTCHA, límites de intento)** | Acota el registro y el relleno de credenciales automatizados. **Acota el abuso; no cierra la puerta**: nunca sustituye a cerrar el registro | Sonda de solo lectura o panel de protección del proveedor |

**Sonda de solo lectura (Supabase / GoTrue).** La configuración pública de autenticación es
consultable con la clave anónima, que es pública por diseño. No crea usuarios, no muta nada y
convierte un `No verificado` en evidencia:

```bash
# Requiere la URL del proyecto y la anon key (pública; nunca la service_role).
curl -s "$SUPABASE_URL/auth/v1/settings" -H "apikey: $SUPABASE_ANON_KEY"
```

Reporta los campos que devuelva relativos a si el registro está deshabilitado, si el correo se
autoconfirma y qué proveedores externos están activos. Cita la respuesta observada, no un
nombre de campo supuesto.

**Sonda activa (crear una cuenta de prueba): solo con autorización explícita del usuario.**
Crea un registro real, puede disparar correos y exige limpieza posterior. Propónla cuando la
sonda de solo lectura no sea concluyente y el modelo declarado sea restringido; nunca la
ejecutes por iniciativa propia.

### Base de datos con políticas (Supabase / PostgreSQL con RLS)

| Control | Por qué importa | Cómo se comprueba |
|---|---|---|
| **RLS activo por tabla** | Una tabla creada por SQL directo no hereda la activación que hace el editor del panel: puede quedar expuesta a la API con los datos completos | Consultar el catálogo del servidor; las migraciones del repositorio no prueban el estado efectivo |
| **Políticas efectivas, no solo declaradas** | Las migraciones versionadas pueden no ser lo aplicado en producción. RLS activo **con cero políticas** niega todo (fallo funcional, no de seguridad); RLS inactivo con políticas escritas abre todo | Catálogo del servidor + comparación con las migraciones |
| **Alcance de las políticas** | Una política que filtra por sesión pero no por inquilino deja ver filas de otra empresa | Lectura de cada política contra el inventario de tablas |
| **Permisos de tabla (`GRANT`) además de las políticas** | Son dos capas distintas y se auditan por separado. Un `GRANT` de `UPDATE`/`DELETE` al rol autenticado, combinado con una política mal acotada, permite modificar o borrar filas ajenas | Catálogo de permisos por tabla y rol, contrastado con las políticas |
| **Tablas de auditoría y bitácora** | Deben ser de solo inserción para el rol autenticado. Si se pueden editar o borrar, el registro deja de ser evidencia y el borrado destruye además el rastro | `GRANT` por tabla + políticas de `DELETE`/`UPDATE` |
| **Vistas y funciones** | Una vista o una función con permisos elevados puede devolver lo que la tabla protege | Revisión de definiciones y de quién puede ejecutarlas |

Cuando no haya acceso al servidor, el estado efectivo de RLS es `No verificado`: dilo, y
entrega la consulta que el usuario puede correr.

### Almacenamiento de archivos (buckets, blobs, CDN)

- **Visibilidad del bucket:** un bucket público sirve sus objetos sin sesión; cualquiera con
  la URL —o capaz de adivinarla— los obtiene. Verifica si los archivos privados viven en un
  bucket privado.
- **Políticas por ruta:** que el bucket sea privado no impide que un usuario descargue la
  carpeta de otro si la política no filtra por propietario.
- **URLs firmadas:** vigencia acotada y no reutilizables. Una URL pública permanente para un
  documento privado es una filtración con fecha indefinida.

### Hosting y entornos (Vercel, Netlify, Cloudflare, contenedores)

- **Protección de deploys de preview:** verifica el estado real; no asumas que está activa ni
  que no lo está. Un preview sin protección publica la aplicación completa —a menudo con datos
  cercanos a producción— en una URL indexable.
- **Separación de entornos:** que las variables de producción no estén presentes en preview ni
  en desarrollo, y que preview no apunte a la base de datos de producción.
- **Variables de entorno en el proveedor:** el conjunto real puede diferir de `.env.example`.
  Una variable crítica ausente en producción degrada silenciosamente un control.
- **Prefijo público del framework:** una variable con el prefijo que el framework expone al
  navegador (`NEXT_PUBLIC_`, `VITE_`, `PUBLIC_`) viaja al cliente. Un secreto con ese prefijo
  está publicado, aunque el repositorio no lo contenga.

### Claves y tokens emitidos

- **Alcance:** una clave de servicio o de administración concede acceso total saltándose las
  políticas. Verifica que no viva en el cliente, en un bundle, en una variable con prefijo
  público ni en un repositorio de frontend.
- **Rotación tras exposición:** una credencial que estuvo expuesta sigue siendo válida hasta
  que se rota. Limpiar el historial de Git no revoca nada: primero rotar en el proveedor.

### Correo, dominios y red

- **Inventario de subdominios:** enumera qué nombres existen y a dónde apunta cada uno. Un
  subdominio que apunta a un proveedor donde el recurso ya no existe es un **subdominio
  colgante**: quien reclame ese nombre en el proveedor sirve contenido desde un dominio de la
  organización, con sus cookies y su reputación. Los subdominios olvidados —entornos de prueba,
  versiones antiguas, paneles internos— aparecen en los registros públicos de transparencia de
  certificados.
- **Remitente verificado (SPF/DKIM/DMARC):** sin esto, los correos transaccionales se pierden
  o el dominio es suplantable.
- **CORS y dominios permitidos:** una configuración con comodín permite que un sitio ajeno
  consuma la API con la sesión del visitante.
- **Webhooks entrantes:** el secreto de firma vive en el proveedor y en el servidor; el
  endpoint debe rechazar lo no firmado. Esto sí se verifica en el código, pero el secreto
  configurado no.

### Pagos (Stripe, MercadoPago, PayPal)

- **Claves de prueba o de producción:** verifica cuál está activa en producción.
- **Eventos suscritos:** un webhook que no recibe el evento de pago confirmado deja el flujo
  dependiendo del cliente.
- **Secreto de firma presente en el entorno real,** no solo en el ejemplo.

---

## 5. Severidad de los hallazgos de superficie

Las severidades se asignan **contra el modelo de acceso declarado**, por el mismo criterio de
impacto real del resto de MarcoZen.

**P0 — verificado y expuesto.** Hay evidencia de que la puerta está abierta y de que no debía
estarlo:

- Registro abierto verificado en un producto de modelo `Registro restringido`, `Provisión por
  administrador` o `Interno`.
- Tabla con datos de usuarios alcanzable por la API sin políticas efectivas.
- Bucket público conteniendo documentos privados.
- Clave de servicio o de administración alcanzable desde el cliente.
- Un usuario autenticado puede leer o mutar recursos de otro cambiando un identificador.

**P1 — control aplicable, requerido y no verificado.** Sin evidencia de exposición, pero el
control es imprescindible para el modelo declarado y nadie puede afirmar que esté puesto:

- Registro no verificable en un producto restringido.
- Estado efectivo de RLS no verificable en un producto con datos de terceros.
- Ausencia de modelo de acceso declarado en un producto que maneja datos de terceros.
- Protección de deploys de preview no verificada cuando el preview usa datos reales.

`P1` aquí no es una vulnerabilidad inventada: es el reconocimiento explícito de que la
auditoría no cubrió un control crítico, con el lugar donde se cierra la brecha. No lo subas a
P0 sin evidencia, y no lo bajes a P3 por incomodidad.

> **Los mitigantes acotan el abuso; no cierran la puerta.** Un límite de envío de correo, un
> CAPTCHA disponible o el hecho de que la cuenta recién creada vea poco se reportan como
> contexto **dentro** del hallazgo, nunca como razón para bajarle la severidad. Si un externo
> puede completar el registro en un producto de acceso restringido, el hallazgo es `P0` aunque
> cada pieza funcione como está programada: la severidad se mide contra el modelo declarado,
> no contra lo rota que esté la implementación.

**P2 — mala práctica sin exposición demostrada.** Documentación de acceso desactualizada,
redirect URLs más amplias de lo necesario sin explotabilidad demostrada, variables del
proveedor divergentes de `.env.example`.

**P3 — endurecimiento deseable.** Rotación periódica, reducción de alcance de claves ya
correctamente ubicadas, políticas más granulares sin fuga demostrada.

### Falsos positivos que hay que descartar antes de alertar

- **Registro abierto correcto:** en `Registro abierto`, que cualquiera pueda crear cuenta no
  es un hallazgo. Es el producto.
- **Bucket público correcto:** imágenes de catálogo, logos y recursos de marketing deben ser
  públicos.
- **Clave anónima o publicable en el cliente:** está diseñada para eso. El hallazgo sería que
  las políticas no la acompañen, no su presencia.
- **Preview sin protección en un sitio público sin datos:** sin datos sensibles ni entorno
  compartido, es P3 o `N/A`.
- **Default del proveedor supuesto:** no reportes una exposición basándote en lo que
  *normalmente* trae un proveedor. Verifica o marca `No verificado`.

---

## 6. Entregable

El resultado de esta parte de la auditoría tiene dos piezas:

1. **Los hallazgos**, con el formato estándar de MarcoZen: qué se observó, evidencia, impacto
   real y acción recomendada.
2. **Una lista corta de verificación externa** —solo los controles `No verificado`— con el
   lugar exacto donde el usuario los comprueba en un minuto, y qué respuesta sería correcta
   según el modelo de acceso declarado:

```markdown
## Verificación externa pendiente

| Control | Dónde se comprueba | Respuesta correcta para este producto |
|---|---|---|
| Registro de nuevas cuentas | Panel de autenticación → registro por correo | Deshabilitado (modelo: provisión por administrador) |
| RLS efectivo en `expedientes` | Consulta al catálogo de la base de datos | Activo y con política por inquilino |
```

La lista es corta por construcción: solo lo aplicable al stack detectado y al modelo
declarado. Si queda vacía porque todo se verificó, dilo. **Nunca la reemplaces por una
advertencia genérica de que «conviene revisar la configuración del proveedor»**: eso no es un
hallazgo, no se puede cerrar y no sirve para nada.
