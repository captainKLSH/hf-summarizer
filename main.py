from src.text_summarizer.logging import logger
from src.text_summarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    dataIngestPipeline=DataIngestionTrainingPipeline()
    dataIngestPipeline.initiateDataIngestion()
    logger.info(f"Stage: {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e
    