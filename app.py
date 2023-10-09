from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import yaml
from functools import wraps
from game_products import *
from flask_migrate import Migrate

app = Flask(__name__)

# Configurar a conexão do banco de dados
db_config = yaml.safe_load(open('db.yaml'))
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_config['mysql_user']}:{db_config['mysql_password']}@{db_config['mysql_host']}/{db_config['mysql_db']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar o SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
