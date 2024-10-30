import argparse
import os
from typing import Optional

from cupi.config import Config


def parse_args() -> tuple[str, Config]:
    parser = argparse.ArgumentParser(
        description="Claude Computer Use Demo with enhanced logging",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "Take a screenshot of the desktop"
  %(prog)s "Create a new folder named 'test'"
  %(prog)s "Open notepad and type 'Hello World'"
  
Common tasks:
  1. Screenshot: "Take a screenshot of [window/area/full screen]"
  2. File operations: "Create/Delete/Move [file/folder]"
  3. Text editing: "Open [editor] and write [content]"
  4. Web browsing: "Navigate to [website] and [action]"
  5. System operations: "Check [system info/status]"
        """,
    )

    parser.add_argument(
        "instruction",
        nargs="?",
        default="Save an image of the current window",
        help='Task instruction for Claude (default: "Save an image of the current window")',
    )

    parser.add_argument(
        "--model",
        "-m",
        type=str,
        default=Config.model,
        choices=["claude-3-5-sonnet-20241022", "claude-3-opus-20240229"],
        help=f"Model to use (default: {Config.model})",
    )

    parser.add_argument(
        "--log-dir",
        "-l",
        type=str,
        default=Config.log_dir,
        help=f"Directory to store logs (default: {Config.log_dir})",
    )

    parser.add_argument(
        "--max-tokens",
        "-mt",
        type=int,
        default=Config.max_tokens,
        help=f"Maximum tokens for response (default: {Config.max_tokens})",
    )

    parser.add_argument(
        "--recent-images",
        "-ri",
        type=int,
        default=Config.recent_images,
        help=f"Number of most recent images to keep (default: {Config.recent_images})",
    )

    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose output"
    )

    if not os.getenv("ANTHROPIC_API_KEY"):
        parser.error("ERROR: ANTHROPIC_API_KEY environment variable is not set")

    args = parser.parse_args()

    # Join multiple words if passed as separate arguments
    if isinstance(args.instruction, list):
        args.instruction = " ".join(args.instruction)

    config = Config(
        model=args.model,
        log_dir=args.log_dir,
        max_tokens=args.max_tokens,
        recent_images=args.recent_images,
        verbose=args.verbose,
    )

    return args.instruction, config
