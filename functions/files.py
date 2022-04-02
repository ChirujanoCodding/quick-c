import os

def get_file(path:str, file:str):
    if not os.path.exists(path):
        os.mkdir(path)
    list_path = os.listdir(path)
    return file in list_path

def create_file(path:str, file:str, content:str):
    try:
        with open(f'{path}/{file}', 'w') as f:
            f.write(content)
            f.close()
    except Exception as e:
        raise e

def rename_file(path:str, file:str, new_name:str):
    try:
        os.rename(f"{path}/{file}", f"{path}/{new_name}")
    except Exception as e:
        raise e

def create_dir(path:str, file:str):
    try:
        os.mkdir(f"{path}/{file}")
    except Exception as e:
        raise e