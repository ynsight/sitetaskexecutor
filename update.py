import shutil, subprocess, sys
from pathlib import Path

import logging
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter("[update] - %(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


if __name__ == '__main__':

    logger.info('Resolving paths...')
    PATHFILE_updatepy = Path(sys.argv[0])
    PATHDIR_root = PATHFILE_updatepy.parent / 'root'
    PATHDIR_root_sitetaskexecutor = PATHDIR_root / 'sitetaskexecutor'
    PATHFILE_root_sitetaskexecutor_executetaskpy = PATHDIR_root_sitetaskexecutor / 'execute_task.py'

    logger.info(
'''PATHFILE_updatepy=%PATHFILE_updatepy%
PATHDIR_root=%PATHDIR_root%
PATHDIR_root_sitetaskexecutor=%PATHDIR_root_sitetaskexecutor%
PATHFILE_root_sitetaskexecutor_executetaskpy=%PATHFILE_root_sitetaskexecutor_executetaskpy%'''
          .replace('%PATHFILE_updatepy%', str(PATHFILE_updatepy))
          .replace('%PATHDIR_root%', str(PATHDIR_root))
          .replace('%PATHDIR_root_sitetaskexecutor%', str(PATHDIR_root_sitetaskexecutor))
          .replace('%PATHFILE_root_sitetaskexecutor_executetaskpy%', str(PATHFILE_root_sitetaskexecutor_executetaskpy))
    )
    logger.info('Resolved paths!')


    logger.info('Creating root dir...')
    if PATHDIR_root.is_dir():
        shutil.rmtree(
            PATHDIR_root,
            ignore_errors=True
        )
    PATHDIR_root.mkdir(
        parents=True
    )
    logger.info('Created root dir!')


    logger.info('Updating sitetask package...')
    subprocess.run(
        ['git', 'clone', 'https://github.com/ynsight/sitetaskexecutor.git'],
        cwd=str(PATHDIR_root)
    )
    logger.info('Updated sitetask package!')


    logger.info('Running sitetask package...')
    subprocess.run(
        ['python3.6', PATHFILE_root_sitetaskexecutor_executetaskpy]
    )
    logger.info('Runned sitetask package!')