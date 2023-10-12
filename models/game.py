from database import db

class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column("game_id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    developer =  db.Column(db.String(100))
    description = db.Column(db.String(100))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __init__(self, name, developer, description, price, quantity):
        self.name = name
        self.developer = developer
        self.description = description
        self.price= price
        self.quantity = quantity
    
    def get_name(self):
        return self.name
    
    def get_developer(self):
        return self.developer
    
    def get_description(self):
        return self.description
    
    def get_price(self):
        return self.price
    
    def get_quantity(self):
        return self.quantity
    
    def set_name(self, name):
        self.name = name
    
    def set_developer(self,developer):
        self.developer = developer
    
    def set_description(self, description):
        self.description = description
    
    def set_price(self, price):
        self.price = price

    def set_quantity(self, quantity):
        self.quantity = quantity
    



