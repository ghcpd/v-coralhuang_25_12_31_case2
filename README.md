# API Migration Fix

This repository contains a Python client for downloading files from an API. Recently, the API underwent breaking changes that required updates to the client code.

## Test Failures and Fixes

The initial test failures were caused by:
- An outdated endpoint: `/v1/files/{file_id}/retrieve_content` (old) vs `/v1/files/{file_id}/content` (new)
- A response schema mismatch: the old API returned JSON with a `content_base64` field, while the new API returns raw bytes/binary data directly

## Changes Made

- Updated `client.py` to use the new endpoint and handle raw bytes responses
- Created documentation files: `README.md`, `api_diff.md`
- Added `.gitignore` for Python virtual environments and artifacts

## Running Tests

To run the tests, execute:

```bash
./run_tests
```

This will set up a virtual environment, install dependencies, and run pytest.