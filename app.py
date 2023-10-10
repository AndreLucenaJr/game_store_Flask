from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes.game_routes import game_bp
from routes.user_routes import user_bp

app = Flask(__name__)

# Configurar a conexão do banco de dados

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/game_store"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar o SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.app_context().push  
db.init_app(app)
db.create_all()

app.register_blueprint(game_bp)
app.register_blueprint(user_bp)
      



if __name__ == '__main__':
    app.run(debug=True)
 