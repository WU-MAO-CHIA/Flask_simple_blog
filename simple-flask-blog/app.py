
from flask_migrate import Migrate

from apps import app
from apps.error.handlers import error_bp
from apps.post.views import index as root_view
from apps.post.views import post_bp
from apps.user.views import user_bp
from config.settings import db

app.add_url_rule("/", view_func=root_view, endpoint="root")
app.register_blueprint(post_bp, url_prefix="/posts")
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(error_bp)

db.init_app(app)
Migrate(app, db)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
