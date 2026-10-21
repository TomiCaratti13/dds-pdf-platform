# Informe de carga y estrés — plantilla de investigación

Equipo: Tomás Caratti / Felipe Mora. Estado: resultados pendientes de medir.

## Hipótesis
Medir si MuPDF y el control de admisión mejoran capacidad útil bajo límites.
No se afirma una mejora sin ejecutar el set oficial.

## Reproducibilidad
Registrar commits de los cinco repos, CPU/RAM del host y Docker, versiones,
hashes/tamaños/páginas de los cuatro PDF oficiales y comandos exactos.
Repetir cada configuración al menos tres veces después de calentamiento.
Separar pruebas con una réplica de las de cinco. No ejecutar otras cargas.

## Experimentos pendientes
1 réplica MAX_INFLIGHT=1; 5 réplicas MAX_INFLIGHT=1; variantes 2 y 4.
Guardar salida cruda k6/Vegeta, recursos de contenedores y reinicios/OOM.
Informar 200/s, solicitudes ofrecidas/completadas, errores por código,
p50/p90/p95/p99 y tiempo máximo. Rechazos 503 no son éxitos.

## Comparación con cátedra
Referencia k6: 25,35 req/s, 0% errores, p95 8,80 s.
Referencia Vegeta: 50 req/s ofrecidos, 16,65 req/s efectivos,
66,53% éxito, p50 14,89 s. Exigir mismas restricciones y PDF.

## Discusión y conclusión
Completar después de medir: cuello de botella, cambios descartados,
calidad del Markdown y límites. No usar el benchmark ASGI de etapa 1 como
comparación: usa otro transporte y otros documentos.
