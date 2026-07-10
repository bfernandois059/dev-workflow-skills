# Branch and Git Policy

## Base

- La branch estable predeterminada es `main`, salvo definición explícita del repositorio.
- No se permiten cambios directos en la branch estable.
- Cada branch debe representar un propósito único y revisable.

## Convención

| Tipo | Uso |
|---|---|
| `feature/` | Nueva capacidad visible o funcional |
| `fix/` | Corrección de comportamiento |
| `refactor/` | Cambio interno sin alterar comportamiento esperado |
| `docs/` | Documentación solamente |
| `test/` | Pruebas |
| `chore/` | Mantenimiento técnico |
| `security/` | Corrección o endurecimiento de seguridad |
| `migration/` | Esquema, datos o transición técnica |
| `hotfix/` | Corrección urgente sobre producción |

Nombres en minúsculas, breves y separados con guiones.

## Prohibiciones

- `git reset --hard` sin autorización.
- `git clean -fd` sin autorización.
- force-push por defecto.
- rebase o amend de commits compartidos sin autorización.
- descartar archivos con cambios no identificados.
- mezclar una feature con limpieza general no requerida.

## Squash merge

Preferido para mantener un commit claro por Pull Request. El título final debe describir el resultado, no el proceso.

Después de integrar:

```bash
git switch main
git pull --ff-only origin main
git status --short --branch
```
