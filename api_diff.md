Old vs New

- HTTP method: GET  →  GET
- Path: /v1/files/{file_id}/retrieve_content  →  /v1/files/{file_id}/content
- Response body type: JSON (old; contained base64 field)  →  raw bytes / binary (new)
- Content-Type: application/json  →  application/octet-stream (typical)

Old response: JSON
New response: raw bytes / binary
