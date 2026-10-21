# PDF Lab · Desarrollo de Software 2026

Proyecto académico UTN San Rafael · Tomás Caratti y Felipe Mora.
Laboratorio de PDF a Markdown con servicios independientes, biblioteca CRUD
y un frente web. La base está implementada; la optimización con el set
oficial y la defensa del TP se completan mediante issues del equipo.

## Repositorios
- [extract](https://github.com/TomiCaratti13/dds-pdf-extract): Go + MuPDF, extracción en memoria, admisión y Markdown.
- [ingest](https://github.com/TomiCaratti13/dds-pdf-ingest): FastAPI, recepción y orquestación HTTP.
- [documents](https://github.com/TomiCaratti13/dds-pdf-documents): FastAPI + TinyDB, CRUD y checksum único.
- [web](https://github.com/TomiCaratti13/dds-pdf-web): React + Vite, biblioteca y laboratorio Markdown.
- Este repo: gateway Caddy, Compose, contratos, scripts de carga e informe.

## Puesta en marcha
Requiere Git y Docker Desktop con contenedores Linux.
Clonar este repo y preparar los otros cuatro:
PowerShell: `powershell -ExecutionPolicy Bypass -File scripts/setup.ps1`
Linux/macOS: `sh scripts/setup.sh`
Luego `docker compose up --build` y abrir http://localhost:8080.
Para detener: `docker compose down`. El volumen de documents conserva datos.

## Flujo
Browser → gateway → ingest → extract → documents.
GET/DELETE van del gateway a documents; el laboratorio /extract omite la base.
TinyDB sólo se escala verticalmente en esta base: una réplica con volumen local.
[Contratos](docs/contracts.md) · [Informe](docs/informe-tp-carga.md).

## TP de carga
Colocar los cuatro PDF oficiales en tests/stress/pdfs/1.pdf a 4.pdf.
`docker compose -f docker-compose.stress.yml up --build --scale extract=5`
Publica sólo proxy + extract en http://localhost:8081, sin CRUD/frontend.
Cada extract: 1 CPU y 512 MiB; máximo cinco réplicas. Proxy: 0,5 CPU/128 MiB.
k6: `k6 run tests/stress/k6-spike.js --summary-export=results/k6.json`
Vegeta (shell Linux/WSL): `sh tests/stress/vegeta.sh`.
Cambiar concurrencia con MAX_INFLIGHT y documentar cada experimento.
No hay resultados oficiales todavía. No se promete superar a la cátedra.

## Trabajo del equipo
Primero Tomás estabiliza contratos, arranque integrado y baseline.
Después Tomás optimiza extract/carga y Felipe mejora documents/web.
Ambos revisan PRs del otro e integran la demo final.
Cada tarea debe tener aceptación, responsable y evidencia de pruebas.

## Alcance
Markdown básico por páginas, sin OCR ni reconstrucción avanzada de tablas.
Sin autenticación: entorno académico local. El endpoint interno no sale por
gateway. go-fitz/MuPDF usa AGPL; revisar su licencia antes de otros usos.
La entrega de etapa 1 se conserva en su repositorio original.

[Tablero del equipo](https://github.com/users/TomiCaratti13/projects/3) · [Reparto y dependencias](https://github.com/TomiCaratti13/dds-pdf-platform/blob/main/docs/team-plan.md)

## Validación integrada

`uv sync --locked` y `uv run --frozen python tests/smoke.py` con Compose iniciado.
La CI clona main de los servicios: al cambiar contratos, coordinar los PRs. Para una entrega, registrar todos los SHA en el informe.
