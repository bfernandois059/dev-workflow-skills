# Versioning Policy

## Fuente de verdad

- `VERSION` contiene la versión SemVer instalada de `project-blueprint` en formato `MAJOR.MINOR.PATCH`.
- El tag Git publicado usa `project-blueprint-vMAJOR.MINOR.PATCH` para evitar colisiones con otras skills del repositorio.
- El commit o tag identifica el contenido exacto; `VERSION` permite comparación humana y automatizada.
- `CHANGELOG.md` en la raíz registra los cambios. No crear un changelog duplicado dentro de la skill.

## Cuándo incrementar

- `MAJOR`: cambia de forma incompatible el contrato, las garantías obligatorias o los entregables esperados.
- `MINOR`: agrega una capacidad, fase, regla, referencia o script compatible.
- `PATCH`: corrige o aclara comportamiento sin agregar capacidades ni romper compatibilidad.

Todo cambio persistente dentro de `skills/project-blueprint/` debe incluir en la misma Pull Request:

1. incremento de `VERSION` según SemVer;
2. entrada bajo `Unreleased` en el `CHANGELOG.md` raíz;
3. validación del frontmatter y scripts;
4. revisión del diff y resultados declarados en la Pull Request.

## Verificar la última versión

Desde la carpeta de la skill:

```bash
python3 scripts/check_version.py
python3 scripts/check_version.py --check-remote
```

En un fork o mirror, pasar su archivo remoto:

```bash
python3 scripts/check_version.py --check-remote --remote-url <url-del-VERSION>
```

Estados: `0` para versión válida y local igual o más nueva; `1` si existe una versión remota más nueva; `2` si la versión es inválida o no puede verificarse.

## Publicar una versión

1. Partir desde la base remota actualizada.
2. Incrementar `VERSION` y completar `CHANGELOG.md`.
3. Validar y abrir la Pull Request.
4. Obtener autorización explícita y hacer merge.
5. Crear el tag namespaced sobre el commit integrado y publicarlo.
6. Verificar que el tag y la branch estable contienen el mismo `VERSION`.

No etiquetar una branch de trabajo ni publicar un tag antes del merge aprobado.
