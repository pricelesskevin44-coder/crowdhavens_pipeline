import os
import argparse

from preprocessing.preprocess import PreprocessingPipeline
from annotation.annotate import Annotator
from dataset.dataset import DatasetFactory
from training.train import Trainer
from evaluation.eval import Evaluator
from runtime_trust.trust import RuntimeTrust
from config_loader import load_config

RAW_DIR = "data/raw"

def collect_images():
    if not os.path.isdir(RAW_DIR):
        print(f"[System] Creating missing directory: {RAW_DIR}")
        os.makedirs(RAW_DIR, exist_ok=True)

    images = []
    for f in os.listdir(RAW_DIR):
        path = os.path.join(RAW_DIR, f)
        if os.path.isfile(path) and f.lower().endswith((".jpg", ".jpeg", ".png")):
            images.append(path)

    print(f"[System] Found {len(images)} image(s) in {RAW_DIR}")
    return images

def run_full_pipeline():
    print("=== CrowdHavens Perception Pipeline (Professional Mode) ===")

    training_cfg = load_config("configs/training.yaml")

    raw_data = collect_images()

    pre = PreprocessingPipeline()
    processed = pre.process(raw_data)

    ann = Annotator()
    annotated = ann.annotate(processed)

    ds = DatasetFactory()
    dataset = ds.build(annotated)

    trainer = Trainer(
        epochs=training_cfg.get("epochs", 3),
        batch_size=training_cfg.get("batch_size", 8),
        learning_rate=training_cfg.get("learning_rate", 0.001),
        augmentations=training_cfg.get("augmentations", {})
    )
    trainer.train(dataset)

    evaluator = Evaluator()
    eval_results = evaluator.evaluate(trainer.model, dataset)

    trust = RuntimeTrust()
    trust.compute_trust(eval_results.get("accuracy", 0.0))

def run_training_only():
    training_cfg = load_config("configs/training.yaml")

    raw_data = collect_images()
    pre = PreprocessingPipeline()
    processed = pre.process(raw_data)

    ann = Annotator()
    annotated = ann.annotate(processed)

    ds = DatasetFactory()
    dataset = ds.build(annotated)

    trainer = Trainer(
        epochs=training_cfg.get("epochs", 3),
        batch_size=training_cfg.get("batch_size", 8),
        learning_rate=training_cfg.get("learning_rate", 0.001),
        augmentations=training_cfg.get("augmentations", {})
    )
    trainer.train(dataset)

def run_evaluation_only():
    raw_data = collect_images()
    pre = PreprocessingPipeline()
    processed = pre.process(raw_data)

    ann = Annotator()
    annotated = ann.annotate(processed)

    ds = DatasetFactory()
    dataset = ds.build(annotated)

    trainer = Trainer()
    evaluator = Evaluator()
    evaluator.evaluate(trainer.model, dataset)

def main():
    parser = argparse.ArgumentParser(description="CrowdHavens Perception Pipeline")
    parser.add_argument(
        "--mode",
        choices=["run-all", "train", "eval"],
        default="run-all",
        help="Select pipeline mode",
    )
    args = parser.parse_args()

    if args.mode == "run-all":
        run_full_pipeline()
    elif args.mode == "train":
        run_training_only()
    elif args.mode == "eval":
        run_evaluation_only()

if __name__ == "__main__":
    main()
