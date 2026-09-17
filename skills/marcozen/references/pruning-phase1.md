# Poda Fase 1 — Cambios Seguros y Remediación Autorizada

Fase de **remediación y orden documental**. Se ejecuta **únicamente bajo autorización del usuario** (sea tras revisar la auditoría o porque el usuario solicitó explícitamente desde el inicio "audita y corrige lo que encuentres").

Objetivo: **Ordenar el repositorio y mitigar riesgos superficiales sin alterar la lógica de negocio ni romper funcionalidades**.

---

## Reglas de ejecución

1. **Trabajar en branch dedicada:** Toda modificación debe realizarse en una rama específica, siguiendo las prácticas de `engineering-workflow`.
2. **Proporcionalidad documental:** Crear únicamente los documentos cuya necesidad esté demostrada en la auditoría. No generar plantillas vacías.
3. **Secretos reales no se tocan a ciegas:** Si se detecta un `.env` versionado con valores reales, **no lo borres precipitadamente en esta fase**: márcalo como bloqueador P0 para acordar la rotación y revocación segura de credenciales antes de eliminarlo del historial.

---

## Alcance de acciones permitidas

- Actualizar o clarificar `README.md` (instrucciones de arranque y mapa del proyecto).
- Crear `.env.example` con identificadores y placeholders (sin valores reales).
- Crear `AGENTS.md` si el proyecto será desarrollado con agentes autónomos.
- Documentar runbooks de despliegue o checklists de seguridad necesarios.
- Eliminar ramas remotas ya fusionadas (previa confirmación explícita del inventario).
- Retirar archivos temporales o basura (`.DS_Store`, logs locales) del control de versiones.

## Acciones estrictamente PROHIBIDAS en esta fase

- Modificar lógica de negocio, cálculos de precios o flujos transaccionales.
- Borrar código funcional.
- Cambiar librerías mayores o dependencias core.
- Alterar esquemas de bases de datos o migraciones.
