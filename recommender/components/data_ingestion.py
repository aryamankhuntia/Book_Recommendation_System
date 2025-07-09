import os
import sys
import urllib.request as urllib
import zipfile
from recommender.logger.log import logging
from recommender.exception.exception_handler import AppException
from recommender.config.configuration import Configuration

class DataIngestion:
    def __init__(self, app_config=Configuration()):
        try:
            logging.info(f"{'=' * 20} Data Ingestion {'=' * 20}")
            self.data_ingestion_config = app_config.get_data_ingestion_config()
        except Exception as e:
            raise AppException(e,sys) from e
        
    def download_data(self):
        try:
            dataset_url = self.data_ingestion_config.dataset_download_url
            zip_download_dir = self.data_ingestion_config.raw_data_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            data_file_name = os.path.basename(dataset_url)
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.info(f"Downloading data from {dataset_url} to {zip_file_path}")
            urllib.urlretrieve(dataset_url, zip_file_path)
            logging.info(f"Data Download Successful: {zip_file_path}")
            return zip_file_path
        except Exception as e:
            raise AppException(e, sys) from e
        
    def extract_data(self, zip_file_path: str):
        try:
            logging.info(f"Extracting data from {zip_file_path}")
            ingested_data_dir = self.data_ingestion_config.ingested_data_dir
            os.makedirs(ingested_data_dir, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(ingested_data_dir)
                logging.info(f"Data extracted to {ingested_data_dir}")
            logging.info("Data Extraction Successful")
        except Exception as e:
            print("check this",zipfile.is_zipfile(zip_file_path))
            raise AppException(e, sys) from e
        
    def initiate_data_ingestion(self):
        try:
            zip_file_path = self.download_data()
            self.extract_data(zip_file_path)
            logging.info(f"{'=' * 15}Data Ingestion Completed Successfully {'=' * 15}\n\n")
        except Exception as e:
            raise AppException(e, sys) from e