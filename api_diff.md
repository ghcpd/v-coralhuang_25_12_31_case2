Old vs New

- HTTP method: GET  -> GET
- Path: /v1/files/{file_id}/retrieve_content  ->  /v1/files/{file_id}/content
- Response body type: JSON (e.g., {"content_base64": "..."})  ->  raw bytes / binary
- Content-Type: application/json  -> application/octet-stream (or other binary types)

Notes:
- Old response: JSON with base64-encoded content
- New response: raw bytes; do not call resp.json(), use resp.content
