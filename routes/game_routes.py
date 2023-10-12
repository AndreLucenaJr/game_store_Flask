from flask import jsonify,request, Blueprint
from models.game import Game
from database import db

game_bp = Blueprint('game', __name__)


#List all the Products
@game_bp.route('/games', methods=['GET'])
def list_games():
    games = Game.query.all()
    games_json = [{"id": g.id, "name": g.name, "developer": g.developer, "price": g.price, "description" : g.description, "quantity" : g.quantity} for g in games]
    return jsonify(games_json)



#Create a game in database
@game_bp.route('/games/add/', methods=['POST'])
def add_game():
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        developer = data.get('developer')
        price = data.get('price')
        description = data.get('description')
        quantity = data.get('quantity')
    
    if name and price and description:
        new_game = Game(name=name, developer=developer, price=price, description=description, quantity=quantity)
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
        game_json = {"id": game.id, "name": game.name, "developer": game.developer, "price": game.price, "description" : game.description, "quantity": game.quantity}
        return jsonify(game_json)
    else:
        return jsonify({'message': 'Game not found'})
    



#Update a game by ID
@game_bp.route('/games/update/<int:game_id>/', methods=['PUT'])
def game_update(game_id):
    game = Game.query.get(game_id)
    if game:
        name = request.json.get('name', game.name)
        developer = request.json.get('developer', game.developer)
        price = request.json.get('price', game.price)
        description = request.json.get('description', game.description)
        quantity = request.json.get('quantity', game.quantity)

        game.name = name
        game.developer = developer
        game.price = price
        game.description = description
        game.quantity = quantity
        
        db.session.commit()
        return jsonify({'message': 'Game Updated'})
    else:
        return jsonify({'message': 'Game not found'})




#Delete a product by ID
@game_bp.route('/games/delete/<int:game_id>/', methods=['DELETE'])
def del_game(game_id):
    game = Game.query.get(game_id)
    if game:
        db.session.delete(game)
        db.session.commit()
        return jsonify({'message': 'Game deleted'})
    else:
        return jsonify({'message': 'Game not found'})
    
