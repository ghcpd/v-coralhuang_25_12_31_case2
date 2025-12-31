from pathlib import Path
import httpx


def download_file(api_key: str, file_id: str, out_path: Path) -> None:
    """
    UPDATED IMPLEMENTATION:
    - Uses new endpoint
    - Handles raw bytes response
    """
    url = f"https://api.together.xyz/v1/files/{file_id}/content"
    headers = {"Authorization": f"Bearer {api_key}"}

    resp = httpx.get(url, headers=headers)
    resp.raise_for_status()

    out_path.write_bytes(resp.content)
