from flask import Flask, render_template, request, redirect, url_for, flash, session
from model import Pokemon, Trainer, db, migrate
from flask_migrate import Migrate
from forms import SignupForm, LoginForm
from flask_wtf.csrf import CsrfProtect
from flask_login import LoginManager, login_required, login_user, current_user
import config

app = Flask(__name__)
app.config.from_object(config)
migrate = Migrate(app, db)

# Stuff to make login easier
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "serve_signup"

@login_manager.user_loader
def load_user(user_id):
    return Trainer.query.get(user_id)

# End login stuff

## Homepage
@app.route("/", methods=['GET'])
def index():
    user = load_user(session.get("user_id"))
    pokelist = Pokemon.query.all()
    return render_template("index.html", title="Pokestraveganzamon", pokemon=pokelist, user=user)

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

## User Stuff
# Login, Signup routes
@app.route("/trainer/login", methods=["GET"])
def serve_signup():
    return render_template("signup.html", signup=SignupForm(), login=LoginForm())

@app.route("/trainer/login", methods=["POST"])
def handle_login():
    form = LoginForm(request.form)
    if not form.validate():
        flash("Incorrect username or password")
        return serve_signup()

    username = form.username.data
    password = form.password.data

    user = Trainer.query.filter_by(username=username).first()

    if not user or not user.authenticate(password):
        flash("Incorrect username or password")
        return serve_signup()

    login_user(user)
    return redirect(request.args.get("next", url_for("index")))


@app.route("/trainer/signup", methods=["POST"])
def handle_signup():
    error = None
    form = SignupForm(request.form)
    if form.validate_on_submit(): # if the form is valid
        flash("trainer {} created!".format(form.username.data))
        new_trainer = Trainer(form.age.data, form.username.data, form.password.data)
        db.session.add(new_trainer)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', form=form, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
