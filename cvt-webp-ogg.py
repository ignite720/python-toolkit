from pathlib import Path
import os

PATTERNS = (
    "*.wav",
    "*.png",
)

files = list()
for pat in PATTERNS:
    files = (files + list(Path("./").rglob(pat)))

for i in files:
    print(i)
    
    cmd = ""
    if i.suffix == ".png":
        cmd = f"cwebp.exe {i} -o {i.parent / i.stem}.webp"
    elif i.suffix == ".wav":
        cmd = f"oggenc2.exe {i} -o {i.parent / i.stem}.ogg"
    os.system(cmd)
    
    # warning: please back up your files first
    #i.unlink()