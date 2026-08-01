import sys
from pathlib import Path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

try:
    from database import Database
    from pipeline import DataPipeline
    print("✓ Imports successful")

    db = Database('test_temp.db')
    print("✓ Database initialized")

    pipeline = DataPipeline('test_temp.db')
    print("✓ Pipeline initialized")

    # Check if we can reach the PTIT website (just a quick check)
    import requests
    try:
        r = requests.get("https://ptit.edu.vn", timeout=5)
        print(f"✓ PTIT Connection: {r.status_code}")
    except Exception as e:
        print(f"✗ PTIT Connection failed: {e}")

    print("\n✓ Environment check passed!")
except Exception as e:
    print(f"✗ Environment check failed: {e}")
    import traceback
    traceback.print_exc()
