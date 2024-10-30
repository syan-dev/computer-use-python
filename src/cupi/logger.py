import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


class ConversationLogger:
    def __init__(self, output_dir: str = "logs"):
        self.output_dir = output_dir
        self.conversation_data = {
            "timestamp": datetime.now().isoformat(),
            "messages": [],
            "screenshots": {},
            "metadata": {"args": None, "version": "1.0.0"},
        }
        Path(output_dir).mkdir(parents=True, exist_ok=True)

    def set_metadata(self, metadata: dict) -> None:
        self.conversation_data["metadata"].update(metadata)

    def add_message(self, role: str, content: Any) -> None:
        self.conversation_data["messages"].append(
            {"role": role, "content": content, "timestamp": datetime.now().isoformat()}
        )

    def add_screenshot(self, tool_use_id: str, base64_image: str) -> None:
        self.conversation_data["screenshots"][tool_use_id] = base64_image

    def save(self) -> str:
        filename = f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = Path(self.output_dir) / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.conversation_data, f, indent=2, ensure_ascii=False)
        return str(filepath)
