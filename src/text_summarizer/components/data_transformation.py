import os
from src.text_summarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk

from src.text_summarizer.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config=config
        self.tokenizer=AutoTokenizer.from_pretrained(config.tokenizerName)

    def examplesToFunctions(self,exmBatch):
        inputEncoding=self.tokenizer(exmBatch['dialogue'],max_length=1024, truncation= True)

        targetEncodings=self.tokenizer(exmBatch['summary'],max_length=128, truncation= True)
        return {
            'inputIds': inputEncoding['input_ids'],
            'attentionMask': inputEncoding['attention_mask'],
            'labels': targetEncodings['input_ids']

        }
    def convert(self):
        dfSamsum=load_from_disk(self.config.dataPath)
        dfSamsumPt=dfSamsum.map(self.examplesToFunctions,batched=True)
        dfSamsumPt.save_to_disk(os.path.join(self.config.rootDir,"samsum_dataset"))
        