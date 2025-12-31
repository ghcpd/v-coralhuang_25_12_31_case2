README — API client migration

Run tests:
./run_tests

Summary:
The test failures were caused by an outdated endpoint and a response-schema change. The client previously called `/v1/files/{file_id}/retrieve_content` and expected JSON (base64) — the new API uses `/v1/files/{file_id}/content` and returns raw bytes/binary. The updated `download_file` now requests the new path and writes `resp.content` directly to the output path; HTTP errors are propagated via `resp.raise_for_status()`.

Old endpoint: /v1/files/{file_id}/retrieve_content
New endpoint: /v1/files/{file_id}/content

New response format: raw bytes / binary (not JSON)
