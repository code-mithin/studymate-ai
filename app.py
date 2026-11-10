"""Entry point. `flask run` / `python app.py` locally, `gunicorn app:app` on Render."""
from flask import Flask, jsonify, render_template
from config import Config
from database.db import close_db, init_db
from routes.api import bp as api_bp

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)
    app.teardown_appcontext(close_db)
    app.register_blueprint(api_bp)
    with app.app_context():
        init_db()

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/health")  # Render uses this to check the app is alive
    def health():
        return jsonify(status="ok")

    @app.errorhandler(404)
    def nf(_e):
        return jsonify(error="Not found."), 404

    @app.errorhandler(500)
    def err(_e):
        return jsonify(error="Server error. Please try again."), 500

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
