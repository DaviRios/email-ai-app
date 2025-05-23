Email Classifier AI
Uma aplicação web para automatizar a classificação de emails e geração de respostas automáticas utilizando inteligência artificial. Desenvolvido como solução para empresas que lidam com grande volume de mensagens diárias, reduzindo trabalho manual e otimizando o tempo da equipe.

Visão Geral
O sistema permite que o usuário envie um email (via upload de arquivo .txt ou .pdf ou inserção direta de texto) e retorna:

A classificação do email em Produtivo ou Improdutivo

Uma resposta automática sugerida, gerada com base no conteúdo

Funcionalidades
Interface web com formulário para upload de emails ou entrada manual

Classificação automática do conteúdo com base em NLP

Geração de resposta utilizando modelos de linguagem

Suporte a arquivos .txt e .pdf

Tecnologias Utilizadas
Python 3.10+

Flask

OpenAI GPT (para geração de resposta)

Hugging Face Transformers (para classificação zero-shot)

PyMuPDF (leitura de PDFs)

HTML e CSS (frontend básico)

Estrutura do Projeto
bash
Copiar
Editar
email-classifier/
│
├── backend/
│   ├── app.py               # API Flask
│   ├── ai_utils.py          # Lógica de IA
│   └── templates/
│       └── index.html       # Interface HTML
│
├── .gitignore
├── requirements.txt
├── .env.example
└── README.md
Como Executar Localmente
Requisitos
Python instalado

Chave de API da OpenAI (ou Hugging Face, se aplicável)

Passos
bash
Copiar
Editar
# Clonar o repositório
git clone https://github.com/seu-usuario/email-classifier.git
cd email-classifier

# Criar ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # macOS/Linux

# Instalar dependências
pip install -r requirements.txt

# Criar arquivo .env com as credenciais
cp .env.example .env
# Edite o arquivo .env com sua chave da API

# Executar aplicação
python backend/app.py
Acesse em http://localhost:5000

Instruções Adicionais
Arquivos .env, venv/ e outros temporários estão devidamente ignorados via .gitignore.

A aplicação pode ser facilmente adaptada para deploy em serviços como Vercel, Render ou Heroku.

Todos os scripts estão organizados para facilitar manutenção e extensão futura.