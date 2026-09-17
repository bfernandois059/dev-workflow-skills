# Plantillas de Documentación Proporcional — MarcoZen

Plantillas de referencia para la Fase 2 (remediación autorizada).

> **Principio rector:** Cada documento debe **ganarse su lugar** según la complejidad, tamaño y equipo del proyecto.  
> No crees documentos vacíos ni recomiendes archivos que no respondan a una necesidad operativa real. Un proyecto pequeño o autoexplicativo no requiere la suite completa; basta con un buen `README.md` y un `.env.example` si maneja variables.

---

## 1. README.md (Indispensable si el repo se entrega o colabora)

```markdown
# [Nombre del proyecto]

[Una línea: propósito del producto y a quién sirve].

## Contexto y stack
- **Entorno:** [Framework / Runtime / Versión]
- **Persistencia / Servicios:** [Bases de datos, APIs de terceros]
- **Hosting / Deploy:** [Plataforma donde corre]

## Puesta en marcha local
\`\`\`bash
# Requisitos previos
cp .env.example .env   # Solo si el proyecto requiere variables
npm install            # Adaptar al gestor del repo (pnpm, pip, cargo, etc.)
npm run dev
\`\`\`

## Estructura clave
[Mapa breve de directorios y responsabilidades principales].

## Documentación adicional (solo si aplica)
- Deploy y operaciones: `docs/deployment-runbook.md`
- Seguridad: `docs/security-checklist.md`
- Contexto de arquitectura: `docs/00-project-blueprint.md`
```

---

## 2. AGENTS.md (Solo si el proyecto se opera con agentes de IA)

```markdown
# AGENTS.md

## Propósito y usuarios
[Descripción breve del problema y usuarios].

## Orden de autoridad de fuentes
1. Conversación directa con el usuario.
2. `docs/00-project-blueprint.md` o documentación técnica aprobada.
3. `README.md`

## Reglas no negociables
- No inventar credenciales, endpoints, roles ni reglas de negocio no especificadas.
- Registrar supuestos reversibles ante datos incompletos.
- Comandos reales de verificación del repositorio: `[comandos reales, ej. npm run build]`.
- No modificar lógica de pagos, transacciones ni esquema de base de datos sin autorización explícita.
```

---

## 3. .env.example (Solo si existen variables de entorno)

```bash
# NUNCA versionar el .env con valores reales. Solo identificadores de configuración.
# Persistencia
DATABASE_URL=

# Servicios de terceros (placeholders, sin claves reales)
STRIPE_SECRET_KEY=
API_SERVICE_KEY=

# Configuración pública de cliente
NEXT_PUBLIC_API_URL=
```

---

## 4. Documentos operacionales condicionales

- **`docs/deployment-runbook.md`**: Solo para aplicaciones críticas con procedimientos de despliegue, monitoreo o guardias.
- **`docs/security-checklist.md`**: Para sistemas con cumplimiento normativo o datos de pago/salud.
- **`CHANGELOG.md`**: Para proyectos que gestionan releases versionados y bibliotecas compartidas.
