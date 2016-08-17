from flask import Flask, render_template, request
from model import Pokemon, db, migrate
from flask_migrate import Migrate

app = Flask(__name__)
migrate = Migrate(app, db)

@app.route("/", methods=['GET'])
def index():
    pokelist = Pokemon.query.all()
    return render_template("index.html", title="Pokestraveganzamon", pokemon=pokelist)

@app.route("/new", methods=["POST"])
def add_new():
    pokemon = Pokemon(
        request.form.get("name", ""),
        request.form.get("type_1", ""),
        request.form.get("type_2", "")
    )
    db.session.add(pokemon)
    db.session.commit()
    return index()

@app.route("/pokemon/<int:pokemon_id>")
def view_pokemon(pokemon_id):
    return render_template("index.html", title="single pokemon", pokemon=Pokemon.query.get(pokemon_id))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
