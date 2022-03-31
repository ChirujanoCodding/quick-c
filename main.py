import argparse, os
from colorama import Fore, init
# crea un argparse
init()
parser = argparse.ArgumentParser(description='[!] This script make a quick-start c++ program.')

parser.add_argument('-d','--directory',help='Directory where the program will be created.', required=True)
parser.add_argument('-n','--name',help='Name of the program.', required=False)

args = parser.parse_args()

directory = args.directory
filename = args.name or 'main'
replace_ = 'n'

print('-'*30)
print('['+Fore.CYAN+'!'+Fore.RESET+'] Quick-start c++ program')
print('-'*30)


if not os.path.exists(directory):
    print('['+Fore.LIGHTYELLOW_EX+'!'+Fore.RESET+'] Creating Directory...')
    print('-'*30)
    os.mkdir(directory)
else:
    print('['+Fore.LIGHTYELLOW_EX+'!'+Fore.RESET+'] Started Directory already.')
    print('-'*30)

counter = 0

for file in os.listdir(directory):
        if file.endswith('.cpp'):
            replace_ = input('['+Fore.LIGHTYELLOW_EX+'?'+Fore.RESET+'] Detected File '+file.split('.')[0]+'.cpp\n['+Fore.LIGHTYELLOW_EX+'?'+Fore.RESET+'] Replace name ? [y/n] ')
            print('-'*30)
            filename = filename if replace_ == "y" else file.split('.')[0]
            os.rename(directory+'/'+file,directory+'/'+filename+'.cpp')
            break
else:
        print('['+Fore.LIGHTYELLOW_EX+'!'+Fore.RESET+'] Creating File... ('+filename+'.cpp)')
        print('-'*30)
        with open(os.path.join(directory,filename+'.cpp'),'w') as file:
            file.write('#include <iostream>\n\nint main()\n{\n\tstd::cout << "Hello World!" << std::endl;\n\treturn 0;\n}')

files = {
    f"{filename}.cpp":'#include <iostream>\n\nint main()\n{\n\tstd::cout << "Hello World!" << std::endl;\n\treturn 0;\n}',
    "start.bat":f"@echo off\ncls\ncolor 2\necho [!] Starting...\ng++ .\{filename}.cpp -o bin\{filename}\ncls\necho [+] Started\ncolor 7\npause\ncls\n.\\bin\{filename}"}


for file in files:
        counter += 1
        if (os.path.exists(directory+'/'+file) and (file.split('.')[0] == filename) and replace_ and replace_ == 'y'):
            print('['+Fore.LIGHTYELLOW_EX+'!'+Fore.RESET+'] Modifying file: '+file+ ' ('+str(counter)+'/'+str(len(files))+')')
            continue
        with open(directory+'/'+file,'w') as f:
            print('['+Fore.LIGHTYELLOW_EX+'!'+Fore.RESET+'] Creating file: '+file+ ' ('+str(counter)+'/'+str(len(files))+')', end='\r')
            f.write(files[file])
            f.close()
        print()

if not os.path.exists(directory+'/bin'):
    print('['+Fore.LIGHTYELLOW_EX+'!'+Fore.RESET+'] Creating bin directory...')
    os.mkdir(directory+'/bin')

if counter == len(files):
    print('-'*30)
    print('['+Fore.GREEN+'+'+Fore.RESET+'] Done!')
    print('-'*30)