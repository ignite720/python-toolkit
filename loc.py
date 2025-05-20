from pathlib import Path
import time

PATTERNS = (
    "*.c",
    "*.cc",
    "*.cpp",
    "*.cxx",
    "*.h",
    "*.hh",
    "*.hpp",
    "*.hxx",
    "*.inl",
    "*.ipp",
    "*.tpp",
    "*.java",
    "*.lua",
    "*.py",
    "*.rs",
)
DIRS_TO_INCLUDE = (
    "./",
    "include",
    "src",
)

loc = dict()
for pat in PATTERNS:
    loc[pat] = {
        "lines_of_code": 0,
        "files": list(),
    }
    for dir_to_inc in DIRS_TO_INCLUDE:
        loc[pat]["files"] = (loc[pat]["files"] + list(Path(dir_to_inc).rglob(pat)))

start = time.time()
for k, v in loc.items():
    for i in v["files"]:
        with open(i, mode="rb") as fp:
            v["lines_of_code"] += sum(1 for line in fp)

end = time.time()
print(f"cost: {(end - start):02f}s")
for k, v in loc.items():
    print(k.ljust(20), v["lines_of_code"])