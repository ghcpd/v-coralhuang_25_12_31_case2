from pathlib import Path
import httpx


def download_file(api_key: str, file_id: str, out_path: Path) -> None:
    """
    OUTDATED IMPLEMENTATION:
    - Calls deprecated endpoint
    - Assumes JSON response schema
    """
    url = f"https://api.together.xyz/v1/files/{file_id}/retrieve_content"
    headers = {"Authorization": f"Bearer {api_key}"}

    resp = httpx.get(url, headers=headers)
    resp.raise_for_status()

    payload = resp.json()
    data = payload["content_base64"]  # outdated field

    out_path.write_bytes(data.encode("utf-8"))
