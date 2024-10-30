import asyncio
import os
from typing import Optional

from anthropic.types.beta import BetaMessageParam

from cupi.callbacks import create_callbacks
from cupi.cli import parse_args
from cupi.computer_use_demo.loop import APIProvider, sampling_loop
from cupi.config import Config
from cupi.logger import ConversationLogger


async def run_claude(instruction: str, config: Config) -> None:
    # Initialize conversation logger
    logger = ConversationLogger(output_dir=config.log_dir)
    logger.set_metadata({"args": {"instruction": instruction, **vars(config)}})

    provider = APIProvider.ANTHROPIC
    api_key = os.getenv("ANTHROPIC_API_KEY")

    print(
        f"""
        Starting Claude Computer Use Demo
        ===============================
        Instruction: {instruction}
        Model: {config.model}
        Log Directory: {config.log_dir}
        Press Ctrl+C to stop
        ===============================
    """
    )

    # Set up the initial messages
    messages: list[BetaMessageParam] = [
        {
            "role": "user",
            "content": instruction,
        }
    ]

    # Log initial user message
    logger.add_message("user", instruction)

    # Create callbacks
    callbacks = create_callbacks(logger, config)

    try:
        # Run the sampling loop
        messages = await sampling_loop(
            model=config.model,
            provider=provider,
            system_prompt_suffix="",
            messages=messages,
            output_callback=callbacks["output_callback"],
            tool_output_callback=callbacks["tool_output_callback"],
            api_response_callback=callbacks["api_response_callback"],
            api_key=api_key,
            only_n_most_recent_images=config.recent_images,
            max_tokens=config.max_tokens,
        )
    except KeyboardInterrupt:
        print("\nGracefully shutting down...")
    except Exception as e:
        print(f"\nError during execution: {str(e)}")
        if config.verbose:
            import traceback

            print("\nFull traceback:")
            traceback.print_exc()
    finally:
        # Save the conversation log
        log_file = logger.save()
        print(f"\nConversation log saved to: {log_file}")


def main() -> None:
    instruction, config = parse_args()
    try:
        asyncio.run(run_claude(instruction, config))
    except Exception as e:
        print(f"Critical error:\n{e}")


if __name__ == "__main__":
    main()
