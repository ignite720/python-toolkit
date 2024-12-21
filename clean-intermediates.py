from pathlib import Path
import shutil

def delete_dir(dir: Path):
    try:
        print(f"delete_dir => {dir}")
        shutil.rmtree(dir)
    except Exception as e:
        print(f"{str(type(e))}: {e}")

def delete_files(dir: Path=Path("foobar"), extensions=("*.foo", "*.bar", "foobar.*",), exclude_files=("foo.txt", "bar.txt",)):
    files = set()
    for ext in extensions:
        files.update(set(Path(dir).rglob(ext)))

    for file in list(files):
        if not file.is_dir() and file.name not in exclude_files:
            print(f"delete_file => {file}")
            file.unlink()

print(f"{Path(__file__).stem}\n")

delete_dir(Path("foo"))
delete_dir(Path("foo/bar") / "foobar")
delete_dir(Path("foo/bar/foobar"))

delete_files()
delete_files("foo/bar", ("*.*",), (".foobar",))