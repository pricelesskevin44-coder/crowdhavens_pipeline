import time

class DatasetFactory:
    def __init__(self):
        print("[Dataset] DatasetFactory initialized (Termux-safe).")

    def build(self, annotated_data):
        print("[Dataset] Building dataset...")
        time.sleep(0.5)

        dataset = []
        for item in annotated_data:
            dataset.append({
                "id": item["id"],
                "data": item["data"],
                "label": item["label"]
            })

        print(f"[Dataset] Dataset built with {len(dataset)} samples.")
        return dataset
