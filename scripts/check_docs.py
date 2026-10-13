"""Offline validation for the public docs kit; no network or credential reads."""
from pathlib import Path
import json
import re
import tomllib
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.relative_to(ROOT).parts and '__pycache__' not in p.relative_to(ROOT).parts]
for p in files:
    if p.suffix not in ('.md', '.json', '.toml', '.svg', '.py'):
        continue
    text = p.read_text()
    if p.suffix == '.md':
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if '://' in target or target.startswith('#'):
                continue
            assert (p.parent / target.split('#')[0]).exists(), (p.name, target)
    if p.suffix == '.json':
        json.loads(text)
    if p.suffix == '.toml':
        tomllib.loads(text)
    if p.suffix == '.svg':
        ET.fromstring(text)
    assert not re.search(r'cb_live_(?!xxx)[A-Za-z0-9_-]{8,}|sk-[A-Za-z0-9]{20,}|-----[B]EGIN .*PRIVATE KEY|/[U]sers/', text), p.name
conf = tomllib.loads((ROOT / 'examples/codex.config.toml').read_text())
assert conf['mcp_servers']['claudebaby']['bearer_token_env_var'] == 'CLAUDEBABY_API_KEY'
cursor = json.loads((ROOT / 'examples/cursor.mcp.example.json').read_text())
assert cursor['mcpServers']['claudebaby']['headers']['Authorization'] == 'Bearer YOUR_API_KEY'
print(json.dumps({'files_checked': len(files), 'local_links': 'PASS', 'formats': 'PASS', 'credential_patterns': 'PASS'}))
