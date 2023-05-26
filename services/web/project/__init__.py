from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, name):
        self.name = name


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/user/add', methods=['POST'])
def add_user():
    name = request.form['name']
    new_user = User(name)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('index'))
