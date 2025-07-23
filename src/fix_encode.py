from config import PATH
from pathlib import Path

def fix_encoding_recursive(data_node):
    if isinstance(data_node, dict):
        return {key: fix_encoding_recursive(value) for key, value in data_node.items()}
    elif isinstance(data_node, list):
        return [fix_encoding_recursive(item) for item in data_node]
    elif isinstance(data_node, str):
        try:
            return data_node.encode('latin-1').decode('utf-8')
        except (UnicodeEncodeError, UnicodeDecodeError):
            return data_node
    else:
        return data_node
    
def get_json_paths() -> list[Path]:
    json_paths = []

    for json_file in PATH.rglob('*.json'):
        if json_file.is_file():
            json_paths.append(json_file)
        
    return json_paths