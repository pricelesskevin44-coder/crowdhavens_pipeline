#!/bin/bash
set -e

MODE=${1:-run-all}

echo "[Entrypoint] Starting CrowdHavens Pipeline — mode: $MODE"

case "$MODE" in
    run-all)
        python run_pipeline.py --mode run-all
        ;;
    train)
        python run_pipeline.py --mode train
        ;;
    eval)
        python run_pipeline.py --mode eval
        ;;
    serve)
        python deployment/serve.py
        ;;
    *)
        echo "[Entrypoint] Unknown mode: $MODE"
        echo "Valid modes: run-all | train | eval | serve"
        exit 1
        ;;
esac
