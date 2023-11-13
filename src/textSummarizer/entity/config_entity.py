from dataclasses import dataclass
from pathlib import Path


# Entity : it's a return type of a function , for this we importe dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path