from pathlib import Path
import re
import sys

CHARS_PER_LINE = 16

def convert_file_to_array(input_file, output_filename, array_name, namespace_name):
    num_bytes = 0
    namespace_str = (f"namespace {namespace_name} {{\n" if len(namespace_name) > 0 else "")
    with open(input_file, 'rb') as fp:
        bin_data = fp.read()
        num_bytes = len(bin_data)
        
        hcode = f"#pragma once\n\n{namespace_str}"
        hcode += f"extern const unsigned char {array_name}[{num_bytes}];\n"
        if len(namespace_name) > 0:
            hcode += "}\n"
            
        cppcode = f"#include \"{output_filename}.h\"\n\n{namespace_str}const unsigned char {array_name}[{num_bytes}] = {{\n"
        for i, byte in enumerate(bin_data):
            cppcode += f"0x{byte:02X}, "
            if (i + 1) % CHARS_PER_LINE == 0:
                cppcode += "\n"
        cppcode += "\n};\n"
        if len(namespace_name) > 0:
            cppcode += "}\n"
        
        # UNIX utf-8
        with open(f"{output_filename}.h", 'w', newline='\n', encoding='utf-8') as file:
            file.write(hcode)
        with open(f"{output_filename}.cpp", 'w', newline='\n', encoding='utf-8') as file:
            file.write(cppcode)
    return num_bytes

def get_argv_or(idx, default_value=""):
    return sys.argv[idx] if argc >= (idx + 1) else default_value

def to_valid_identifier_str(input):
    return re.sub(r'[\s\-!@#$%^&*()\[\]{};,./\\|]', '_', input)

argc = len(sys.argv)
print(f"argc: {argc}")

input_file = get_argv_or(1)
if not (argc >= 2 and len(input_file) > 0):
    print("Usage: python bin2arr.py input_file <namespace_name>")
else:
    namespace_name = to_valid_identifier_str(get_argv_or(2))
    output_filename = to_valid_identifier_str(Path(input_file).stem)
    array_name = f"g_{output_filename}"
    
    num_bytes = convert_file_to_array(input_file, output_filename, array_name, namespace_name)
    print(f"Conversion successful, output has been written to ({output_filename}.h and {output_filename}.cpp), {num_bytes} bytes.")