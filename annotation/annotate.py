import time

class Annotator:
    def __init__(self):
        print("[Annotation] Annotator initialized (Termux-safe).")

    def annotate(self, data):
        print("[Annotation] Starting annotation...")
        time.sleep(0.5)

        annotated = []
        for idx, item in enumerate(data):
            annotated.append({
                "id": idx,
                "data": item,
                "label": "unlabeled"  # placeholder label
            })

        print(f"[Annotation] Completed. {len(annotated)} items annotated.")
        return annotated
