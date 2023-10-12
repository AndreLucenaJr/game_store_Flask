from flask import Flask
from database import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/game_store"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)



if __name__ == '__main__':
  
    from routes.game_routes import game_bp
    from routes.user_routes import user_bp

  
    app.app_context().push()

    app.register_blueprint(game_bp)
    app.register_blueprint(user_bp)

    db.create_all()
    app.run(debug=True)
