from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id

@app.route('/')
def index():
    return render_template("main_page.html")


@app.route('/posts')
def posts():
    articles = Article.query.all()
    return render_template("posts.html", articles=articles)


@app.route('/posts/<id>/delete')
def post_delete(id):
    articles = Article.query.get_or_404(id)
    try:
        db.session.delete(articles)
        db.session.commit()
        return redirect('/posts')
    except:
        return "При удалении пользователя произошла ошибка"


@app.route('/posts/<id>/update', methods=['POST', 'GET'])
def post_update(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.text = request.form['text']
        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return "При редактировании данных о пользователе произошла ошибка"
    else:
        return render_template("post_update.html", article=article)


@app.route('/create_article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        title = request.form['title']
        text = request.form['text']
        article = Article(title=title, text=text)
        try:
            db.session.add(artidododp)
            db.session.commit()
            return redirect('/posts')
        except NameError:
            return "При добавлении пользователя произошла ошибка"
    else:
        return render_template("create_article.html")


if __name__ == "__main__":
    app.run(debug = True)
