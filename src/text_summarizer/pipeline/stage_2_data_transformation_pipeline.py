

from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self):
        pass

    def initDataTransform(self):
        config= ConfigurationManager()
        dataTransformationConfig =config.getDataTransformationConfig()
        dataTransformation= DataTransformation(config=dataTransformationConfig)
        dataTransformation.convert()