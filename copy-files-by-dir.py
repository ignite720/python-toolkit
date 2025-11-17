import argparse
from pathlib import Path
import shutil

def main():
    FILE_SIZE_THRESHOLD = (2 * 1024, )

    parser = argparse.ArgumentParser(description='<src_dir> <dst_dir> "*.png,*.jpg"')
    parser.add_argument('src_dir', type=str, help='<src_dir>')
    parser.add_argument('dst_dir', type=str, help='<dst_dir>')
    parser.add_argument('extensions', type=str, help='<extensions>')
    
    args = parser.parse_args()
    src_dir = Path(f"{args.src_dir}")
    dst_dir = Path(f"{args.dst_dir}")
    extensions = args.extensions.split(",")
    print(args)
    
    src_files = dict()
    for ext in extensions:
        for i in src_dir.rglob(ext):
            if i.is_file():
                src_files[i.name] = i

    dst_files = list()
    for ext in extensions:
        dst_files = (dst_files + list(dst_dir.rglob(ext)))
        
    for i in dst_files:
        #if i.stat().st_size < FILE_SIZE_THRESHOLD[0]:
        if True:
            if i.name in src_files:
                print(i)
                shutil.copy2(src_files[i.name], i)
            
if __name__ == '__main__':
    main()