from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('flaskr.config.Config')

    from flaskr.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
