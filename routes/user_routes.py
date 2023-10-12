from flask import jsonify,request, Blueprint
from models.user import User
from flask_bcrypt import Bcrypt
from database import db

bcrypt = Bcrypt()
user_bp = Blueprint('user', __name__)

# Register a user
@user_bp.route('/user/register', methods=['POST'])
def register_user():
    if request.method == 'POST':
        data = request.json
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        money = data.get('money')
        is_admin = data.get('is_admin', 0)

    if username and password and email:

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password, email=email, money=money, is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registration successful'})
    else:
        return jsonify({'message': 'Mandatory fields not filled in'})




# Login a user
@user_bp.route('/user/login', methods=['POST'])
def login_user():
    if request.method == 'POST':
        data = request.json
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

    if username and password and email:
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user()
            return jsonify({'message': 'Login well done'})
        else:
            return jsonify({'message': 'Invalids username or password'})
    else:
        return jsonify({'message': 'Mandatory fields not filled in'})
    



#Get the user by ID
@user_bp.route('/user/<int:user_id>/', methods=['GET'])
def find_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        user_json =  {"id": user.id, "name": user.username, "email": user.email, "money": user.money}
        return jsonify(user_json)
    else:
        return jsonify({'message': 'User not found'})




#delete a user
@user_bp.route('/user/delete/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted'})
    else:
        return jsonify({'message': 'User not found'})
