# Change Risk Matrix

## LOW

Ejemplos:

- texto o estilos acotados;
- documentación;
- corrección localizada sin datos;
- test adicional.

Mínimo:

- diff completo;
- lint/typecheck aplicables;
- prueba focalizada;
- documentación si cambia comportamiento.

## MEDIUM

Ejemplos:

- nueva pantalla o flujo;
- formulario;
- email transaccional;
- nueva dependencia;
- API interna;
- generación de PDF no crítica.

Mínimo:

- tests focalizados;
- build;
- manejo de errores;
- revisión de variables de entorno;
- actualización de documentación y changelog.

## HIGH

Ejemplos:

- autenticación o permisos;
- migración de datos;
- pagos;
- archivos privados;
- integraciones externas críticas;
- cambios de contratos públicos;
- infraestructura o despliegue.

Mínimo:

- plan de migración y rollback;
- pruebas positivas y negativas;
- revisión de seguridad;
- ADR o actualización arquitectónica;
- runbook;
- revisión humana obligatoria antes del merge.

## CRITICAL

Ejemplos:

- pérdida o transformación irreversible de datos;
- cambio de autorización global;
- manejo de información altamente sensible;
- producción sin rollback viable;
- rotación o exposición de secretos;
- incidente activo.

Requisitos:

- no ejecutar automáticamente;
- autorización explícita;
- respaldo verificado;
- plan de rollback ensayado o claramente operativo;
- doble revisión cuando sea posible;
- ventana y monitoreo de despliegue;
- registro de incidente o decisión.
