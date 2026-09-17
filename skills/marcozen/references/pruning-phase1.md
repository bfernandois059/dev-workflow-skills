# Poda Fase 1 — Cambios Seguros y Remediación Autorizada

Fase de **remediación y orden documental**. Se ejecuta **únicamente bajo autorización del usuario** (sea tras revisar la auditoría o porque el usuario solicitó explícitamente desde el inicio "audita y corrige los problemas seguros que encuentres").

> **Frontera de autorización:** La solicitud de "audita y corrige" autoriza proceder directamente con mejoras seguras, no destructivas y reversibles (documentación, README, `.env.example`, limpieza de basura local/temporal). **No autoriza la eliminación automática de ramas remotas**: la poda de ramas remotas afecta el historial compartido y exige siempre presentar el inventario clasificado y solicitar confirmación explícita sobre esas ramas específicas antes de borrarlas.

Objetivo: **Ordenar el repositorio y mitigar riesgos superficiales sin alterar la lógica de negocio ni romper funcionalidades**.

---

## Reglas de ejecución

1. **Trabajar en branch dedicada:** Toda modificación debe realizarse en una rama específica, siguiendo las prácticas de `engineering-workflow`.
2. **Proporcionalidad documental:** Crear únicamente los documentos cuya necesidad esté demostrada en la auditoría. No generar plantillas vacías.
3. **Secretos reales no se tocan a ciegas:** Si la inspección prioritaria de un `.env` versionado revela que contiene secretos o credenciales reales comprometidas, **no lo borres precipitadamente en esta fase**: repórtalo como bloqueador P0 (sin exponer valores) para acordar la rotación y revocación segura de credenciales antes de eliminarlo del historial de Git. Si solo contiene configuración no sensible, puede removerse a `.gitignore` y documentarse en `.env.example`.

---

## Alcance de acciones permitidas

- Actualizar o clarificar `README.md` (instrucciones de arranque y mapa del proyecto).
- Crear `.env.example` con identificadores y placeholders (sin valores reales).
- Crear `AGENTS.md` si el proyecto será desarrollado con agentes autónomos.
- Documentar runbooks de despliegue o checklists de seguridad necesarios.
- Eliminar ramas remotas ya fusionadas (requiere siempre confirmación explícita del inventario específico).
- Retirar archivos temporales o basura (`.DS_Store`, logs locales) del control de versiones.

## Acciones estrictamente PROHIBIDAS en esta fase

- Modificar lógica de negocio, cálculos de precios o flujos transaccionales.
- Borrar código funcional.
- Cambiar librerías mayores o dependencias core.
- Alterar esquemas de bases de datos o migraciones.
