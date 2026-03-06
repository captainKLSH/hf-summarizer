from src.text_summarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().getModelEvalConfig()

    def predict(self,text):
        tokenizer= AutoTokenizer.from_pretrained(self.config.tokenizerPath)
        genKwargs={"length_penalty": .8, "num_beams":8,"max_length":128}
        pipe= pipeline("text-generation",model=self.config.modelPath,tokenizer=tokenizer)
        print("Dialogue: ")
        print(text)
        output=pipe(text, **genKwargs)[0]["generated_text"]
        print("\n Model Summary: ")
        print(output)
        return output

