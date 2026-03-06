import os

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
import torch
from datasets import load_from_disk

from src.text_summarizer.entity import ModelTrainingConfig

class ModelTraining:
    def __init__(self, config= ModelTrainingConfig):
        self.config=config
        
    def train(self):
        device= "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer= AutoTokenizer.from_pretrained(self.config.modelCkpt)
        modelPegasus= AutoModelForSeq2SeqLM.from_pretrained(self.config.modelCkpt).to(device)
        seq2SeqDataCollator = DataCollatorForSeq2Seq(tokenizer,model= modelPegasus)

        # loading data
        dfSamsumPt = load_from_disk(self.config.dataPath)

        # the dataset already includes tokenized fields from transformation stage;
        # Trainer expects `input_ids` and `attention_mask` names, so rename columns
        dfSamsumPt = dfSamsumPt.rename_column("inputIds", "input_ids")
        dfSamsumPt = dfSamsumPt.rename_column("attentionMask", "attention_mask")

        trainingArgs= TrainingArguments(
            output_dir=self.config.rootDir,
            num_train_epochs= self.config.numTrainEpoch,
            warmup_steps= self.config.warmupSteps,
            per_device_train_batch_size= self.config.perDeviceTrainBatchSize,
            per_device_eval_batch_size=1,
            weight_decay= self.config.weightDecay,
            logging_steps= self.config.loggingSteps,
            # evaluation_stratergy = self.config.evaluationStratergy,
            eval_steps= self.config.evalSteps,
            save_steps= 1,
            gradient_accumulation_steps= self.config.gradientAccumulationSteps,
        )
        trainer=Trainer(model= modelPegasus, args=trainingArgs,processing_class=tokenizer,
                        data_collator=seq2SeqDataCollator, train_dataset=dfSamsumPt['train'],
                        eval_dataset=dfSamsumPt['validation'])
        trainer.train()

        modelPegasus.save_pretrained(os.path.join(self.config.rootDir,'pegasus_samsum_model'))
        tokenizer.save_pretrained(os.path.join(self.config.rootDir,'tokenizer'))