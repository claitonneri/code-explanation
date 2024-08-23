import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  organization=os.getenv('ORGANIZATION_ID'),
  project=os.getenv('PROJECT_ID'),
  api_key=os.getenv('OPENAI_API_KEY')
)

print(client.models.list())