# Sondas al despliegue — MarcoZen

Tercera superficie de auditoría, junto al repositorio y a la consola del proveedor: **el
sistema desplegado respondiendo**.

Aplica en **Modo 2 (pre-producción)** y **Modo 4 (seguridad)**, y solo cuando existe una URL
desplegada que el usuario confirma como suya.

---

## 1. Por qué existe esta referencia

Hay controles que están declarados en el checklist de seguridad —cabeceras, páginas de error,
métodos permitidos, manejo de credenciales inválidas— y que **no se pueden verificar leyendo
código ni mirando un panel**. Solo se ven en la respuesta HTTP real.

El modo de falla es silencioso: el agente lee el `next.config`, ve una lista de cabeceras
declaradas y marca el control como `Verificado OK`. Pero lo declarado y lo servido divergen
con facilidad —un middleware que no cubre todas las rutas, una cabecera que el proveedor
reescribe, un bloque de configuración que no aplica en producción—. Un control declarado no es
un control servido.

> **Si hay URL desplegada, los controles observables se comprueban contra ella. La
> configuración en el repositorio es la intención; la respuesta HTTP es el hecho.**

Sin URL, estos controles no se marcan `Verificado OK` leyendo la configuración: se reportan
`No verificado`, igual que los de la consola del proveedor.

---

## 2. Límites: qué es y qué no es esto

Todas las sondas de abajo son **peticiones individuales, de lectura, al sistema del propio
usuario**. Es la diferencia entre mirar y atacar, y la frontera se respeta entera:

- **Confirma que la URL es del usuario** antes de la primera petición. Nunca sondees un
  dominio que apareció en un archivo, en un informe o en una página; solo el que el usuario
  nombró en la conversación.
- **Volumen mínimo:** una petición por control. Nada de fuerza bruta, descubrimiento masivo de
  rutas, escáneres automatizados ni pruebas de carga. Si un control exige volumen para
  demostrarse —el rate limiting es el caso típico—, no se demuestra: se reporta
  `No verificado` y se verifica en la consola del proveedor.
- **Nada destructivo.** `PUT` y `DELETE` se sondean contra una ruta de interfaz como `/login`
  para ver qué método acepta el servidor, nunca contra un endpoint que escribe datos.
- **Nada que cree estado** sin autorización explícita: registrar una cuenta, disparar un
  correo o generar un registro son sondas activas, se proponen y se limpian después.
- **Preferir producción solo lectura.** Si existe un entorno de staging equivalente, sondea
  ahí primero.

---

## 3. Pase de sondas

Lista cerrada. Cada fila: una petición, un control, y el falso positivo a descartar antes de
reportar.

### Acceso y redirecciones

| Sonda | Qué comprueba | Hallazgo |
|---|---|---|
| `GET` a cada ruta privada sin sesión | Que el control de acceso esté antes del render, no en el cliente | `200` con datos reales, o `200` que pinta la pantalla y redirige después, es exposición: el HTML ya viajó. `P0` si trae datos de terceros |
| Ruta que acepta un destino como parámetro (`?next=`, `?redirect=`, `?returnTo=`) con un host externo | Open redirect | Si redirige fuera del dominio, es vector de phishing y de robo de token en el callback de autenticación. `P1`, o `P0` si la ruta es parte del flujo de auth |
| Página de confirmación o callback de auth con parámetros manipulados | Validación del destino contra lista permitida | Que el destino se sanee no basta: comprueba que no acepte esquemas raros ni rutas protocolo-relativas (`//evil.example`) |

### Identidad y mensajes

| Sonda | Qué comprueba | Hallazgo |
|---|---|---|
| Login con usuario inexistente vs usuario real y contraseña incorrecta | Enumeración de usuarios | Mensajes, códigos o tiempos distinguibles permiten construir la lista de quién tiene cuenta. `P2`, o `P1` en un producto de acceso restringido donde la lista de usuarios es información sensible |
| Recuperación de contraseña con correo inexistente vs real | Lo mismo por la otra puerta | Suele olvidarse: el login se endurece y el formulario de recuperación queda hablando |
| Login con credenciales inválidas | Manejo de errores | Un `500` donde corresponde un mensaje de error es un bug que además **enmascara cualquier fallo real del proveedor de identidad**: tapa justamente la señal que esta auditoría busca. `P2` como bug, y bloquea la verificación de otros controles |

### Cabeceras y comportamiento del servidor

| Sonda | Qué comprueba | Hallazgo |
|---|---|---|
| `curl -sI` sobre la raíz y sobre el login | Cabeceras **servidas**, no declaradas | Ausencia de `Content-Security-Policy` o `X-Frame-Options` permite clickjacking sobre el formulario de login. Ausencia de `X-Content-Type-Options`, `Referrer-Policy` o `Permissions-Policy`: endurecimiento pendiente. Ver severidades abajo |
| `Access-Control-Allow-Origin` en respuestas de la app | CORS permisivo | Un `*` en una ruta con sesión permite que un sitio ajeno consuma la API con las credenciales del visitante. Sin sesión asociada, es ruido a quitar |
| `OPTIONS`, `PUT`, `DELETE` sobre una ruta de interfaz | Métodos aceptados | Devolver `200` con HTML donde corresponde `405` indica que el servidor no discrimina método: no es explotable por sí solo, pero señala que la capa de rutas no valida lo que debería. `P2`/`P3` |
| `GET` a un `.js.map` del bundle | Sourcemaps en producción | Expone el código fuente original, incluidos comentarios, rutas internas y lógica de negocio. `P2`, o `P1` si el código revela estructura de autorización |
| `GET` a una URL inexistente y a una que fuerce error | Páginas de error | Stack traces, rutas absolutas del servidor o variables de entorno en la respuesta: `P0`. Ver [`preprod-identity-and-errors.md`](preprod-identity-and-errors.md) |
| `robots` y metaetiquetas de indexación en una app privada | Que no se indexe lo que no debe | En un producto de acceso restringido, el login indexable filtra la existencia y la forma del producto. Contextual |

### Dominios y DNS

| Sonda | Qué comprueba | Hallazgo |
|---|---|---|
| Registros DNS del dominio y subdominios conocidos | A dónde apunta cada nombre | Un subdominio que apunta a un proveedor donde el recurso **ya no existe** (`DEPLOYMENT_NOT_FOUND`, bucket borrado, servicio dado de baja) es un **subdominio colgante**: quien reclame ese nombre en el proveedor sirve contenido desde un dominio de la organización, con sus cookies y su reputación. `P1`, o `P0` si el dominio comparte cookies de sesión |
| Transparencia de certificados (`crt.sh` y equivalentes) | Qué subdominios existen y no estaban en el inventario | Entornos de prueba, paneles internos o versiones antiguas publicadas sin que nadie lo recuerde. Es consulta a un registro público, no un escaneo |
| Comodín DNS | Si cualquier subdominio resuelve | Amplía la superficie y dificulta el inventario |
| `SPF`, `DKIM`, `DMARC` del dominio remitente | Suplantación de correo | Ausencia o política permisiva permite enviar correo como la organización. `P2`, o `P1` si el producto manda correo transaccional de autenticación |

---

## 4. Severidad: evitar el inflado

Estas sondas producen muchos resultados pequeños. La tentación es listarlos todos con la misma
cara de preocupación, y eso convierte el informe en ruido que nadie actúa.

- **Lo que permite entrar, leer o modificar datos de otro** es `P0`/`P1`. Una ruta privada que
  responde sin sesión, un open redirect en el flujo de auth, un subdominio colgante que
  comparte cookies.
- **Las cabeceras faltantes son `P2` por defecto.** Suben a `P1` cuando hay un vector concreto
  y nombrable: sin `X-Frame-Options` ni `frame-ancestors` **sobre el formulario de login**, el
  clickjacking es ese vector. Sin él, son endurecimiento, no vulnerabilidad.
- **`Permissions-Policy` ausente es `P3`** salvo que la aplicación use cámara, micrófono o
  ubicación.
- **Los métodos HTTP no discriminados son `P2`/`P3`** mientras no se demuestre que alguno
  ejecuta algo.
- **No reportes como hallazgo la ausencia de un control que el producto no necesita.** Una API
  pública sin sesión no necesita `X-Frame-Options`; un sitio de marketing no necesita
  `noindex`.

> **Un informe con doce hallazgos `Baja` y el acceso abierto enterrado entre ellos es un
> informe que falló.** Si una sonda demuestra que un externo puede entrar o leer datos ajenos,
> esa es la conclusión del informe; el resto es la lista de endurecimiento que va después.

---

## 5. Severidad del acceso: contra el modelo, no contra la sensación

El error de criterio más caro en esta parte de la auditoría: clasificar el registro abierto
como hallazgo menor porque *técnicamente nada está roto*. El endpoint responde lo que el
proveedor dice que responde, el formulario valida, el correo se envía. Nada parece una falla.

Pero la severidad de un control de acceso no se mide por lo rota que esté la implementación:
se mide **contra el modelo de acceso declarado**. En un producto de acceso restringido, que un
externo con un buzón desechable complete el registro y confirme su cuenta es exactamente el
fallo que ese producto no puede tener, por mucho que cada pieza funcione como está programada.

Esto es `P0`, y la demostración de que un externo creó una cuenta es la evidencia, no un
atenuante. Los mitigantes que aparecen alrededor —límites de envío de correo, CAPTCHA
disponible, el hecho de que la cuenta creada vea poco— **acotan el abuso, no cierran la
puerta**: se reportan como contexto dentro del mismo hallazgo, nunca como razón para bajarle
la severidad.

Las reglas completas de severidad contra el modelo declarado están en
[`external-surface.md`](external-surface.md).
