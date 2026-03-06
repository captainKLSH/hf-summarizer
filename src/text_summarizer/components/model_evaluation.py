from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk
import evaluate
import torch
import pandas as pd
from tqdm import tqdm

from src.text_summarizer.entity import ModelEvaluationConfig



class ModelEval:
    def __init__(self, config=ModelEvaluationConfig):
        self.config = config

    def generateBatchChunks(self, LoE, batchSize):
        for i in range(0, len(LoE), batchSize):
            yield LoE[i : i + batchSize]

    def calMetricTest(
        self,
        dataset,
        metric,
        model,
        tokenizer,
        batchSize=16,
        device="cuda" if torch.cuda.is_available() else "cpu",
        columnText="article",
        columnSummary="highlights",
    ):
        articleBatches = list(self.generateBatchChunks(dataset[columnText], batchSize))
        targetBatches = list(
            self.generateBatchChunks(dataset[columnSummary], batchSize)
        )

        for articleBatch, targetBatch in tqdm(
            zip(articleBatches, targetBatches), total=len(articleBatches)
        ):

            inputs = tokenizer(
                articleBatch,
                max_length=1024,
                truncation=True,
                padding="max_length",
                return_tensors="pt",
            )

            summaries = model.generate(
                input_ids=inputs["input_ids"].to(device),
                attention_mask=inputs["attention_mask"].to(device),
                length_penalty=0.8,
                num_beams=8,
                max_length=128,
            )
            """ parameter for length penalty ensures that the model does not generate sequences that are too long. """

            # Finally, we decode the generated texts,
            # replace the  token, and add the decoded texts with the references to the metric.
            decodedSummaries = [
                tokenizer.decode(
                    s, skip_special_tokens=True, clean_up_tokenization_spaces=True
                )
                for s in summaries
            ]

            decodedSummaries = [d.replace("", " ") for d in decodedSummaries]

            metric.add_batch(predictions=decodedSummaries, references=targetBatch)

        #  Finally compute and return the ROUGE scores.
        score = metric.compute()
        return score
    
    def evaluate(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizerPath)
        modelPegasus= AutoModelForSeq2SeqLM.from_pretrained(self.config.modelPath).to(device)
        dfSampt= load_from_disk(self.config.dataPath)
        rougeNames = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
        rougeMetric = evaluate.load('rouge')

        score = self.calMetricTest(dfSampt['test'][0:10], rougeMetric, modelPegasus, tokenizer, batchSize = 2, columnText = 'dialogue', columnSummary= 'summary')

        # Directly use the scores without accessing fmeasure or mid
        rougeDict = {rn: score[rn] for rn in rougeNames}
        df = pd.DataFrame(rougeDict, index=[f'pegasus'])
        df.to_csv(self.config.metricFilePath,index=False)
