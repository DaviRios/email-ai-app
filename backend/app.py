from flask import Flask, request, jsonify, render_template
from classify import classify_category, classify_productivity
from response_gen import generate_mock_response
from utils import extract_text
import os

app = Flask(__name__)

# GET -> carrega a página
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# POST -> processa o formulário e retorna JSON
@app.route('/analyze', methods=['POST'])
def analyze_email():
    file = request.files.get('file')
    email_text = request.form.get('email_text', '')

    text = extract_text(file, email_text)

    if not text.strip():
        return jsonify({"error": "Email vazio"}), 400

    category = classify_category(text)
    productivity = classify_productivity(category)
    response, _, _ = generate_mock_response(category)

    return jsonify({
        "email": text,
        "category": productivity.capitalize(),
        "response": response
    })

if __name__ == '__main__':
    app.run(debug=True)
