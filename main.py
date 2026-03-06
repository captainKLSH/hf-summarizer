from src.text_summarizer.logging import logger
from src.text_summarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.text_summarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationPipeline
from src.text_summarizer.pipeline.stage_3_model_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    dataIngestPipeline=DataIngestionTrainingPipeline()
    dataIngestPipeline.initiateDataIngestion()
    logger.info(f"Stage: {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    dataTransformPipeline=DataTransformationPipeline()
    dataTransformPipeline.initDataTransform()
    logger.info(f"Stage: {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training stage"
try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    modelTrainPipeline=ModelTrainingPipeline()
    modelTrainPipeline.initModelTrain()
    logger.info(f"Stage: {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e