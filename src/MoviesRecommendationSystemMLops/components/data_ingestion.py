import os 
import urllib.request as request 
import zipfile
from MoviesRecommendationSystemMLops import logger 
from MoviesRecommendationSystemMLops.utils.common import get_size
from MoviesRecommendationSystemMLops.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config   

    def download_movies_file(self):
        if not os.path.exists(self.config.movies_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.movies_URL,
                filename= self.config.movies_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.movies_data_file))}")
    
    
    def download_credits_file(self):
        if not os.path.exists(self.config.credits_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.credits_URL,
                filename= self.config.credits_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.movies_data_file))}")




    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.movies_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.credits_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)