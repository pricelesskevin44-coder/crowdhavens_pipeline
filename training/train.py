import time
import random

class FakeModel:
    def __init__(self):
        self.weights = random.random()

    def predict(self, x):
        return self.weights * 0.5

class Trainer:
    def __init__(self, epochs=3):
        print(f"[Training] Trainer initialized (NO PyTorch, Termux-safe). epochs={epochs}")
        self.epochs = epochs
        self.model = FakeModel()

    def train(self, data):
        print("[Training] Starting fake training loop...")
        time.sleep(1)

        losses = []
        for epoch in range(self.epochs):
            loss = random.random()
            losses.append(loss)
            print(f"[Training] Epoch {epoch+1}/{self.epochs} — loss={loss:.4f}")
            time.sleep(0.5)

        print("[Training] Training complete.")
        return {"losses": losses}

    def save_model(self, path="data/models/fake_model.bin"):
        with open(path, "w") as f:
            f.write(str(self.model.weights))
        print(f"[Training] Model saved to {path}")

    def load_model(self, path="data/models/fake_model.bin"):
        try:
            with open(path, "r") as f:
                self.model.weights = float(f.read().strip())
            print(f"[Training] Model loaded from {path}")
        except FileNotFoundError:
            print("[Training] No saved model found.")
