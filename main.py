from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy #project_4
from flask_admin import Admin #project_4
from flask_admin.contrib.sqla import ModelView #project_4

from project_1_files import project_1_files
from project_2_articles import project_2_articles
#from project_4_sqlalchemy import project_4_sqlalchemy

app = Flask(__name__)
app.register_blueprint(project_1_files)
app.register_blueprint(project_2_articles)
#app.register_blueprint(project_4_sqlalchemy)

#project_4:
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.secret_key = "!!!!!!!"

db = SQLAlchemy()
#project_4 end

class Project:
    def __init__(self,
                 title,
                 description,
                 link):
        self.title = title
        self.description = description
        self.link = link

projects = [Project('Project 1: files hosting','This project allows you to download a file with a project archive','/project_1_files'),
            Project('Project 2: Articles','This project implements CRUD using Articles as an example, without CSS','/project_2_articles'),
            Project('Project 3: Bootstrap/layout','This project is an implementation of this page','/'),
            Project('Project 4: Flask + SQLAlchemy, Flask-Admin', 'This project demonstrates connecting a database and admin panel','/project_4_sqlalchemy'),
            Project('Project 5: Flask-Admin, Login, Declaring Models', 'This project uses Declaring Models (Many-to-Many Relationships) and Flask-Login','/project_4_sqlalchemy')]

#project_4:
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
#project_4 end

@app.route("/")
def index():
    return render_template('index.html', projects=projects)

@app.route("/project_1_files")
def get_project_1():
    return render_template('/project_1_files.html')

@app.route("/project_2_articles")
def get_project_2():
    return render_template('/project_2_articles.html')

@app.route("/project_4_sqlalchemy")
def get_project_4():
    return render_template('/project_4_sqlalchemy.html')

@app.route("/project_5_admin")
def get_project_5():
    return render_template('/project_5.html')

app.run()