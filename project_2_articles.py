# CRUD for articles
# dinamic pages
from flask import Blueprint, render_template, redirect, request

project_2_articles = Blueprint("project_2_articles",
                            __name__,
                            template_folder="templates")

class Article:
    def __init__(self,
                 title,
                 description,
                 text):
        self.title = title
        self.description = description
        self.text = text

articles = [Article("title1","description1","text1"),
            Article("title2","description2","text2"),
            Article("title3","description3","text3"),
            Article("title4","description4","text4"),
            Article("title5","description5","text5")]

@project_2_articles.route("/project_2_articles")
def list_articles():
    return render_template("project_2_articles.html",articles=enumerate(articles))

@project_2_articles.route("/project_2_articles/<int:article_id>")
def get_article(article_id):
    return render_template("project_2_article.html",article=articles[article_id])

@project_2_articles.route("/project_2_articles/delete/<int:article_id>")
def delete_article(article_id):
    articles.pop(article_id)
    return redirect("/project_2_articles")

@project_2_articles.route("/project_2_articles/add",methods=["GET","POST"])
def add_article():
    if request.method == "POST": #data from form
        article_data = request.form
        article = Article(article_data.get("title"),
                          article_data.get("description"),
                          article_data.get("text"))
        articles.append(article)
        return redirect("/project_2_articles")
    return render_template("project_2_add_article.html")
