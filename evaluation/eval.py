import random
import time

class Evaluator:
    def __init__(self):
        print("[Evaluation] Evaluator initialized (NO PyTorch, Termux-safe).")

    def evaluate(self, model, data):
        print("[Evaluation] Starting fake evaluation...")
        time.sleep(1)

        # Fake accuracy + trust score
        accuracy = random.uniform(0.4, 0.9)
        trust = random.uniform(0.3, 0.8)

        print(f"[Evaluation] Accuracy: {accuracy:.3f}")
        print(f"[Evaluation] Trust score: {trust:.3f}")

        return {
            "accuracy": accuracy,
            "trust": trust
        }
