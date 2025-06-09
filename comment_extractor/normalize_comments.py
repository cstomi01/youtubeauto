import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "extracted_comments.txt")
output_path = os.path.join(script_dir, "normalized_comments.txt")

with open(input_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

filtered = []

for line in lines:
    # Drop if no English letters
    if not re.search(r'[a-zA-Z]', line):
        continue

    # If line starts with @mention, remove it to check what's left
    line_no_mentions = re.sub(r'^@\w+\s*', '', line)

    # Drop if after removing mention, no English letters left
    if not re.search(r'[a-zA-Z]', line_no_mentions):
        continue

    filtered.append(line)

with open(output_path, "w", encoding="utf-8") as f:
    for line in filtered:
        f.write(line + "\n")

print(f"Done! Kept {len(filtered)} normalized comments.")
