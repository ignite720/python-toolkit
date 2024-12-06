from pathlib import Path

def process_file(file_path, spaces_per_tab=4):
    with open(file_path, "r") as fp:
        content = fp.read()
    if '\t' in content:
        replacement_spaces = (' ' * spaces_per_tab)
        updated_content = content.replace('\t', replacement_spaces)
        with open(file_path, mode="w", encoding="utf-8", newline="\n") as fp:
            fp.write(updated_content)
        print(f"Processed file: {file_path}")

EXTENSIONS = (
    "*.h",
    "*.cpp",
    "*.yml",
    "*.java",
    "*.rs",
    "*.py",
    "*.lua",
)
TARGET_DIRS = (
    #"./",
    ".github",
    "app",
    "app-rs",
    "app-rs-android",
    "libraries/app_core",
    "libraries/bar",
    "libraries/foo",
    "libraries/test",
)

files = []
for dir in TARGET_DIRS:
    for ext in EXTENSIONS:
        files = (files + list(Path(dir).rglob(ext)))

for i in files:
    process_file(i)