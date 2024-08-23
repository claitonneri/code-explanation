import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  organization=os.getenv('ORGANIZATION_ID'),
  project=os.getenv('PROJECT_ID'),
  api_key=os.getenv('OPENAI_API_KEY')
)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": "Você irá receber um código e gostaria de uma explicação detalhada sobre o funcionamento do código."},
      {"role": "user", "content": "freecodecamp = 'FREECODECAMP' print(f'{freecodecamp.lower()}')"}
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")