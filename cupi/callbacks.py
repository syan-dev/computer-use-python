import os
import json
import base64
from pathlib import Path
from typing import Callable, Dict
from anthropic import APIResponse
from anthropic.types.beta import BetaMessage

from cupi.computer_use_demo.tools import ToolResult
from cupi.logger import ConversationLogger
from cupi.config import Config


def create_callbacks(logger: ConversationLogger, config: Config) -> Dict[str, Callable]:
    def output_callback(content_block):
        if isinstance(content_block, dict) and content_block.get("type") == "text":
            message = content_block.get("text")
            print("Assistant:", message)
            if config.verbose:
                print(
                    f"[DEBUG] Content block: {json.dumps(content_block, indent=2)}")
            logger.add_message("assistant", content_block)

    def tool_output_callback(result: ToolResult, tool_use_id: str):
        output_data = {
            "tool_use_id": tool_use_id,
            "output": result.output,
            "error": result.error
        }

        if result.output:
            print(f"> Tool Output [{tool_use_id}]:", result.output)
        if result.error:
            print(f"!!! Tool Error [{tool_use_id}]:", result.error)
        if result.base64_image:
            # Add base64 image to logger
            logger.add_screenshot(tool_use_id, result.base64_image)
            output_data["has_screenshot"] = True

        if config.verbose:
            print(f"[DEBUG] Tool result: {json.dumps(output_data, indent=2)}")

        logger.add_message("tool", output_data)

    def api_response_callback(response: APIResponse[BetaMessage]):
        response_data = json.loads(response.text)
        if config.verbose:
            print(
                "\n---------------\nAPI Response:\n",
                json.dumps(response_data["content"], indent=4),
                "\n",
            )
        logger.add_message("api_response", response_data)

    return {
        "output_callback": output_callback,
        "tool_output_callback": tool_output_callback,
        "api_response_callback": api_response_callback,
    }
