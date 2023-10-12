from flask import jsonify,request, Blueprint
from models.game import Game
from database import db

game_bp = Blueprint('game', __name__)


#List all the Products
@game_bp.route('/games', methods=['GET'])
def list_games():
    games = Game.query.all()
    games_json = [{"id": g.id, "name": g.name, "price": g.price, "description" : g.description, "quantity" : g.quantity} for g in games]
    return jsonify(games_json)


#Create a game in database
@game_bp.route('/games/add/', methods=['POST'])
def add_game():
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')

    
    if name and price and description:
        new_game = Game(name=name, price=price, description=description)
        db.session.add(new_game)
        db.session.commit()
        return jsonify({'message': 'Successfully created game'})
    else:
        return jsonify({'message': 'Mandatory fields not filled in'})  


#List a game by ID
@game_bp.route('/games/<int:game_id>/', methods=['GET'])
def get_game(game_id):
    game = Game.query.get(game_id)
    if game:
        game_json = {"id": game.id, "name": game.name, "price": game.price, "description" : game.description}
        return jsonify(game_json)
    else:
        return jsonify({'message': 'Product not found'})
    


#Delete a product by ID
@game_bp.route('/games/delete/<int:game_id>/', methods=['DELETE'])
def del_game(game_id):
    game = Game.query.get(game_id)
    if game:
        db.session.delete(game)
        db.session.commit()
        return jsonify({'message': 'Product deleted'})
    else:
         return jsonify({'message': 'Product not found'})
    
