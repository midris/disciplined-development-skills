"""Repository-local entry point; vendored dependencies require no installation."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'vendor'))
sys.path.insert(0, str(ROOT / 'src'))
from relaypack.cli import main
if __name__ == '__main__':
    raise SystemExit(main())
