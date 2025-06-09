import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Full path to the input file
input_path = os.path.join(script_dir, "raw_comments.txt")

# Full path to the output file
output_path = os.path.join(script_dir, "extracted_comments.txt")

comments = []

with open(input_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

i = 0
while i < len(lines):
    if "'s profile picture" in lines[i]:
        steps = 0
        j = i + 1
        while j < len(lines) and steps < 4:
            if "'s profile picture" in lines[j]:
                i = j - 1  # restart from new profile picture
                break
            steps += 1
            j += 1
        else:
            if j <= len(lines):
                comment = lines[j - 1].strip()
                if comment:
                    comments.append(comment)
            i = j
            continue
    i += 1

with open(output_path, "w", encoding="utf-8") as f:
    for c in comments:
        f.write(c + "\n")

print(f"Done! Extracted {len(comments)} comments.")
