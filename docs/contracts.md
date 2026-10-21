# Contratos v1

## Extract (stateless)
`POST /extract`: application/pdf, application/octet-stream o multipart con un
único `file`. Máximo inicial 12 MiB. Respuesta 200:
`{"content":"## Página 1\n\nTexto", "page_count":1, "text":"Texto"}`.
content es Markdown básico por página; text preserva texto plano para etapa 1.
No promete reconstrucción semántica de tablas ni OCR. Error 400/413/415/503;
saturación devuelve Retry-After. Admisión antes de leer el cuerpo.

## Ingest (stateless)
`POST /documents/upload` y `PUT /documents/{doc_id}`: un PDF en `file`, 5 MiB.
Extrae vía HTTP y envía JSON a documents. Sin reintentos automáticos de
escritura: evita repetir una operación de resultado incierto. Timeout 504,
dependencia caída/contrato inválido 502. Propaga 409 y 503.

## Documents (estado local)
GET `/documents/`, GET/DELETE `/documents/{doc_id}` públicos por gateway.
POST `/internal/documents`, PUT `/internal/documents/{doc_id}` sólo red interna.
Entrada JSON: filename, text (plano), checksum SHA-256 hex, size en bytes.
Respuesta: agrega id UUID, created_at y updated_at. Duplicado 409, ausente 404,
bloqueo agotado 503. Una réplica de documents, volumen local persistente.

## Integración
Mismo origen de navegador; rutas relativas, sin CORS para la demo integrada.
El gateway no expone /internal. El frontend renderiza Markdown sin HTML crudo.
/health informa vida del proceso; no equivale a disponibilidad de dependencias.
