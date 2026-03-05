from src.text_summarizer.constants import *
from src.text_summarizer.utils.common import readYaml, createDir
from src.text_summarizer.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_path=CONFIG_FILE_PATH, params_path= PARAMS_FILE_PATH):
        self.config=readYaml(config_path)
        self.params=readYaml(params_path)

        createDir([self.config.artifactsRoot])

    def getDataIngestionConfig(self)-> DataIngestionConfig:
        config=self.config.dataIngestion
        createDir([config.rootDir])

        dataIngestionConfig = DataIngestionConfig(
            rootDir =config.rootDir,
            sourceURL= config.sourceURL,
            localDataFile= config.localDataFile,
            unzipDir= config.unzipDir,
            )
        return dataIngestionConfig
