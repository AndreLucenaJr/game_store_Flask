from flask import jsonify,request, Blueprint
from models.user import User
from flask_bcrypt import Bcrypt
from app import db

user_bp = Blueprint('user', __name__)

# Register a user
@app.route('/register', methods=['POST'])
def register_user():
    if request.method == 'POST':
        data = request.json
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        is_admin = data.get('is_admin', 0)

    if username and password and email:

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password, email=email, is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registration successful'})
    else:
        return jsonify({'message': 'Mandatory fields not filled in'})