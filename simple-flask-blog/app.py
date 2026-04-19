import os

from dotenv import load_dotenv
from flask import Flask, Response, flash, redirect, render_template, request, url_for
from flask_migrate import Migrate

from config.settings import db

load_dotenv()
from models import Post

app = Flask(__name__)


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{ROOT_PATH}/db/blog.db"
app.secret_key = os.getenv("APP_SECRET_KEY", "dev-test")
db.init_app(app)
Migrate(app, db)


@app.route("/")
@app.route("/posts")
def index() -> str:
    # posts = Post.query.order_by(Post.id.desc()).all()
    posts = Post.query.order_by(-Post.id).all()
    return render_template("posts/index.html.jinja", posts=posts)


@app.route("/posts/new")
def new_post() -> str:
    return render_template("posts/new.html.jinja")


@app.route("/posts/create", methods=["POST"])
def create() -> Response:
    title = request.form.get("title")
    content = request.form.get("content")

    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()

    # print(title, content)
    flash("新增文章成功！")
    return redirect(url_for("index"))


@app.route("/posts/<int:id>")
def show(id) -> Response:
    post = Post.query.get_or_404(id)
    # if post is None:
    #     abort(404)
    return render_template("posts/show.html.jinja", post=post)


@app.errorhandler(404)
def page_not_found(e) -> Response:
    return render_template("errors/404.html.jinja"), 404


@app.route("/posts/<int:id>/edit")
def edit(id) -> Response:
    post = Post.query.get_or_404(id)
    return render_template("posts/edit.html.jinja", post=post)


@app.route("/posts/<int:id>/update", methods=["POST"])
def update(id) -> Response:
    post = Post.query.get_or_404(id)

    post.title = request.form.get("title")
    post.content = request.form.get("content")

    db.session.add(post)  # 可省略
    db.session.commit()

    flash("更新文章成功！")
    return redirect(url_for("show", id=id))


@app.route("/posts/<int:id>/delete", methods=["POST"])
def delete(id) -> Response:
    post = Post.query.get_or_404(id)

    db.session.delete(post)
    db.session.commit()

    flash("刪除文章成功！")
    return redirect(url_for("index"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)
