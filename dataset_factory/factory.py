import random

class DatasetFactory:
    def __init__(self, seed: int = 42):
        random.seed(seed)

    def build_dataset(self, name: str, samples, train_ratio: float = 0.8):
        print(f"[DATASET] Building dataset '{name}' with {len(samples)} samples")
        samples = list(samples)
        random.shuffle(samples)
        split = int(len(samples) * train_ratio)
        train = samples[:split]
        val = samples[split:]
        print(f"[DATASET] Train: {len(train)} | Val: {len(val)}")
        return {"name": name, "train": train, "val": val}
