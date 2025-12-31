Fix for API breaking change and test instructions

Run tests:

./run_tests

Summary

Tests in this repo were failing because the client used an outdated endpoint and expected a JSON response. The upstream API changed the endpoint from `/v1/files/{file_id}/retrieve_content` to `/v1/files/{file_id}/content` and now returns raw bytes (binary) instead of JSON. The `download_file` implementation has been updated to call the new path and to write `resp.content` directly to the output path; HTTP errors are propagated via `resp.raise_for_status()`.