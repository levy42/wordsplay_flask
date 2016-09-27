from flask import Flask
from flask import send_from_directory
from flask import render_template
from api import api
from db import models
app = Flask(__name__)
app.config.from_pyfile('conf.cfg')
db = models.db
db.init_app(app)
app.register_blueprint(api.api)


@app.route('/start')
def start():
    return render_template('start.html')


@app.route('/')
@app.route('/ring')
@app.route('/game')
def home():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(port=10000)
