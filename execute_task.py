from pathlib import Path
import sys
sys.path.append(str(Path(sys.argv[0]).parent))

import shutil

import logging
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter("[task] - %(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

from sitetaskexecutor.Sitetask.deploy_site_Sitetask import deploy_site_Sitetask
from sitetaskexecutor.Sitetask.upload_on_pypi_Sitetask import upload_on_pypi_Sitetask

if __name__ == '__main__':
    PATHFILE_home_pythonanywhereusername_root_sitetaskexecutor_executetaskpy = Path(sys.argv[0])
    PATHDIR_home_pythonanywhereusername_root_sitetaskexecutor = PATHFILE_home_pythonanywhereusername_root_sitetaskexecutor_executetaskpy.parent
    PATHDIR_home_pythonanywhereusername_root = PATHDIR_home_pythonanywhereusername_root_sitetaskexecutor.parent
    PATHDIR_home_pythonanywhereusername = PATHDIR_home_pythonanywhereusername_root.parent
    pythonanywhere_username = PATHDIR_home_pythonanywhereusername.name

    if pythonanywhere_username == 'ynsbuilder':
        task_Type = upload_on_pypi_Sitetask
    else:
        task_Type = deploy_site_Sitetask

    task_Type.from_PATHFILE_executetaskpy(
        PATHFILE_executetaskpy=PATHFILE_home_pythonanywhereusername_root_sitetaskexecutor_executetaskpy
    )._Execute()


    # update.py:
    logger.info('Writing update.py file...')

    FILENAME_updatepy = 'update.py'
    PATHFILE_home_pythonanywhereusername_root_sitetaskexecutor_updatepy = PATHDIR_home_pythonanywhereusername_root_sitetaskexecutor / FILENAME_updatepy
    PATHFILE_home_pythonanywhereusername_updatepy = PATHDIR_home_pythonanywhereusername / FILENAME_updatepy


    logger.info(
'''update.py paths:
PATHFILE_home_pythonanywhereusername_root_sitetaskexecutor_updatepy=%PATHFILE_home_pythonanywhereusername_root_sitetaskexecutor_updatepy%
PATHFILE_home_pythonanywhereusername_updatepy=%PATHFILE_home_pythonanywhereusername_updatepy%'''
        .replace('%PATHFILE_home_pythonanywhereusername_root_sitetaskexecutor_updatepy%', str(PATHFILE_home_pythonanywhereusername_root_sitetaskexecutor_updatepy))
        .replace('%PATHFILE_home_pythonanywhereusername_updatepy%', str(PATHFILE_home_pythonanywhereusername_updatepy))
    )

    shutil.copyfile(
        PATHFILE_home_pythonanywhereusername_root_sitetaskexecutor_updatepy,
        PATHFILE_home_pythonanywhereusername_updatepy
    )
    logger.info('Writed update.py file!')