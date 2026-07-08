# Plantillas de documentación mínima — MarcoZen

Plantillas listas para la Fase 2 (poda). Copia, completa lo que aplique y borra lo que no.
Un documento a medio llenar con secciones vacías es peor que no tenerlo: sé concreto o
elimina la sección.

---

## README.md

```markdown
# [Nombre del proyecto]

[Una línea: qué es y para quién.]

## Qué hace
[2–4 líneas de contexto funcional.]

## Stack
- Lenguaje/framework:
- Base de datos / servicios externos:
- Deploy:

## Cómo correrlo localmente
\`\`\`bash
# requisitos previos (node X, etc.)
cp .env.example .env   # completar variables
npm install
npm run dev
\`\`\`

## Estructura del repo
[Mapa breve de carpetas clave y qué vive en cada una.]

## Documentación
- Contexto: docs/project-context.md
- Deploy: docs/deployment-runbook.md
- Seguridad: docs/security-checklist.md
- Para agentes IA: AGENTS.md
```

---

## AGENTS.md

```markdown
# AGENTS.md

## Contexto del proyecto
[Qué es, quiénes lo usan, qué problema resuelve.]

## Orden de lectura para agentes
1. README.md
2. docs/project-context.md
3. docs/architecture.md
4. [lo específico de la tarea]

## Reglas críticas
- [Qué NO tocar sin confirmación: schema de BD, cálculos, precios, etc.]
- [Convenciones obligatorias del repo.]
- [Comandos de verificación antes de dar por hecho un cambio, ej: `npm run build`.]

## Cosas que NO se implementan todavía
- [Features fuera de alcance para evitar que un agente las agregue por su cuenta.]
```

---

## .env.example

```bash
# Copiar a .env y completar. NUNCA versionar el .env real.
# Base de datos
DATABASE_URL=

# Servicios externos (placeholders, sin valores reales)
STRIPE_SECRET_KEY=
SENDGRID_API_KEY=

# App
NODE_ENV=development
PORT=3000
```

---

## docs/project-context.md

```markdown
# Contexto del proyecto

## Problema que resuelve
## Usuarios / roles
## Decisiones clave y por qué
## Qué está dentro y fuera de alcance
## Glosario de términos del dominio
```

---

## docs/architecture.md (o docs/02-architecture.md)

```markdown
# Arquitectura

## Diagrama / flujo principal
## Capas y responsabilidades
## Datos: modelos y relaciones principales
## Integraciones externas
## Decisiones y trade-offs (enlazar a docs/adr/ si existe)
```

---

## docs/deployment-runbook.md (o docs/03-deployment-runbook.md)

```markdown
# Runbook de deploy

## Dónde está desplegado (plataforma, URL, cuenta)
## Cómo se despliega (pasos o comando exacto)
## Variables de entorno requeridas (ver .env.example)
## Cómo verificar que quedó bien (healthcheck)
## Cómo hacer rollback
## Contactos / accesos necesarios
```

---

## docs/security-checklist.md (o docs/04-security-checklist.md)

```markdown
# Checklist de seguridad

- [ ] No hay secretos versionados (.env fuera del repo, en .gitignore)
- [ ] .env.example actualizado con todas las variables (sin valores reales)
- [ ] Dependencias sin vulnerabilidades críticas conocidas
- [ ] Auth y autorización revisadas en endpoints sensibles
- [ ] Datos personales / de pago tratados según normativa aplicable
- [ ] Logs no filtran secretos ni PII
- [ ] Backups y recuperación definidos
```

---

## docs/05-seo-analytics-checklist.md (solo web/e-commerce público)

```markdown
# Checklist SEO / analítica / conversión

- [ ] sitemap.xml generado y enviado
- [ ] robots.txt correcto (no bloquea lo que debe indexarse)
- [ ] Metadatos y OpenGraph por página clave
- [ ] Analytics / tag manager instalado y verificado
- [ ] Eventos de conversión definidos y disparando
- [ ] Core Web Vitals dentro de rango
```

---

## docs/adr/README.md

```markdown
# Architecture Decision Records

Cada decisión relevante va en un archivo `NNNN-titulo.md` con:
fecha · contexto · decisión · alternativas consideradas · consecuencias.
```

---

## CHANGELOG.md

```markdown
# Changelog

Formato basado en Keep a Changelog. Fechas en formato AAAA-MM-DD.

## [No publicado]
### Añadido
### Cambiado
### Corregido
```
