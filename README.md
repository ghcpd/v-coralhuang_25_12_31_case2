./run_tests

Problem summary

The test failures were caused by an API breaking change: the file download endpoint changed and the response format no longer returns JSON.

- Old endpoint: /v1/files/{file_id}/retrieve_content
- New endpoint: /v1/files/{file_id}/content

The old server returned a JSON payload containing base64 content; the new server returns raw bytes (binary) with Content-Type like application/octet-stream. The bug was fixed by updating `client.download_file` to call the new path and write `resp.content` directly to disk, and by relying on `resp.raise_for_status()` for error handling.

Run the test suite with:

./run_tests
