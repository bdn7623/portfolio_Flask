from flask import Flask, render_template, redirect, url_for

from flask_sqlalchemy import SQLAlchemy #project_4
from flask_admin import Admin #project_4,5
from flask_admin.contrib.sqla import ModelView #project_4,5

from project_1_files import project_1_files
from project_2_articles import project_2_articles

from models import db #project_5
from models import Article, Author, Category #project_5
from flask_admin.form.upload import ImageUploadField #project_5
from auth_part import auth_module,login_manager,User #project_5
from flask_login import current_user #project_5

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project_51.db" #project_5
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.secret_key = "secret_key"

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(project_1_files)
app.register_blueprint(project_2_articles)
app.register_blueprint(auth_module) #project_5
login_manager.init_app(app) #project_5

db = SQLAlchemy()

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
            Project('Project 5: Flask-Admin, Login, Declaring Models', 'This project uses Declaring Models (Many-to-Many Relationships) and Flask-Login','/project_5')]

class ImageView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('/login'))

    form_extra_fields = {
        'img': ImageUploadField(base_path='static')
    }

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

@app.route("/project_5")
def get_project_5():
    return render_template('/project_5.html')

@app.route("/project_5_home")
def get_categories():
    categories = Category.query.all()
    return render_template('project_5_categories.html', categories=categories)

@app.route("/categories/<int:category_id>")
def get_category(category_id):
    category = Category.query.filter(Category.id==category_id).first()
    return render_template('project_5_category.html', category=category)

@app.route("/articles/<int:article_id>")
def get_article(article_id):
    article = Article.query.filter(Article.id==article_id).first()
    return render_template('project_5_article.html', article=article)

admin = Admin(app, name='Project_5', template_mode='bootstrap3')

admin.add_view(ImageView(Article, db.session))
admin.add_view(ImageView(Author, db.session))
admin.add_view(ImageView(Category, db.session))
admin.add_view(ImageView(User, db.session))

app.run()