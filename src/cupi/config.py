from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    model: str = "claude-3-5-sonnet-20241022"
    log_dir: str = "logs"
    max_tokens: int = 4096
    recent_images: int = 10
    verbose: bool = False


DEFAULT_CONFIG = Config()
