from flask import Flask, render_template
from .config import db, DevelopmentConfig
from .controllers import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    
    db.init_app(app)
    with app.app_context():
        db.create_all()

    register_blueprints(app)
    
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    return app
