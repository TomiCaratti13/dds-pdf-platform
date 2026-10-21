# Reparto de tareas y dependencias

[Tablero público](https://github.com/users/TomiCaratti13/projects/3)

## Orden de trabajo

Primero Tomás completa F1 en orden: contratos → clon limpio → dataset/baseline → checkpoint. F2 depende de ese checkpoint.

Después ambos trabajan en paralelo: Tomás extract/ingest/rendimiento, Felipe documents/web/documentación. Cada PR recibe revisión del otro.

Las tareas de Felipe llevan etiqueta owner:felipe; GitHub sólo permite asignarlo formalmente después de aceptar las invitaciones.

## Fase 1 — Tomás

- [[F1 · Tomás] Validar contratos v1 y congelar la integración inicial](https://github.com/TomiCaratti13/dds-pdf-platform/issues/1) — TomiCaratti13

- [[F1 · Tomás] Repetir puesta en marcha y CRUD desde un clon limpio](https://github.com/TomiCaratti13/dds-pdf-platform/issues/2) — TomiCaratti13

- [[F1 · Tomás] Incorporar dataset oficial y registrar baseline comparable](https://github.com/TomiCaratti13/dds-pdf-platform/issues/3) — TomiCaratti13

- [[F1 · Tomás] Habilitar trabajo paralelo con Felipe](https://github.com/TomiCaratti13/dds-pdf-platform/issues/4) — TomiCaratti13


## Fase 2 — paralelo

- [[F2 · Tomás] Ampliar regresiones PDF y calidad de Markdown](https://github.com/TomiCaratti13/dds-pdf-extract/issues/1) — TomiCaratti13

- [[F2 · Tomás] Optimizar admisión y concurrencia con mediciones](https://github.com/TomiCaratti13/dds-pdf-extract/issues/2) — TomiCaratti13

- [[F2 · Tomás] Cubrir fallas entre servicios y escrituras inciertas](https://github.com/TomiCaratti13/dds-pdf-ingest/issues/1) — TomiCaratti13

- [[F2 · Felipe] Migrar regresiones de persistencia y concurrencia](https://github.com/TomiCaratti13/dds-pdf-documents/issues/1) — felipemorarodrigo11-web

- [[F2 · Felipe] Mejorar consulta de documentos sin romper contrato](https://github.com/TomiCaratti13/dds-pdf-documents/issues/2) — felipemorarodrigo11-web

- [[F2 · Felipe] Pulir biblioteca, estados de error y accesibilidad](https://github.com/TomiCaratti13/dds-pdf-web/issues/1) — felipemorarodrigo11-web

- [[F2 · Felipe] Mejorar laboratorio Markdown y evidencia de demo](https://github.com/TomiCaratti13/dds-pdf-web/issues/2) — felipemorarodrigo11-web

- [[F2 · Tomás] Automatizar ensayos y generar resultados comparables](https://github.com/TomiCaratti13/dds-pdf-platform/issues/5) — TomiCaratti13

- [[F2 · Felipe] Documentar arquitectura, decisiones y guía de ejecución](https://github.com/TomiCaratti13/dds-pdf-platform/issues/6) — felipemorarodrigo11-web


## Fase 3 — ambos

- [[F3 · Ambos] Integración final, informe y defensa del TP](https://github.com/TomiCaratti13/dds-pdf-platform/issues/7) — TomiCaratti13


## Base inicial

- [[Base] Publicar repos, código inicial y organización del equipo](https://github.com/TomiCaratti13/dds-pdf-platform/issues/8) — TomiCaratti13


## Cómo colaborar

Felipe acepta las cinco invitaciones de repos. Ambos clonan platform, ejecutan setup y prueban la base. Tomás confirma el checkpoint F1 antes de abrir el trabajo paralelo.

Rama por issue, commits pequeños, PR con evidencia de TDD y pruebas, revisión cruzada y CI verde. Los cambios de contrato se acuerdan en platform.

La issue de base es retrospectiva y registra la preparación asistida. Las otras permanecen abiertas para el trabajo real de los integrantes.
