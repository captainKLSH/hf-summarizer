# 📚 hf‑summarizer

A Python project for training and serving a text‑summarization model using Hugging Face datasets and transformers. The repo is structured as a multi‑stage pipeline with clear separation of concerns: data ingestion, transformation, model training, evaluation, and prediction.

---

## 🔍 Project Overview

This repository implements a modular NLP pipeline:

1. **Data Ingestion** – download and prepare raw data.
2. **Data Transformation** – process and convert data to model‑ready format.
3. **Model Training** – fine‑tune a Pegasus summarization model on the SAMSum dataset.
4. **Model Evaluation** – compute evaluation metrics and save results.
5. **Prediction Service** – expose a FastAPI app for inference.

Models, intermediate artifacts, and logs are persisted under artifacts.

---

## 🗂️ Repository Structure

```text
.
├── app.py                   # FastAPI application for training & prediction
├── main.py                  # Entry point executing all pipeline stages
├── template.py              # (unused placeholder)
├── params.yaml              # Hyper‑parameters and config values
├── requirements.txt
├── pyproject.toml
├── setup.py
├── README.md
├── artifacts/               # Outputs of each pipeline stage
├── config/                  # YAML configuration files
├── src/
│   └── text_summarizer/
│       ├── components/      # Stage logic (ingestion, transform, etc.)
│       ├── pipeline/        # Pipeline orchestrators & prediction logic
│       ├── config/          # Configuration loader
│       ├── constants/       # Shared constants
│       ├── entity/          # Data models / dataclasses
│       ├── logging/         # Custom logger
│       └── utils/           # Helper functions
└── research/                 # Jupyter notebooks for experimentation
```

---

## ⚙️ Configuration

- **params.yaml** – training hyper‑parameters (batch size, epochs, learning rate, etc.).
- **config.yaml** – file paths for raw and processed data, model directories, etc.
- **configuration.py** – loads and validates the YAML files into Python objects.

Make sure paths in the YAMLs point to valid locations before running the pipeline.

---

## 🛠️ Setup

1. **Clone and enter the repo**

   ```bash
   git clone <repo-url>
   cd hf-summarizer
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *(Also included in pyproject.toml and setup.py for packaging.)*

4. **Populate data**

   - The SAMSum dataset is already included under samsum_dataset.
   - If you need to ingest new data, modify data_ingestion.py.

---

## 🚀 Running the Pipeline

The entire pipeline is orchestrated from main.py. Simply execute:

```bash
python main.py
```

Each stage logs start/completion messages via the custom `logger` and captures exceptions.

Stages:

- **Data Ingestion:** `DataIngestionTrainingPipeline.initiateDataIngestion()`
- **Data Transformation:** `DataTransformationPipeline.initDataTransform()`
- **Model Training:** `ModelTrainingPipeline.initModelTrain()`
- **Model Evaluation:** `ModelEvaluationPipeline.initModelEval()`

Outputs are placed under artifacts according to stage.

---

## 🧠 Model Training & Evaluation

Training uses a pre‑trained Pegasus model fine‑tuned on the SAMSum conversation summarization dataset.

- Configurable via params.yaml.
- Trained weights saved to pegasus_samsum_model.
- Evaluation metrics written to metrics.csv.

Refer to model_training.py and `model_evaluation.py` for details.

---

## 📡 Deployment & Inference

The FastAPI app at app.py exposes two endpoints:

- **`GET /`** – redirect to docs.
- **`GET /train`** – runs `python main.py` to retrain the pipeline.
- **`POST /predict`** – accepts raw text in the request body, returns a summary.

Example prediction using `curl`:

```bash
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" \
     -d '{"text":"Your conversation text here"}'
```


Start the server locally:

```bash
python app.py
uvicorn app:app --reload
```

---

## 📁 Development Helpers

- Notebooks in research demonstrate each stage interactively.
- Common utilities (e.g. `save_object`, `load_object`) live in common.py.
- Logging is configured in ___init__.py._

---

## 📌 Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make changes and add tests if applicable.
4. Submit a pull request with a clear description.

---

## ⚠️ Notes & Tips

- Ensure versions in requirements.txt match your environment.
- Large model files are stored as `*.safetensors` under artifacts.
- Cleaning up artifacts may be necessary to re‑run experiments from scratch.

---

## 📄 License

This project is released under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---
