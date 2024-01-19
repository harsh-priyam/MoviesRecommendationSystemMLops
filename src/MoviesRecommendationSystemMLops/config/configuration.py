from MoviesRecommendationSystemMLops.constants import *
from MoviesRecommendationSystemMLops.utils.common import read_yaml,create_directories 
from MoviesRecommendationSystemMLops.entity.config_entity import (DataIngestionConfig,DataValidationConfig,ModelTrainerConfig)

class ConfigurationManager:
      def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH):
        
            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)
            self.schema = read_yaml(schema_filepath)

            create_directories([self.config.artifacts_root])

      def get_data_ingestion_config(self) -> DataIngestionConfig:
          config = self.config.data_ingestion 

          create_directories([config.root_dir])

          data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                movies_URL=config.movies_URL,
                credits_URL=config.credits_URL,
                movies_data_file=config.movies_data_file,
                credits_data_file=config.credits_data_file,
                unzip_dir=config.unzip_dir
          )       

          return data_ingestion_config
      
      def get_data_validation_config(self) -> DataValidationConfig:
          config = self.config.data_validation 
          schema = self.schema.COLUMNS

          create_directories([config.root_dir])

          data_validation_config = DataValidationConfig(
                root_dir=config.root_dir,
                STATUS_FILE=config.STATUS_FILE,
                unzip_movies_dir= config.unzip_movies_dir,
                unzip_credits_dir= config.unzip_credits_dir,
                all_schema=schema,
          )
          
          return data_validation_config
      

      def get_model_trainer_config(self) -> ModelTrainerConfig:
          config = self.config.model_trainer 
          params = self.params.CountVectorizer 
          schema = self.schema.COLUMNS
          
          create_directories([config.root_dir])

          model_trainer_config = ModelTrainerConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                movies_model_name= config.movies_model_name,
                similarity_model_name= config.similarity_model_name,
                max_features = params.max_features,
          )

          return model_trainer_config