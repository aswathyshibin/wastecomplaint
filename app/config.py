import os

# Securely get from environment variables (important for public repo and Vercel)
# Default values for local testing (User should replace these in Vercel/Environment)
API_KEY = os.getenv("API_KEY", "YOUR_GROQ_API_KEY")

API_URL = os.getenv("API_URL", "https://api.groq.com/openai/v1/chat/completions")

MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")