import os
from dotenv import load_dotenv

# Load environment variables from .env file (create this with your API key)
load_dotenv()

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')