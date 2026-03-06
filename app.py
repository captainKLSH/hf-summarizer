from fastapi import FastAPI
import os
import sys
import uvicorn
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.text_summarizer.pipeline.prediction_pipeline import PredictionPipeline

text : str = "What is text Summarization"

app=FastAPI()
@app.get('/',tags=["authntication"])
async def index():
    return RedirectResponse(url= "/docs")

@app.get('/train')
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful!")
    except Exception as e:
        return Response(f"Error Occured: {e}")
    
@app.post("/predict")
async def predictRoute(text):
    try:
        obj=PredictionPipeline()
        text=obj.predict(text)
        return text
    except Exception as e:
        raise e
    
if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0", port=8000)
    