from pathlib import Path

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
DIRS_TO_INCLUDE = (
    #"./",
    "include",
    "src",
)
DIRS_TO_EXCLUDE = (
    "wkslight/.git",
    "wkslight/libraries/FastNoise2",
    "wkslight/libraries/headeronly",
    "wkslight/libraries/lua",
    "wkslight/libraries/sol2",
    "wkslight/libraries/spdlog",
    "wkslight/libraries/XMath",
    "wkslight/premake5-modules/android-studio",
    "wkslight/premake5-modules/emscripten",
    "wkslight/premake5-modules/ninja",
    "wkslight/premake5-modules/winrt",
)

files = list_files(PATTERNS, DIRS_TO_INCLUDE, DIRS_TO_EXCLUDE)
for i in files:
    if i.is_dir():
        print(f"Fatal error: is_dir => {i}")
        break
    else:
        process_file(i)