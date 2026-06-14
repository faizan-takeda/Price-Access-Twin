#!/usr/bin/env python3
"""Generate only the AccessTwin welcome-gate narration.

The generated file must sit at:
    audio/welcome_intro.mp3

Run:
    pip install --upgrade openai python-dotenv
    python generate_welcome_audio.py
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = "gpt-4o-mini-tts"
VOICE = "sage"
OUT = Path(__file__).resolve().parent / "audio" / "welcome_intro.mp3"

TEXT = (
    "Dear visitor, please allow me about five minutes to walk you through the whole "
    "system end to end. You will see the hidden pricing network, the asset evidence, "
    "the Global Value Frontier, the payer War Room and the final negotiation brief. "
    "You can pause, resume, or play me anytime from the bottom left panel. Guided "
    "option starts narration immediately. In manual mode, every section retains its "
    "own Start walkthrough control."
)

DELIVERY = (
    "Speak as a calm, intelligent AI host welcoming senior pharmaceutical leaders. "
    "Warm, polished and confident. Use a measured executive pace with subtle energy. "
    "Pause naturally after the first sentence and around the main capability names. "
    "Do not sound theatrical or salesy."
)


def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is missing.")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    client = OpenAI(api_key=api_key)

    with client.audio.speech.with_streaming_response.create(
        model=MODEL,
        voice=VOICE,
        input=TEXT,
        instructions=DELIVERY,
        response_format="mp3",
    ) as response:
        response.stream_to_file(OUT)

    print(f"Created: {OUT}")


if __name__ == "__main__":
    main()
