from flask import Blueprint, render_template, redirect, url_for

default_blueprint = Blueprint('home', __name__)

@default_blueprint.route("/")
def redirect_to_home():
    return redirect(url_for('home.home_route'))

@default_blueprint.route("/home")
def home_route():
    return render_template('home.html')

@default_blueprint.route('/docs')
def docs_route():
    return render_template('docs/docs.html')

@default_blueprint.errorhandler(404)
def not_found(error):
    return render_template('404.html')