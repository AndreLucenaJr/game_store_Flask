from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import yaml
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from functools import wraps

app = Flask(__name__)

# Config db
db = yaml.safe_load(open('db.yaml'))
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db['mysql_user']}:{db['mysql_password']}@{db['mysql_host']}/{db['mysql_db']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

