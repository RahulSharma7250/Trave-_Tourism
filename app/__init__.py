from flask import Flask
from flask_pymongo import PyMongo

mongo = None

def create_app():
    global mongo
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize MongoDB
    mongo = PyMongo(app)

    # Register Blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.booking_routes import booking_bp
    from app.routes.destination_routes import destination_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(booking_bp, url_prefix='/bookings')
    app.register_blueprint(destination_bp, url_prefix='/destinations')

    return app
