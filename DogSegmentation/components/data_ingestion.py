import os
import gdown
import sys
import zipfile
from DogSegmentation.logger import logging
from DogSegmentation.exception import AppException
from DogSegmentation.entity.config_entity import DataIngestionConfig
from DogSegmentation.entity.artifacts_entity import DataIngestionArtifact

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise AppException(e,sys)
        
    def download_data(self)-> str:
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            data_file_name = "data.zip"
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.info("Downloading data from {dataset_url} into file {zip_file_path}")

            file_id = dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_file_path)

            logging.info(f"Data downloaded from {dataset_url} at {zip_file_path}")

            return zip_file_path

        except Exception as e:
            raise AppException(e,sys)
        
    def extract_zip_file(self, zip_file_path: str)-> str:
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok=True)

            with zipfile.ZipFile(zip_file_path,'r') as zip_ref:
                zip_ref.extractall(feature_store_path)

            logging.info(f"Extracting all files: {zip_file_path} into dir: {feature_store_path}")

            return feature_store_path
        
        except Exception as e:
            raise AppException(e,sys)
        
    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        logging.info("Entered initiate_data_ingestion of Data_Ingestion_Class")
        try:
            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path)

            data_ingestion_artifacts = DataIngestionArtifact(
                data_zip_file_path= zip_file_path,
                feature_store_path= feature_store_path
            )

            logging.info("Exited initiate_data_ingestion method of Data_Ingestion class.")
            logging.info(f"Data ingestion artifacts: {data_ingestion_artifacts}")

            return data_ingestion_artifacts
        
        except Exception as e:
            raise AppException(e,sys)