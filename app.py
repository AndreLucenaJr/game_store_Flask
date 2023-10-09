from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import yaml
from functools import wraps

app = Flask(__name__)

# Configurar a conexão do banco de dados
db_config = yaml.safe_load(open('db.yaml'))
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_config['mysql_user']}:{db_config['mysql_password']}@{db_config['mysql_host']}/{db_config['mysql_db']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar o SQLAlchemy
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
