
import os
from typing import Optional

def get_openai_api_key() -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise EnvironmentError("Please set the OPENAI_API_KEY environment variable.")
    return key

def get_anthropic_api_key() -> Optional[str]:
    return os.getenv("ANTHROPIC_API_KEY")

def get_gemini_api_key() -> Optional[str]:
    return os.getenv("GEMINI_API_KEY")
