from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # Cria a aplicação Flask

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///empreguei.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Evita warnings

# Inicializa o banco de dados com a aplicação
db = SQLAlchemy(app)

# Rota da página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True)
