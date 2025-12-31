# File Download API Migration

## Overview
This repository contains a client for downloading files from the Together AI API. The implementation has been updated to support a breaking API change.

## Test Instructions
Run the test suite with:
```bash
./run_tests
```

## What Changed

The Together AI API introduced a breaking change that required this client to be updated:

### Outdated Endpoint (Old)
- **Path:** `/v1/files/{file_id}/retrieve_content`
- **Response Format:** JSON with a `content_base64` field

### New Endpoint (Current)
- **Path:** `/v1/files/{file_id}/content`
- **Response Format:** Raw bytes / binary data (no JSON)

## Implementation Update

The `client.py` file has been updated to:
1. Use the new endpoint path (`/v1/files/{file_id}/content`)
2. Handle the response as raw binary data (`resp.content`) instead of parsing JSON
3. Write bytes directly to the output file without encoding
4. Propagate HTTP errors via `raise_for_status()` for non-2xx responses

## Why This Broke

The original implementation assumed:
- A JSON response with a `content_base64` field
- Manual base64 decoding and UTF-8 encoding

The new API returns raw binary content directly, making the old JSON parsing approach incorrect and unnecessary.
