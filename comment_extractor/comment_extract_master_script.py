import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# Step 1: Extract raw comments to extracted_comments.txt
subprocess.run(["python3", os.path.join(script_dir, "extract_coments.py")])

# Step 2: Normalize to remove useless comments
subprocess.run(["python3", os.path.join(script_dir, "normalize_comments.py")])
