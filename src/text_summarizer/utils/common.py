import os
from box.exceptions import BoxValueError

import yaml
from src.text_summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def readYaml(pathToYaml: Path)->ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(pathToYaml) as yamlFiles:
            content=yaml.safe_load(yamlFiles)
            logger.info(f"YAML file:{pathToYaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def createDir(pathToDir: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in pathToDir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory Created at: {path}")