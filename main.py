import argparse
from time import sleep
from colorama import Fore, init
from functions.files import *

init()

def decorate(text,begin=True, final=True, verboose=True,endl="\n"):
    if verboose:
        print('-'*40) if begin else None
        print(text,end=endl)
        print('-'*40) if final else None

COLORS = Fore.__dict__
arguments = argparse.ArgumentParser(description = "[i] Quick-c++ start program")
arguments.add_argument("-p","--path", help="Path to quick-start", required = False)
arguments.add_argument("-fn","--filename",help = "name of the cpp file", required = False)
arguments.add_argument("-v","--verboose", help = "Activate verboosity", required = False)
args = arguments.parse_args()

TITLE_SCRIPT = f"[{COLORS['MAGENTA']}i{COLORS['RESET']}] Quick-c++ start program".center(48,' ')
END_SCRIPT = f"[{COLORS['GREEN']}+{COLORS['RESET']}] Done".center(48,' ')
INFO_SCRIPT = f"[{COLORS['CYAN']}i{COLORS['RESET']}]"
ERROR_SCRIPT = f"[{COLORS['RED']}-{COLORS['RESET']}] Error: "
DONE_SCRIPT = f"[{COLORS['GREEN']}+{COLORS['RESET']}]"
SET_SCRIPT = f"[{COLORS['YELLOW']}>{COLORS['RESET']}]"
LOAD_CHARACTER = "█"

decorate(TITLE_SCRIPT)

inputs:dict[str, str] = {}

all_params_filled = True

decorate(f"{INFO_SCRIPT} Starting...".center(50, ' '), begin=False)
sleep(0.5)
for key, value in args._get_kwargs():
    if not value and key != 'verboose':
        all_params_filled = False
    if value == None and key != 'verboose':
        temp = input("[{}>{}] Enter a {}: ".format(COLORS["CYAN"],COLORS["RESET"],key))
        if (key == 'filename') and not temp.endswith('.cpp'):
            temp += '.cpp'
        inputs[key] = temp
    else:
        inputs[key] = value
try:
    if get_file(inputs['path'], inputs['filename']):
        all_params_filled = False
        rename = input(f"{SET_SCRIPT} File {inputs['filename']} founded. Rename? [Y/N]: ") or False
        new_name = False
        if rename.lower() == 'y':
                new_name = input(f"{SET_SCRIPT} Enter a new name: ") + '.cpp'
                rename_file(inputs['path'], inputs['filename'], new_name)
                decorate(f"{DONE_SCRIPT} {inputs['filename']} renamed to {new_name}",False, True, verboose=inputs['verboose'] == 'y')
        files = {\
            f"{new_name if rename.lower() == 'y' else inputs['filename']}":'#include <iostream>\n\nint main()\n{\n\tstd::cout << "Hello World!" << std::endl;\n\treturn 0;\n}',
            "start.bat": f"@echo off\ncls\ncolor 2\necho [!] Starting...\ng++ .\{new_name if rename.lower() == 'y' else inputs['filename']} -o bin\{new_name.split('.')[0] if rename.lower() == 'y' else inputs['filename'].split('.')[0]}\ncls\necho [+] Started\ncolor 7\npause\ncls\n.\\bin\{new_name.split('.')[0] if rename.lower() == 'y' else inputs['filename'].split('.')[0]}"
            }
    else:
        files = {
    f"{inputs['filename']}":'#include <iostream>\n\nint main()\n{\n\tstd::cout << "Hello World!" << std::endl;\n\treturn 0;\n}',
    "start.bat":f"@echo off\ncls\ncolor 2\necho [!] Starting...\ng++ .\{inputs['filename']} -o bin\{inputs['filename'].split('.')[0]}\ncls\necho [+] Started\ncolor 7\npause\ncls\n.\\bin\{inputs['filename'].split('.')[0]}"}
    i = 0

    total_progress = len(files)
    max_length_name = len(max(files.keys(), key=len))
    for file in files:
        i += 1
        progress = "{}{}".format(LOAD_CHARACTER*(i*10//total_progress), " "*(10-i*10//total_progress))
        create_file(inputs['path'], file, files[file])
        decorate(f"{DONE_SCRIPT} {file+' created ':20s}[{progress}] ({i}/{len(files)})", False, False, verboose=inputs['verboose'] == 'y',endl="\r")
        sleep(0.5)
    else:
        print()

    try:
        create_dir(inputs['path'], "bin")
        decorate(f"{DONE_SCRIPT} bin folder created", False, True, verboose=inputs['verboose'] == 'y')
    except:
        pass

except Exception as e:
    decorate(f'{ERROR_SCRIPT}{e}', final=False)
    exit()


decorate(END_SCRIPT, begin=not all_params_filled)
