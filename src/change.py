import os

folder = "C:/path/to/your/folder"  # ← change this to your folder
ext = ".jpg"

files = [f for f in os.listdir(folder) if f.endswith(ext)]
files.sort()  # optional

for i, filename in enumerate(files, 1):
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, f"{i}{ext}")
    os.rename(old_path, new_path)

print("Done renaming!")
