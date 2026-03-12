import os
from sarvamai import SarvamAI

# API KEY
os.environ["SARVAMAI_API_KEY"] = "YOUR_API_KEY_HERE"

client = SarvamAI(api_subscription_key=os.environ["SARVAMAI_API_KEY"])

# Bot personality
SYSTEM_PROMPT = """
You are a helpful assistant.
Keep all responses under 3 sentences.
You are speaking out loud, not writing.
Be conversational, warm and natural.
"""

EXIT_PHRASES = ["exit", "quit", "stop", "bye"]

conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]
