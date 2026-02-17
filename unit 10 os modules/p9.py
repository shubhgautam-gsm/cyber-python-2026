import os

src = r"d:/movies_abc.txt"
dst = r"d:/movies_xyz.txt"

os.replace(src, dst)   # overwrites if exists
print("Renamed successfully!")
