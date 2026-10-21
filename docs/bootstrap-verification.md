# Verificación de la base — 21 de octubre de 2026

- Documents: 2 tests de contrato, CRUD, checksum duplicado y reapertura aprobados.
- Ingest: 2 tests de orquestación, texto plano, validación y admisión aprobados.
- Extract: go test -race y go vet aprobados antes del primer build; el Dockerfile ejecuta tests, incluyendo PDF real multipágina y corrupto.
- Web: npm ci/build aprobados; lockfile versionado.
- Docker: cuatro imágenes construidas, cinco servicios iniciados con límites.
- Smoke integrado aprobado a través de Caddy: frontend, extracción binaria/multipart, texto plano, CRUD, 409/400/413/404 y bloqueo de rutas internas.

Esto verifica la base inicial. Dataset oficial, baseline k6/Vegeta, ampliación de regresiones, mejoras de UI y defensa siguen pendientes en issues.
Los archivos PDF de prueba son sintéticos. No se cargaron documentos personales.
