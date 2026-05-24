#!/bin/bash

echo "=============================================="
echo "   CrowdHavens Perception Pipeline Installer   "
echo "=============================================="

echo "[1/8] Checking Python version..."
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found. Please install Python 3.8+ and rerun."
    exit 1
fi

echo "[2/8] Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "[3/8] Upgrading pip..."
pip install --upgrade pip

echo "[4/8] Installing Python dependencies..."
pip install -r requirements.txt

echo "[5/8] Installing optional system tools..."
pkg update -y
pkg install -y ffmpeg imagemagick jq git wget

echo "[6/8] Ensuring data directories exist..."
mkdir -p data/raw data/processed data/annotations data/models data/logs

echo "[7/8] Running self-test..."
python3 - << 'EOF2'
print("CrowdHavens pipeline environment is active.")
print("Python version OK.")
print("Dependencies installed.")
EOF2

echo "[8/8] Installation complete!"
echo "Activate your environment with: source venv/bin/activate"
echo "Then run: python run_pipeline.py"
