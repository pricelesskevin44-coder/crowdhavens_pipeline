from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from training.train import Trainer
from evaluation.eval import Evaluator
from runtime_trust.trust import RuntimeTrust
from preprocessing.preprocess import PreprocessingPipeline
from annotation.annotate import Annotator
from dataset.dataset import DatasetFactory
import uvicorn
import os

app = FastAPI(title="CrowdHavens Perception API")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Save temp file
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    # Preprocess
    pre = PreprocessingPipeline()
    processed = pre.process([temp_path])

    # Annotate
    ann = Annotator()
    annotated = ann.annotate(processed)

    # Build dataset
    ds = DatasetFactory()
    dataset = ds.build(annotated)

    # Fake model load + inference
    trainer = Trainer()
    evaluator = Evaluator()
    results = evaluator.evaluate(trainer.model, dataset)

    # Trust score
    trust = RuntimeTrust()
    trust_score = trust.compute_trust(results.get("accuracy", 0.0))

    # Cleanup
    os.remove(temp_path)

    return JSONResponse({
        "accuracy": results.get("accuracy", 0.0),
        "trust_score": trust_score
    })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
