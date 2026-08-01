import sys
from pathlib import Path

def add_root_to_syspath():
    sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))