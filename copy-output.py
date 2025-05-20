import sys
import shutil
from pathlib import Path

def pathlib_copytree(src_dir, dst_dir, extensions=("*.*",)):
    for ext in extensions:
        for file_from in Path(src_dir).rglob(ext):
            file_to = (Path(dst_dir) / file_from.name)
            file_to.write_bytes(file_from.read_bytes())
            print(f"file has copied to {file_to}")

src_dir = "./output"
dst_dir = "../App/output"

if sys.version_info >= (3, 8):
    # dirs_exist_ok need python>=3.8
    shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)
else:
    pathlib_copytree(src_dir, dst_dir)
print("done")