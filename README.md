# CrowdHavens Perception Pipeline

A modular, configurable, container-ready computer-vision pipeline for robotics, autonomy, and distributed sensing. The system processes raw images through preprocessing, annotation, dataset creation, training, evaluation, and trust scoring, and includes a FastAPI inference server for real-time predictions.

## Features
- End-to-end pipeline: ingestion → preprocessing → annotation → dataset → training → evaluation → trust scoring  
- Config-driven via YAML  
- FastAPI inference server  
- Docker-ready unified entrypoint  
- Lightweight and Termux-safe  

## Pipeline Modes
- run-all — full pipeline  
- train — training only  
- eval — evaluation only  
- serve — API server  

Run:
python run_pipeline.py --mode run-all

## API Usage
Start server:
docker run -p 8080:8080 crowdhavens/pipeline serve

Send an image:
curl -X POST http://localhost:8080/predict -F "file=@image.jpg"

Response:
{
  "accuracy": 0.70,
  "trust_score": 0.47
}

## Docker
Build:
docker build -t crowdhavens/pipeline .

Run:
docker run --rm crowdhavens/pipeline run-all

Serve API:
docker run -p 8080:8080 crowdhavens/pipeline serve

## Configuration
Configs live in `configs/`:
- training.yaml  
- evaluation.yaml  
- trust.yaml  
- deployment.yaml  

## Project Structure
crowdhavens_pipeline/
├── annotation/
├── preprocessing/
├── dataset/
├── training/
├── evaluation/
├── runtime_trust/
├── deployment/serve.py
├── configs/
├── entrypoint.sh
├── run_pipeline.py
├── config_loader.py
└── Dockerfile

## License
MIT or your preferred license.
