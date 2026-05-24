from pathlib import Path

class IngestionPipeline:
    def __init__(self, raw_dir: str = "data/raw"):
        self.raw_dir = Path(raw_dir)
        self.raw_dir.mkdir(parents=True, exist_ok=True)

    def ingest_from_folder(self, source_dir: str = "data/raw"):
        source = Path(source_dir)
        if not source.exists():
            raise FileNotFoundError(f"Source folder not found: {source}")
        files = [p for p in source.glob("**/*") if p.is_file()]
        print(f"[INGEST] Found {len(files)} files in {source}")
        samples = [{"path": str(f)} for f in files]
        return samples
