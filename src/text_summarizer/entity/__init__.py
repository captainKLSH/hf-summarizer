from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    rootDir : Path
    sourceURL: Path
    localDataFile: Path
    unzipDir: Path

@dataclass
class DataTransformationConfig:
    rootDir: Path
    dataPath: Path
    tokenizerName: Path

@dataclass
class ModelTrainingConfig:
    rootDir: Path
    dataPath: Path
    modelCkpt: Path
    numTrainEpoch: int
    warmupSteps: int
    perDeviceTrainBatchSize: int
    weightDecay: float
    loggingSteps: int
    evaluationStratergy: str
    evalSteps: int
    saveSteps: int
    gradientAccumulationSteps: int