#!/usr/bin/env python3
"""Generate the AccessTwin welcome narration with the OpenAI Speech API.

Output:
    audio/1_welcome_intro.mp3

Setup:
    pip install --upgrade openai
    set OPENAI_API_KEY=your_key_here        # Windows CMD
    $env:OPENAI_API_KEY="your_key_here"     # PowerShell
    export OPENAI_API_KEY="your_key_here"   # macOS/Linux
    python generate_welcome_audio_openai.py
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from openai import OpenAI

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


SCRIPT = (
    "Dear viewers, please allow us six minutes to walk you through the system end to end. "
    "We will follow the hidden global pricing network, the product evidence, the Global Value Frontier, "
    "the payer War Room, and the final negotiation brief. "
    "Germany and TAK-279 are used as an illustrative example, but AccessTwin is not confined to one country, products, indications or launch decisions. "
    "Please note all numbers and facts mentioned are for the sake of ideation and do not represent real-life facts. "
    "From the next page, you can pause, resume, or replay at any time using the player at the bottom of the screen. "
    "From here on Sara will take over the walk through. She will guide you through the system and explain the key capabilities. "
    "Choose Guided to begin Sara's narration immediately, or choose Manual to explore freely and start the walkthrough "
    "for any section when you are ready."
)

INSTRUCTIONS = (
    "Speak as a warm, calm and confident senior product guide. Use clear international English, a polished executive tone, "
    "and a measured pace. Add a brief natural pause after each sentence. Emphasize that Germany and TAK-279 are illustrative "
    "examples only. Pronounce TAK-279 as T-A-K two seventy-nine. Do not sound promotional or theatrical."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate the AccessTwin welcome MP3 using OpenAI only.")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "audio" / "1_welcome_intro.mp3",
        help="Output MP3 path (default: audio/1_welcome_intro.mp3 beside this script).",
    )
    parser.add_argument(
        "--voice",
        default="cedar",
        choices=["alloy", "ash", "ballad", "coral", "echo", "fable", "nova", "onyx", "sage", "shimmer", "verse", "marin", "cedar"],
        help="OpenAI built-in TTS voice. Cedar is the default for a clear executive narration.",
    )
    parser.add_argument(
        "--model",
        default="gpt-4o-mini-tts",
        help="OpenAI speech model (default: gpt-4o-mini-tts).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY is not set.", file=sys.stderr)
        print("Set the key in your environment, then run this script again.", file=sys.stderr)
        return 2

    args.output.parent.mkdir(parents=True, exist_ok=True)
    client = OpenAI()

    try:
        with client.audio.speech.with_streaming_response.create(
            model=args.model,
            voice=args.voice,
            input=SCRIPT,
            instructions=INSTRUCTIONS,
            response_format="mp3",
        ) as response:
            response.stream_to_file(args.output)
    except Exception as exc:
        print(f"ERROR: OpenAI speech generation failed: {exc}", file=sys.stderr)
        return 1

    if not args.output.exists() or args.output.stat().st_size == 0:
        print("ERROR: The API call completed but no audio file was created.", file=sys.stderr)
        return 1

    print(f"Created: {args.output}")
    print(f"Size: {args.output.stat().st_size:,} bytes")
    print("The HTML is already configured to play this file on open or reload.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
