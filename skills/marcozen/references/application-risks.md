# Clases de fallo de aplicación — MarcoZen

Complementa a [`preprod-security.md`](preprod-security.md) y a
[`external-surface.md`](external-surface.md). Aquellas responden *quién puede entrar y qué puede
pedir*. Esta cubre lo que pasa **una vez dentro**: un usuario legítimo que consigue más de lo
que le corresponde, una entrada que el servidor no debió creer, una persona o un pipeline con
más acceso del que nadie recuerda.

Aplica en **Modo 2 (pre-producción)** y **Modo 3 (seguridad)**, y sus tres primeras secciones
forman parte del [piso de seguridad](../SKILL.md#piso-de-seguridad-en-cualquier-modo) cuando el
producto tiene usuarios.

**No es un checklist para recitar.** Cada clase está condicionada al stack: si el proyecto no
tiene la pieza, la fila no existe y no se menciona. Para cada clase que sí aplica, el informe
deja uno de los cuatro estados de siempre —`Verificado OK`, `Hallazgo`, `No verificado`, `N/A`—
en el [libro de cobertura](../SKILL.md#formato-de-salida-estándar).

> **No afirmes el comportamiento por defecto de un proveedor de memoria.** Esta referencia
> describe mecanismos, no defaults. Si un control depende de cómo está configurado el proyecto,
> se verifica o se reporta `No verificado`.

El inventario determinista —`python3 scripts/surface_inventory.py <raíz>`— entrega las pistas de
varias de estas clases (columnas de rol no, pero sí funciones `SECURITY DEFINER`, vistas,
`GRANT`, uso de `user_metadata`, HTML sin escapar, RPC invocadas, endpoints sin señal de auth).
Sus resultados son pistas: cada una se lee en el código antes de reportarla.

---

## 1. Escalada de privilegios

El usuario está autenticado y es quien dice ser. El fallo es que puede **cambiar lo que es**.

| Patrón | Señal en el repositorio | Cómo se verifica |
|---|---|---|
| **Columna de rol editable por su dueño** | Tabla de perfiles con `role`, `is_admin`, `plan`, `org_id` o `credits`, y una política de `UPDATE` que solo exige `auth.uid() = id` | Las políticas filtran **filas, no columnas**. Si el usuario puede actualizar su fila, puede actualizar todas sus columnas salvo que exista un `GRANT` por columna, un trigger que lo impida o un `WITH CHECK` que compare con el valor anterior. Busca cuál de los tres existe |
| **Autorización sobre metadatos que el usuario edita** | `user_metadata` / `raw_user_meta_data` leído para decidir rol, plan u organización —en código o dentro de una política | Esos metadatos los puede escribir el propio usuario desde el cliente. Un rol que vive ahí no es un control. Debe vivir en una tabla protegida o en metadatos que solo el servidor escribe |
| **Rol que llega en la petición** | Endpoint o server action que toma `role`, `userId`, `orgId` o `price` del cuerpo y lo usa sin compararlo con la sesión | Lectura del handler: la identidad y el alcance salen de la sesión verificada en el servidor, nunca del cuerpo |
| **Asignación masiva** | `insert(body)`, `update({...body})`, `Object.assign(row, input)` sin lista de campos permitidos | Aunque la interfaz envíe tres campos, el endpoint acepta los que lleguen |
| **Restricción solo en la interfaz** | Botón o ruta de administración oculta por rol en el cliente, sin comprobación equivalente en el endpoint que ejecuta la acción | Es el tercer visitante del pase de autorización: usuario normal donde se espera administrador |

**Severidad.** Un usuario normal que puede volverse administrador, cambiarse de organización o
alterar su saldo es `P0` cuando el camino está verificado en el código. Con el patrón presente
pero sin poder confirmar qué lo contiene (`GRANT` por columna o trigger definidos fuera del
repositorio), es `P1` con la consulta que lo cierra.

---

## 2. Funciones, vistas y código que salta las políticas

Las políticas protegen tablas. Todo lo que se ejecuta **con permisos de otro** las rodea.

| Pieza | Por qué importa | Qué comprobar |
|---|---|---|
| **Funciones `SECURITY DEFINER`** | Se ejecutan con los permisos de su dueño e ignoran las políticas de quien llama. Si están en un esquema expuesto por la API, son invocables como RPC | Quién tiene `EXECUTE` (revisar si se revocó al público y a los roles de API), si la función valida al llamante por dentro, y si fija `search_path`. Una función administrativa invocable por cualquier usuario autenticado es una puerta completa |
| **Vistas** | Una vista se evalúa con los permisos de su dueño salvo que se declare lo contrario: puede devolver filas que la tabla base protege | Si declara `security_invoker`, o si su definición filtra por el usuario de la sesión |
| **Funciones de borde y serverless** | Corren con la clave que se les configure. Con la clave de servicio, las políticas no aplican dentro de la función | Si exigen un token, y —distinto— si comprueban **quién** es el llamante y qué puede hacer. Verificar la firma de un token no es autorizar |
| **Cliente de administración en el servidor** | Un cliente creado con la clave de servicio en un endpoint ignora todas las políticas: la autorización pasa a depender únicamente del código de ese endpoint | Cada uso: ¿hay comprobación de sesión y de pertenencia **antes** de la consulta? |
| **Canales en tiempo real** | Lo que se emite por un canal llega a quien esté suscrito | Qué se publica, y si la suscripción está sujeta a la misma autorización que la lectura |

Cuando hay acceso de lectura al servidor, las consultas de catálogo están en
[`external-surface.md`](external-surface.md#consultas-de-catálogo-de-solo-lectura).

---

## 3. Identidad y sesión

Lo que rodea al login. La mayoría es configuración del proveedor: se verifica por la
[escalera de evidencia](../SKILL.md#escalera-de-evidencia) o queda `No verificado`.

- **Inicio de sesión anónimo.** Si está habilitado, un visitante sin cuenta obtiene una sesión
  que las políticas pueden tratar como la de cualquier usuario autenticado. Verifica si está
  activo y, si lo está, si las políticas distinguen a los anónimos.
- **Segundo factor para roles de alto privilegio.** En un producto con administradores que ven
  datos de terceros, la ausencia de un segundo factor disponible o exigido es `P1`/`P2` según
  el dato.
- **Política de contraseñas** y protección contra contraseñas filtradas, cuando el proveedor
  las ofrece.
- **Vida de la sesión y cierre remoto:** duración de los tokens, revocación al cambiar la
  contraseña, cierre de sesiones al desactivar una cuenta. Una cuenta "desactivada" en la
  aplicación cuyo token sigue vivo no está desactivada.
- **Cambio de correo y recuperación:** si cambiar el correo exige confirmar el anterior o
  reautenticarse; si el enlace de recuperación expira y es de un solo uso.
- **Vinculación de identidades:** un proveedor social que vincula por coincidencia de correo
  sin que ese correo esté verificado permite tomar una cuenta ajena.
- **Baja de usuarios:** al eliminar o desactivar a alguien, qué pasa con sus sesiones, sus
  claves de API personales y sus invitaciones pendientes.

---

## 4. Entrada que el servidor no debió creer

Solo las clases que el stack hace posibles.

| Clase | Señal | Qué comprobar |
|---|---|---|
| **XSS** | HTML insertado sin escapar (`dangerouslySetInnerHTML`, `v-html`, `{@html}`, `innerHTML`), Markdown renderizado a HTML | Origen del contenido: si viene de un usuario o de una fuente externa, debe sanearse. Con sesión en almacenamiento accesible por script, un XSS es toma de cuenta |
| **Inyección** | SQL construido por concatenación, `EXECUTE` dinámico dentro de una función, filtros armados con texto del usuario, comandos de shell con entrada externa | Parámetros enlazados; identificadores validados contra lista cerrada |
| **SSRF** | El servidor descarga una URL que entrega el usuario (previsualización de enlaces, importadores, webhooks configurables, proxy de imágenes) | Lista de destinos permitidos; bloqueo de direcciones internas y de metadatos del proveedor de nube |
| **Subida de archivos** | Endpoint o bucket que recibe archivos | Tipo validado por contenido y no por extensión, límite de tamaño, nombre y ruta generados por el servidor (nunca los del cliente), y que un archivo subido no se sirva como HTML ejecutable desde el dominio de la aplicación |
| **CSRF** | Sesión por cookie más endpoints que mutan con `GET`, o `POST` sin comprobación de origen ni token | Atributo `SameSite` de la cookie, verificación de origen en mutaciones. Con token en cabecera en vez de cookie, no aplica |
| **Consultas sin límite** | Listados sin paginación máxima, filtros que aceptan cualquier columna, exportaciones completas | Un usuario legítimo puede extraer la tabla entera o tumbar la base |
| **Abuso con costo** | Endpoints que disparan correo, SMS, generación con modelos o procesos pesados | Límite por usuario y por IP. Sin él, el daño es la factura. El límite se verifica en el proveedor o en el código, no enviando volumen |

---

## 5. Personas con acceso

El control más olvidado no es técnico. Un sistema perfectamente configurado sigue abierto para
todos los que tienen la llave.

**Antes de reportar una cuenta inesperada como registro abierto, descarta este camino:**
alguien con acceso a la consola del proveedor, con la clave de servicio o con la cadena de
conexión puede crear usuarios aunque el registro público esté cerrado. Son hallazgos distintos
con correcciones distintas, y confundirlos deja uno de los dos sin cerrar.

| Qué inventariar | Dónde se comprueba | Hallazgo |
|---|---|---|
| Miembros de la organización en cada proveedor (base de datos, hosting, pagos, correo, DNS) y su rol | Panel de cada proveedor, o su conector/CLI | Personas que ya no trabajan en el proyecto, cuentas personales en vez de corporativas, todos como propietarios |
| Colaboradores del repositorio y sus permisos | Plataforma de Git | Acceso de escritura o administración sin necesidad; llaves de despliegue y tokens personales vigentes |
| Quién conoce las credenciales de alto privilegio | Preguntarlo | Una clave de servicio compartida por chat o usada en máquinas personales no es rotable con certeza: se rota |
| Protección de la rama de producción | Plataforma de Git | Sin revisión obligatoria, quien tenga escritura despliega a producción solo |
| Separación entre quien desarrolla y los datos reales | Entornos y sus variables | Desarrollo local apuntando a la base de producción convierte a cada colaborador en administrador de los datos reales |

Sin acceso a los paneles, cada fila aplicable se entrega en **Verificación externa pendiente**
con la respuesta correcta para este producto. Es `P1` cuando el producto maneja datos de
terceros y nadie puede enumerar quién tiene acceso de administración.

---

## 6. Pipeline y cadena de suministro

Aplica si existe CI/CD o despliegue automático.

- **Secretos en el pipeline:** qué secretos están disponibles para qué flujos, y si un flujo
  disparado por una contribución externa puede leerlos. Un flujo que se ejecuta con el contexto
  del repositorio base sobre código de un fork es el patrón a buscar.
- **Acciones y pasos de terceros** referenciados por una etiqueta móvil en vez de una versión
  fija, en flujos con acceso a secretos.
- **Despliegues de preview** generados desde ramas o forks ajenos con variables reales.
- **Dependencias:** archivo de bloqueo versionado y respetado en la instalación; scripts de
  instalación de paquetes poco conocidos; dependencias que resuelven desde un registro distinto
  al esperado.
- **Secretos en el historial:** el árbol actual puede estar limpio y el secreto seguir en un
  commit anterior. Si el proyecto tiene un escáner de secretos instalado, úsalo; si no, busca
  por nombre de variable sensible en el historial (`git log -S '<NOMBRE>' --oneline`) y revisa
  los commits que la tocan. Reporta tipo y commit, nunca el valor. Un secreto que estuvo en el
  historial se considera expuesto hasta rotarlo: reescribir el historial no lo revoca.

---

## 7. Datos, registros y errores

- **Datos personales o secretos en logs:** cuerpos de petición completos, tokens, cabeceras de
  autorización o documentos de identidad escritos a un log que más personas pueden leer que la
  propia base de datos.
- **Respuestas que devuelven de más:** `select *` hacia el cliente con columnas que la
  interfaz no muestra (hash, correo de otros usuarios, notas internas). Lo que no se pinta
  igualmente viajó.
- **Registro de eventos de seguridad:** si queda rastro de inicios de sesión, cambios de rol y
  acciones administrativas, y si ese rastro es inmutable para quien lo genera.
- **Respaldo y restauración:** que exista, y que alguien haya restaurado uno. Un respaldo nunca
  restaurado es una hipótesis.
