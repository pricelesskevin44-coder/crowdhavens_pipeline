from PIL import Image
import os

class PreprocessingPipeline:
    def __init__(self):
        print("[Preprocessing] Pipeline initialized (Pillow backend)")

    def load_image(self, path):
        try:
            img = Image.open(path).convert("RGB")
            print(f"[Preprocessing] Loaded image: {path}")
            return img
        except Exception as e:
            print(f"[Preprocessing] Failed to load image {path}: {e}")
            return None

    def process(self, data):
        processed = []
        for item in data:
            if os.path.isfile(item):
                img = self.load_image(item)
                if img is not None:
                    processed.append(img)
            else:
                print(f"[Preprocessing] Skipping non-file: {item}")
        print(f"[Preprocessing] Completed. {len(processed)} items processed.")
        return processed
