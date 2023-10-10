from app import db

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column("user_id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    money = db.Column(db.Float)
    email = db.Comlumn(db.String(100))
    is_admin = db.Column(db.Boolean, default = False)

    def __init__(self, name):
        self.name = name
        self.money = 0

  
    def add_money(self, quantity):
        self.money += quantity

    def discount_money(self, quantity):
        self.money -= quantity

    def set_name(self, name):
        self.name = name

    def get_money(self):
        return self.money
