import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from session import expires_at
settings = json.loads((ROOT / 'config/defaults.json').read_text())
print(f"token_ttl_minutes={settings['token_ttl_minutes']}; expires_at={expires_at(100, settings)}")
