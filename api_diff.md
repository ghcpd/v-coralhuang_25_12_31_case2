# API Differences: Old vs New

## HTTP Method
- Old: GET
- New: GET

## Path
- Old: `/v1/files/{file_id}/retrieve_content`
- New: `/v1/files/{file_id}/content`

## Response Body Type
- Old: JSON (with `content_base64` field)
- New: Raw bytes / binary

## Content-Type
- Old: `application/json`
- New: `application/octet-stream`