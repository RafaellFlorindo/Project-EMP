from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # Criar a aplicação Flask

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///empreguei.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Para evitar warnings

db = SQLAlchemy(app)  # Inicializa o banco de dados

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
