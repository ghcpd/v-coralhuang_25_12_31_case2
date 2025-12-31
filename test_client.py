from pathlib import Path
import httpx
import pytest

from client import download_file


def test_download_uses_new_endpoint_and_raw_bytes(tmp_path: Path):
    file_id = "file_123"
    expected_bytes = b"binary-content"

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "GET"
        assert request.url.path == f"/v1/files/{file_id}/content"
        return httpx.Response(
            200,
            headers={"Content-Type": "application/octet-stream"},
            content=expected_bytes,
        )

    transport = httpx.MockTransport(handler)
    httpx.get = lambda *a, **k: httpx.Client(transport=transport).get(*a, **k)

    out = tmp_path / "x.bin"
    download_file("key", file_id, out)

    assert out.read_bytes() == expected_bytes


def test_http_error_is_propagated(tmp_path: Path):
    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(404, content=b"not found")

    transport = httpx.MockTransport(handler)
    httpx.get = lambda *a, **k: httpx.Client(transport=transport).get(*a, **k)

    with pytest.raises(httpx.HTTPStatusError):
        download_file("key", "missing", tmp_path / "x.bin")


def test_required_docs_exist_and_are_nontrivial():
    # README must be created by agent
    readme = Path("README.md")
    assert readme.exists(), "README.md must be created"
    txt = readme.read_text(encoding="utf-8")
    assert "./run_tests" in txt, "README must include one-click test command"
    assert "retrieve_content" in txt and "content" in txt, "README must mention old/new endpoints"
    assert "raw bytes" in txt.lower() or "binary" in txt.lower(), "README must mention binary/raw bytes response"

    # API diff doc must be created by agent
    diff = Path("api_diff.md")
    assert diff.exists(), "api_diff.md must be created"
    d = diff.read_text(encoding="utf-8")
    assert "/v1/files/{file_id}/retrieve_content" in d, "diff must include old endpoint path"
    assert "/v1/files/{file_id}/content" in d, "diff must include new endpoint path"
    low = d.lower()
    assert "json" in low, "diff must mention JSON"
    assert "raw bytes" in low or "binary" in low, "diff must mention raw bytes/binary"
    assert len(d.splitlines()) <= 20, "diff must be concise (<= 20 lines) for human review"
