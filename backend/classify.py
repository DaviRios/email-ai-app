from transformers import pipeline
import json
import os

classifier = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-1")

mocks_path = os.path.join(os.path.dirname(__file__), 'mocks.json')
with open(mocks_path, 'r', encoding='utf-8') as f:
    mocks = json.load(f)

def classify_category(text):
    labels = list(mocks.keys())
    result = classifier(text, labels)
    best_match = result['labels'][0]
    return best_match

def classify_productivity(category):
    category_data = mocks.get(category.lower(), mocks["default"])
    return category_data["productivity"]

