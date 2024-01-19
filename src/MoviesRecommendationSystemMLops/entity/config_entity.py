from dataclasses import dataclass 
from pathlib import Path  

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    movies_URL: str
    credits_URL: str
    movies_data_file: Path
    credits_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str 
    unzip_movies_dir: Path 
    unzip_credits_dir: Path 
    all_schema: dict 

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path 
    movies_model_name: str 
    similarity_model_name: str
    max_features: int 