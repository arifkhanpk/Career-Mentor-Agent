from dataclasses import dataclass
from openai import OpenAI
import os

@dataclass
class CareerOption:
    name: str
    description: str
    growth: str
    salary: str

class BaseAgent:
    def __init__(self):
        self.client = OpenAI(
            base_url=os.getenv("OPENROUTER_BASE_URL"),
            api_key=os.getenv("OPENROUTER_API_KEY")
        )
        self.headers = {
            "HTTP-Referer": "https://career-mentor-agent.com",
            "X-Title": "Career Mentor Agent"
        }
        # Correct OpenRouter model names
        self.models = {
            "default": "anthropic/claude-3-haiku",  # Free and reliable model
            "gpt": "openai/gpt-3.5-turbo-0125",  # Correct GPT-3.5 model name
            "claude": "anthropic/claude-3-sonnet"  # More powerful Claude model
        }