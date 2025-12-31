Old vs New

- HTTP method: GET  -> GET
- Path: /v1/files/{file_id}/retrieve_content  -> /v1/files/{file_id}/content
- Response body type: JSON (old)  -> raw bytes / binary (new)
- Content-Type: application/json (old, typically)  -> application/octet-stream (new, typically)

Old response: JSON with fields (e.g. content_base64)
New response: raw bytes / binary payload (not JSON)