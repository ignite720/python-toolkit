from pathlib import Path
import sys
import time

PATTERNS = (
    "*.asm",
    "*.c",
    "*.cc",
    "*.cpp",
    "*.cppm",
    "*.cs",
    "*.cxx",
    "*.glsl",
    "*.go",
    "*.h",
    "*.hh",
    "*.hlsl",
    "*.hpp",
    "*.hxx",
    "*.inl",
    "*.ipp",
    "*.ixx",
    "*.java",
    "*.js",
    "*.kt",
    "*.lua",
    "*.php",
    "*.py",
    "*.rb",
    "*.rs",
    "*.sql",
    "*.swift",
    "*.tpp",
    "*.ts",
)

if True:
    langs = sorted(list(PATTERNS))
    for lang in langs:
        print(f"\"{lang}\",")

dirs = sys.argv[1:] if len(sys.argv) > 1 else ["."]

loc = {}
for dir in dirs:
    for pat in PATTERNS:
        if pat not in loc:
            loc[pat] = {
                "files": [],
                "lines_of_code": 0,
            }
        loc[pat]["files"].extend(list(Path(dir).rglob(pat)))

start = time.time()
for k, v in loc.items():
    for i in v["files"]:
        with open(i, mode="rb") as fp:
            v["lines_of_code"] += sum(1 for line in fp)
end = time.time()

total_loc = sum(v["lines_of_code"] for v in loc.values())
print(f"cost: {(end - start):02f}s\ndir: {dirs}\ntotal lines of code: {total_loc:,}")

pattern = "pattern"
num_files = "num of files"
lines_of_code = "lines of code"
print(f"{pattern:<20} {num_files:<20} {lines_of_code:<20}")
for k, v in loc.items():
    print(f"{k:<20} {len(v['files']):<20,} {v['lines_of_code']:<20,}")