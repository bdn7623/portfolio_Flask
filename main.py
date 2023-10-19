from flask import Flask, render_template

from project_1_files import project_1_files
from project_2_articles import project_2_articles
from project_4_sqlalchemy import project_4_sqlalchemy

app = Flask(__name__)
app.register_blueprint(project_1_files)
app.register_blueprint(project_2_articles)
app.register_blueprint(project_4_sqlalchemy)

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
            Project('Project 4: Flask + SQLAlchemy, Flask-Admin', 'This project demonstrates connecting a database and admin panel','/project_4_sqlalchemy')]

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

app.run()