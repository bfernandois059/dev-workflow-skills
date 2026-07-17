# Versioning Policy

## Fuente de verdad

- `VERSION` contiene la versión SemVer instalada de `engineering-workflow` en formato `MAJOR.MINOR.PATCH`.
- El tag Git publicado usa `engineering-workflow-vMAJOR.MINOR.PATCH` para evitar colisiones con otras skills del mismo repositorio.
- El commit o tag identifica el contenido exacto; `VERSION` permite comparación humana y automatizada.
- `CHANGELOG.md` en la raíz del repositorio registra los cambios de cada versión. No crear un changelog duplicado dentro de la skill.

## Cuándo incrementar

- `MAJOR`: cambia de forma incompatible el contrato, las garantías obligatorias o el flujo esperado.
- `MINOR`: agrega una capacidad, regla, referencia o script compatible.
- `PATCH`: corrige o aclara comportamiento sin agregar capacidades ni romper compatibilidad.

Todo cambio persistente dentro de `skills/engineering-workflow/` debe incluir en la misma Pull Request:

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

El segundo comando compara la copia local con `VERSION` en la branch principal del repositorio canónico. En un fork o mirror, pasar su archivo remoto:

```bash
python3 scripts/check_version.py --check-remote --remote-url <url-del-VERSION>
```

Estados de salida:

- `0`: versión válida y local igual o más nueva que la remota;
- `1`: existe una versión remota más nueva;
- `2`: versión inválida o verificación imposible.

No asumir que una copia es actual solo porque fue instalada recientemente. Si la tarea exige la última versión, actualizar referencias Git y comparar contra el origen antes de modificar.

## Publicar una versión

1. Partir desde la base remota actualizada.
2. Incrementar `VERSION` y completar `CHANGELOG.md`.
3. Ejecutar las validaciones aplicables y abrir la Pull Request.
4. Obtener autorización explícita y hacer merge según la política del repositorio.
5. Crear el tag namespaced sobre el commit integrado y publicarlo.
6. Verificar que el tag y la branch estable contienen el mismo `VERSION`.

No etiquetar una branch de trabajo ni publicar un tag antes del merge aprobado.
