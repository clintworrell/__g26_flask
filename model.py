from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/pokemon'
db = SQLAlchemy(app)

class Pokemon(db.Model):

    __tablename__ = 'pokemon'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    type_1 = db.Column(db.Text())
    type_2 = db.Column(db.Text())

    def __init__(self, name, type_1, type_2):
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2

    # This is what will be displayed when you examine an instance
    def __repr__(self):
        return 'Name: {} - Type1 {}, Type2 {}'.format(self.name, self.type_1, self.type_2)

    def greeting(self):
        return self.name + "!"



if __name__ == "__main__":
    db.drop_all() # drop tables
    db.create_all() # create tables

    pikachu = Pokemon("Pikachu", "Electric", "Normal")
    bulbasaur = Pokemon("Bulbasaur", "Grass", "Poison")

    db.session.add(pikachu)
    db.session.add(bulbasaur)
    db.session.commit() # save to the DB
