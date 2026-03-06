

from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.model_training import ModelTraining


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initModelTrain(self):
        config= ConfigurationManager()
        modelTrainConfig =config.getModelTrainingConfig()
        modelTrain= ModelTraining(config=modelTrainConfig)
        modelTrain.train()