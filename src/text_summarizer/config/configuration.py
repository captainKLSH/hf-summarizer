from src.text_summarizer.constants import *
from src.text_summarizer.utils.common import readYaml, createDir
from src.text_summarizer.entity import DataIngestionConfig, DataTransformationConfig, ModelEvaluationConfig, ModelTrainingConfig

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

    def getDataTransformationConfig(self)-> DataTransformationConfig:
        config= self.config.dataTransformation

        createDir([config.rootDir])

        dataTransformConfig= DataTransformationConfig(
            rootDir= config.rootDir,
            dataPath= config.dataPath,
            tokenizerName= config.tokenizerName,
        )

        return dataTransformConfig
    
    def getModelTrainingConfig(self)-> ModelTrainingConfig:
        config=self.config.modelTrainer
        params= self.params.TrainingArgumets
        createDir([config.rootDir])
        modelTrainingConfig= ModelTrainingConfig(
            rootDir= config.rootDir,
            dataPath= config.dataPath,
            modelCkpt= config.modelCkpt,
            numTrainEpoch= params.numTrainEpoch,
            warmupSteps= params.warmupSteps,
            perDeviceTrainBatchSize= params.perDeviceTrainBatchSize,
            weightDecay= params.weightDecay,
            loggingSteps= params.loggingSteps,
            evaluationStratergy= params.evaluationStratergy,
            evalSteps= params.evalSteps,
            saveSteps= params.saveSteps,
            gradientAccumulationSteps= params.gradientAccumulationSteps,

        )

        return modelTrainingConfig
    def getModelEvalConfig(self)-> ModelEvaluationConfig:
        config=self.config.modelEvaluation
        createDir([config.rootDir])
        modelEvalConfig= ModelEvaluationConfig(
            rootDir= config.rootDir,
            dataPath=config.dataPath,
            modelPath= config.modelPath,
            tokenizerPath= config.tokenizerPath,
            metricFilePath= config.metricFilePath,

        )

        return modelEvalConfig

