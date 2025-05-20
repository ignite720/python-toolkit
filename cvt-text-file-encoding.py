from pathlib import Path
import chardet
import codecs

def convert_text_file_encoding(oldfile, newfile, from_encoding="", to_encoding="utf-8-sig"):
    from_encoding_confidence = 1.0
    
    try:
        if from_encoding == "":
            with open(oldfile, "rb") as fp:
                rawdata = fp.read()
                result = chardet.detect(rawdata)
                from_encoding = result["encoding"]
                from_encoding_confidence = result["confidence"]
        print(f"{oldfile}, from encoding: {from_encoding} {from_encoding_confidence * 100:.2f}%, to encoding: {to_encoding}")
        if from_encoding != to_encoding:
            with codecs.open(oldfile, "r", encoding=from_encoding) as fp:
                content = fp.read()
                
            with codecs.open(newfile, mode="w", encoding=to_encoding) as fp:
                fp.write(content)
    except Exception as e:
        print(e)

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
    "wkslight/.github",
    "wkslight/app",
    "wkslight/app-rs",
    "wkslight/app-rs-android",
    "wkslight/foobar",
    "wkslight/libraries/app_core",
    "wkslight/libraries/bar",
    "wkslight/libraries/foo",
    "wkslight/libraries/test",
)

files = list()
for dir_to_inc in DIRS_TO_INCLUDE:
    for pat in PATTERNS:
        files = (files + list(Path(dir_to_inc).rglob(pat)))

for i in files:
    # eg. cp1252 is equivalent to Latin-1, cp936 is GBK, cp932 is Shift_JIS, cp949 is EUC-KR, respectively.
    convert_text_file_encoding(i, i, "", "utf-8")