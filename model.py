from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CsrfProtect
from forms import SignupForm
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CsrfProtect(app)
bcrypt = Bcrypt(app)

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

class Trainer(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text(), unique=True)
    age = db.Column(db.Integer)
    password = db.Column(db.Text())

    def __init__(self, age, username, password):
        self.username = username
        # handle decoding - hash the password and call it a day!
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def authenticate(self, password):
        password = password.encode("utf-8")
        return bcrypt.check_password_hash(self.password, password)

if __name__ == "__main__":
    db.drop_all() # drop tables
    db.create_all() # create tables

    pikachu = Pokemon("Pikachu", "Electric", "Normal")
    bulbasaur = Pokemon("Bulbasaur", "Grass", "Poison")

    db.session.add(pikachu)
    db.session.add(bulbasaur)
    db.session.commit() # save to the DB
