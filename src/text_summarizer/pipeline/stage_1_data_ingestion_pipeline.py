from src.text_summarizer.components.data_ingestion import DataIngestion
from src.text_summarizer.config.configuration import ConfigurationManager


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiateDataIngestion(self):
        config= ConfigurationManager()
        dataIngestConfig= config.getDataIngestionConfig()
        dataIngestion= DataIngestion(config=dataIngestConfig)

        dataIngestion.downloadFile()
        dataIngestion.extractZipFile()
