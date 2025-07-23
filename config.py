from pathlib import Path

from utils.p_json import read_json

SETTING = {}
PATH = None
OUTPUT_PATH = None

def get_setting():
    if not Path('setting.json').exists():
        raise FileNotFoundError('找不到 setting.json，請先將 setting.json.example 改為 setting.json')

    global SETTING
    SETTING = read_json('setting.json')
    
def get_path():
    path = read_json('setting.json').get('path')
    if not path: 
        raise KeyError('請在 setting.json 當中填入 path 變數')
    
    global PATH
    PATH = Path(path)

get_setting()
get_path()

OUTPUT_PATH = Path(SETTING.get('output_path'))