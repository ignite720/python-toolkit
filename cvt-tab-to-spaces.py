from pathlib import Path
import sys

def read_dirs_to_exclude(path: str=".dirs_to_exclude.txt"):
    try:
        with open(path, 'r', encoding='utf-8') as fp:
            return [line.strip() for line in fp.readlines()]
    except (IOError, UnicodeDecodeError):
        return []

def list_files(patterns, dirs_to_include, dirs_to_exclude):
    files = list()
    for dir_to_inc in dirs_to_include:
        for pat in patterns:
            for file_path in Path(dir_to_inc).rglob(pat):
                file_path_str = str(file_path)
                if not any(file_path_str.startswith(dir_to_exc) for dir_to_exc in dirs_to_exclude):
                    files.append(file_path)
    return files

def process_file(file_path, spaces_per_tab=4):
    with open(file_path, "r") as fp:
        content = fp.read()
    if '\t' in content:
        replacement_spaces = (' ' * spaces_per_tab)
        updated_content = content.replace('\t', replacement_spaces)
        with open(file_path, mode="w", encoding="utf-8", newline="\n") as fp:
            fp.write(updated_content)
        print(f"Processed file: {file_path}")

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
    "*.sh",
    "*.yml",
)

dirs_to_include = sys.argv[1:] if len(sys.argv) > 1 else ["."]
dirs_to_exclude = read_dirs_to_exclude()
files = list_files(PATTERNS, dirs_to_include, dirs_to_exclude)
for i in files:
    if i.is_dir():
        print(f"Fatal error: is_dir => {i}")
        break
    else:
        process_file(i)