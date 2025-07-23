import logging
from pprint import pformat

from src.fix_encode import get_json_paths, fix_encoding_recursive
from utils.p_json import read_json, write_json
from config import OUTPUT_PATH, PATH
from src.setup_log import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

'''取得全部的 json file path'''
logger.info('Getting path...')

paths = get_json_paths()

if not paths:
    raise FileNotFoundError('找不到任何 .json 檔案')
logger.debug(f'Got paths: {pformat(paths, 4)}')
logger.info(f'Total found {len(paths)} files')
''''''

'''開始修復 json'''
logger.info(f"Fixing encode...  Using Path: {OUTPUT_PATH or PATH}")
successed = 0
failed = 0

for path in paths:
    try:
        d = read_json(path)
        fixed_d = fix_encoding_recursive(d)

        relative_path = path.relative_to(PATH)
        writen_path = OUTPUT_PATH.joinpath(relative_path) if OUTPUT_PATH else path.parent
        writen_path.mkdir(parents=True, exist_ok=True)

        write_json(fixed_d, writen_path.joinpath(path.name))
        successed += 1
    except:
        logger.error('Error accured...', exc_info=True)
        failed += 1

logger.info(f'Fixed {successed} files, failed {failed}')
''''''