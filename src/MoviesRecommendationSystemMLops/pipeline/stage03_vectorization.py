from MoviesRecommendationSystemMLops.config.configuration import ConfigurationManager
from MoviesRecommendationSystemMLops.components.vectorization import Vectorization
from MoviesRecommendationSystemMLops import logger

STAGE_NAME = "Vectorization Stage"

class VectorizationPipeline:
    def __init__(self):
        pass 

    def main(self):
       config = ConfigurationManager()
       model_trainer_config = config.get_model_trainer_config()
       model_trainer_config = Vectorization(config=model_trainer_config)
       model_trainer_config.train()    

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = VectorizationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
    except Exception as e:
        logger.exception(e)
        raise e