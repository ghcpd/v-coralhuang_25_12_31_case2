$ErrorActionPreference = "Stop"

# Create venv
python -m venv .venv

# Activate venv (PowerShell)
. .\.venv\Scripts\Activate.ps1

# Install deps
python -m pip install -U pip | Out-Null
python -m pip install pytest httpx | Out-Null

# Run tests
pytest -q
