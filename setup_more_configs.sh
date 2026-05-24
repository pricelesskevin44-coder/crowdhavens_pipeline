#!/bin/bash

echo "[1] Writing configs/evaluation.yaml..."
cat << 'YAML' > configs/evaluation.yaml
metrics:
  - accuracy
  - precision
  - recall
thresholds:
  min_accuracy: 0.60
YAML

echo "[2] Writing configs/trust.yaml..."
cat << 'YAML' > configs/trust.yaml
trust_thresholds:
  min_confidence: 0.50
  min_accuracy: 0.60
weights:
  accuracy_weight: 0.7
  confidence_weight: 0.3
YAML

echo "[3] Writing configs/deployment.yaml..."
cat << 'YAML' > configs/deployment.yaml
api:
  host: "0.0.0.0"
  port: 8080
model:
  path: "data/models/latest_model.bin"
logging:
  level: "INFO"
YAML

echo "[DONE] Additional configs created."
