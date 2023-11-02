from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

article_autor_table = db.Table(
    "article_autor_table",
    db.Column("article_id", db.ForeignKey("articles.id"), primary_key=True),
    db.Column("author_id", db.ForeignKey("authors.id"), primary_key=True),
)

article_category_table = db.Table(
    "article_category_table",
    db.Column("article_id", db.ForeignKey("articles.id"), primary_key=True),
    db.Column("category_id", db.ForeignKey("categories.id"), primary_key=True),
)

author_category_table = db.Table(
    "author_category_table",
    db.Column("author_id", db.ForeignKey("authors.id"), primary_key=True),
    db.Column("category_id", db.ForeignKey("categories.id"), primary_key=True),
)
class Article(db.Model):
    __tablename__ = "articles"
    __allow_unmapped__ = True
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    discription = db.Column(db.String(150))
    text = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    img = db.Column(db.String(150))
    authors = db.relationship("Author",
                              secondary=article_autor_table)
    categories = db.relationship("Category",
                                 secondary=article_category_table)

    def __str__(self):
        return self.title

class Author(db.Model):
    __tablename__ = "authors"
    __allow_unmapped__ = True
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(50))
    discription = db.Column(db.String(150))
    img = db.Column(db.String(150))
    articles = db.relationship("Article",
                               secondary=article_autor_table)
    categories = db.relationship("Category",
                                 secondary=author_category_table)

    def __str__(self):
        return self.author_name

class Category(db.Model):
    __tablename__ = "categories"
    __allow_unmapped__ = True
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50))
    img = db.Column(db.String(150))
    articles = db.relationship("Article",
                               secondary=article_category_table)
    authors = db.relationship("Author",
                              secondary=author_category_table)

    def __str__(self):
        return self.category_name

