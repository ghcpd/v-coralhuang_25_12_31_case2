# API Endpoint Changes

## Old vs New

| Property | Old | New |
|----------|-----|-----|
| **HTTP Method** | GET | GET |
| **Path** | `/v1/files/{file_id}/retrieve_content` | `/v1/files/{file_id}/content` |
| **Response Body Type** | JSON | Raw bytes / binary |
| **Content-Type** | application/json | application/octet-stream |
| **Response Structure** | `{"content_base64": "..."}` | Direct binary content |

## Key Differences

The API endpoint was simplified and the response format changed from structured JSON to raw binary content.

**Old:** Clients had to parse JSON and extract the base64-encoded content.

**New:** Clients receive raw bytes directly from the response body.
