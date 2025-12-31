from pathlib import Path
import httpx


def download_file(api_key: str, file_id: str, out_path: Path) -> None:
    """
    OUTDATED IMPLEMENTATION:
    - Calls deprecated endpoint
    - Assumes JSON response schema
    """
    url = f"https://api.together.xyz/v1/files/{file_id}/content"
    headers = {"Authorization": f"Bearer {api_key}"}

    resp = httpx.get(url, headers=headers)
    # propagate HTTP errors as httpx.HTTPStatusError
    resp.raise_for_status()

    # New API returns raw bytes (not JSON). Write response bytes directly.
    out_path.write_bytes(resp.content)
