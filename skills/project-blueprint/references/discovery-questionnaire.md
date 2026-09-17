# Discovery Questionnaire

Esta es una **biblioteca de descubrimiento e indagación**, no un formulario secuencial ni un cuestionario obligatorio que deba responderse en su totalidad.

## Reglas de uso

1. **Guiado por impacto:** Selecciona exclusivamente preguntas cuyas respuestas puedan modificar el alcance, la arquitectura, la seguridad, la operación, el costo o la experiencia crítica del producto.
2. **No recitar:** Nunca presentes el cuestionario completo al usuario. Selecciona un bloque corto (3 a 5 preguntas) centrado en las incertidumbres arquitectónicas de mayor riesgo.
3. **No redundancia:** Si una información ya consta en el repositorio, brief, Brand Master o mensajes previos, regístrala como `Confirmado` o `Supuesto` y no vuelvas a preguntarla.
4. **Preguntas no aplicables:** Se descartan de inmediato sin requerir respuestas artificiales (ej. no indagar por modelos de CMS en una API interna sin contenido editorial).
5. **Incertidumbre no bloqueante:** Si el usuario desconoce un dato y este no imposibilita definir la arquitectura base, formula una **recomendación o supuesto reversible** y continúa sin detener el proceso.
6. **Adaptación por modo:**
   - **Greenfield:** Indagar los dominios fundamentales del nuevo producto según su tipo y nivel estimado (L0–L4).
   - **Retrofit:** Contrastar la realidad del repositorio existente con los objetivos del negocio; indagar los motivos de decisiones previas problemáticas para diseñar `docs/migration-plan.md`.
   - **Decision Patch:** Interrogar **únicamente** las variables que condicionan la decisión acotada en juego (ej. para auth: ¿roles, proveedores, sesiones?; para PDFs: ¿frecuencia, firma, diseño dinámico?).

---

## 1. Resultado y negocio
- ¿Qué problema concreto debe resolver el proyecto y para quién?
- ¿Qué resultado observable o métrica indicará que la solución funciona?
- ¿Quién patrocina el proyecto y quién aprueba el entregable técnico?
- ¿Existen restricciones no negociables de plazo, presupuesto, infraestructura o proveedores existentes?

## 2. Usuarios, acceso y control
- ¿Quiénes interactúan con el sistema y con qué frecuencia?
- ¿Es público, requiere autenticación o es de uso exclusivamente interno?
- ¿Qué roles diferenciados existen y qué acciones exclusivas puede realizar cada uno?
- ¿Se requiere inicio de sesión social, invitaciones de equipo, SSO/SAML corporativo o acceso por enlaces mágicos?
- ¿Existe separación de datos por sucursales, clientes u organizaciones (multi-tenant)?

## 3. Flujos principales y alcance
- ¿Cuáles son los 2 a 4 flujos troncales de inicio a fin?
- ¿Qué evento o acción inicia cada flujo y qué estado o artefacto lo da por concluido?
- ¿Qué queda explícitamente **fuera de alcance** en esta fase o MVP?
- ¿Cuáles son los errores o excepciones más costosos que el sistema debe prevenir?

## 4. Contenido y administración editorial
- ¿Qué contenidos requieren actualización frecuente por personas no técnicas?
- ¿Se requiere flujo editorial con estados (borrador, revisión, programado, publicado)?
- ¿Se necesita previsualización en vivo (preview) antes de publicar?
- ¿El contenido se consume únicamente en la web o se reutiliza en aplicaciones móviles, PDFs o emails?

## 5. Datos y persistencia
- ¿Qué entidades de información son centrales para el producto?
- ¿Cuál es la fuente de verdad de cada dato relevante?
- ¿Existe información personal, financiera, de salud o comercialmente sensible?
- ¿Cuál es la política esperada de retención, exportación o eliminación de datos?
- ¿Hay datos históricos o bases de datos previas que migrar o transformar?

## 6. Archivos y documentos
- ¿Los usuarios cargan archivos (imágenes, contratos, comprobantes, anexos)?
- ¿Se requiere control de acceso privado sobre los archivos o son públicos?
- ¿El sistema debe generar documentos formales (facturas, comprobantes, reportes en PDF)?
- ¿Dichos documentos requieren validez legal, numeración correlativa inmutable o firma?

## 7. Integraciones y servicios externos
- ¿El sistema debe conectarse con pasarelas de pago, CRM, ERP, logística o mensajería?
- ¿Cuál es el sentido de la comunicación (el sistema envía, recibe o sincroniza bidireccionalmente)?
- ¿Existen entornos de pruebas (sandboxes) y credenciales accesibles?
- ¿Qué debe ocurrir si una integración externa se degrada o no responde?

## 8. Experiencia, contexto y diseño
- ¿Existe marca, manual de identidad, sistema de diseño en Figma o referencias visuales aprobadas?
- ¿Qué dispositivos y condiciones de uso son predominantes (móvil en terreno, escritorio con alta densidad, mala conectividad)?
- ¿Qué destinos de rescate (2-3 enlaces útiles) deben ofrecer las páginas de sistema (404, error, sin permiso)?
- ¿Quién es responsable de proveer las piezas de identidad visible (favicon, ícono de app, imagen OG 1200×630)?

## 9. Medición y SEO (cuando aplique)
- ¿El proyecto depende de posicionamiento orgánico para captar usuarios o clientes?
- ¿Qué acciones clave deben medirse analíticamente como conversión?
- ¿Qué secciones deben indexarse públicamente y cuáles deben estar estrictamente excluidas?

## 10. Seguridad, operación y continuidad
- ¿Cuál sería el impacto de una indisponibilidad de varias horas o de una filtración de datos?
- ¿Quién gestionará las credenciales y variables de entorno seguras?
- ¿Qué política de respaldos y tiempo de recuperación ante desastres (RPO/RTO) se requiere?
- ¿Quién mantendrá, monitoreará y responderá alertas una vez en producción?
