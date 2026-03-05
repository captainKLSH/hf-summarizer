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