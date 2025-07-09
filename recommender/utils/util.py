import yaml
import sys
from recommender.exception.exception_handler import AppException
from recommender.logger.log import logging

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            content = yaml.safe_load(file)
        return content
    except Exception as e:
        logging.error(f"Error reading YAML file: {file_path}, Error: {e}")
        raise AppException(e, sys) from e