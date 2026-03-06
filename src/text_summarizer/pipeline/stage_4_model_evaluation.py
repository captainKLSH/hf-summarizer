from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.model_evaluation import ModelEval


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initModelEval():
        config = ConfigurationManager()
        modelEvalConfig = config.getModelEvalConfig()
        modelEvalutaion= ModelEval(config=modelEvalConfig)
        modelEvalutaion.evaluate()