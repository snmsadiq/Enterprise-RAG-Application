import sys
from pathlib import Path

# Dynamically add the project root (parent of 'test') to sys.path
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from app.config import Settings

print("Testing Settings class...")
print("AWS Region:", Settings().aws_region)
print("AWS Access Key ID:", Settings().aws_access_key_id)
print("AWS Secret Access Key:", Settings().aws_secret_access_key)