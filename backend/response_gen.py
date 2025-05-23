import os
from openai import OpenAI
from dotenv import load_dotenv
import json
import random

load_dotenv()  # Carrega variáveis do .env

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

client = OpenAI(api_key=api_key)


mocks_path = os.path.join(os.path.dirname(__file__), 'mocks.json')
with open(mocks_path, 'r', encoding='utf-8') as f:
    mocks = json.load(f)

def generate_mock_response(category):
    category_data = mocks.get(category.lower(), mocks["default"])
    response = category_data["responses"][0]  
    correct_cat = category_data["correct_category"]
    productivity = category_data["productivity"]
    return response, correct_cat, productivity

def generate_response(text, category):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"{category}: {text}"}],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        if "insufficient_quota" in str(e) or "429" in str(e):
            return generate_mock_response(category)
        else:
            raise