#Flask & SQLAlchemy
#Admin
from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import Blueprint, render_template

project_4_sqlalchemy = Blueprint("project_4_sqlalchemy",
                            __name__,
                            template_folder="templates")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.secret_key = "!!!!!!!"

db = SQLAlchemy()

class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    text = db.Column(db.Text)
    author = db.Column(db.String(100))
    date = db.Column(db.Date)

db.init_app(app)

with app.app_context():
    db.create_all()

admin = Admin(app, name='project_4', template_mode='bootstrap3')
admin.add_view(ModelView(Article, db.session))

@project_4_sqlalchemy.route("/project_4_sqlalchemy")
def get_admin():
    return render_template("project_4_sqlalchemy.html")


#app.run()