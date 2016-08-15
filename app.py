from flask import Flask, render_template, request
from pokemon import Pokemon

pokelist = [Pokemon("pikachu"), Pokemon("bulbasaur")]

app = Flask(__name__)

@app.route("/sayHi", methods=['GET'])
def index():
    return render_template("index.html", title="Hello World", pokemon=pokelist)

@app.route("/new", methods=["POST"])
def add_new():
    pokelist.append(Pokemon(request.form["pokemon"]))
    return index()

@app.route("/pokemon/<int:pokemon_id>")
def view_pokemon(pokemon_id):
    return render_template("index.html", title="single pokemon", pokemon=[pokelist[pokemon_id]])


if __name__ == "__main__":
    app.run(debug=True)
