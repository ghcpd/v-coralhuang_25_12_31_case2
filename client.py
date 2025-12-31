from pathlib import Path
import httpx


def download_file(api_key: str, file_id: str, out_path: Path) -> None:
    """
    Updated implementation:
    - Uses new endpoint path (/v1/files/{file_id}/content)
    - Treats response as raw bytes and writes them directly
    - Raises httpx.HTTPStatusError for non-2xx via resp.raise_for_status()
    """
    url = f"https://api.together.xyz/v1/files/{file_id}/content"
    headers = {"Authorization": f"Bearer {api_key}"}

    resp = httpx.get(url, headers=headers)
    resp.raise_for_status()

    out_path.write_bytes(resp.content)
