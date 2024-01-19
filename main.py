from MoviesRecommendationSystemMLops import logger
from MoviesRecommendationSystemMLops.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from MoviesRecommendationSystemMLops.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from MoviesRecommendationSystemMLops.pipeline.stage03_vectorization import VectorizationPipeline



STAGE_NAME = "Data Ingestion stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Vectorization stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = VectorizationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e