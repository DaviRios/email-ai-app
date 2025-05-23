from flask import Flask, render_template, request
from classify import classify_category, classify_productivity
from response_gen import generate_mock_response, generate_response
from utils import extract_text
import os
app = Flask(__name__)

print("Template path exists?", os.path.exists("templates/index.html"))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        email_text = request.form.get('email_text', '')

        text = extract_text(file, email_text)

        if not text.strip():
            return render_template('index.html', email="", category="Erro: Email vazio", response="")

        category = classify_category(text)
        productivity = classify_productivity(category)
        response, _, _ = generate_mock_response(category)

        return render_template('index.html', email=text, category=productivity.capitalize(), response=response)


    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)