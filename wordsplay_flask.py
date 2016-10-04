from flask import Flask
from flask import render_template
from api import api
from auth import auth
from db import models
from auth import auth

app = Flask(__name__)
app.config.from_pyfile('conf.cfg')
db = models.db
db.init_app(app)
auth_bp = auth.auth
auth.init_app(app)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(api.api)
app.register_blueprint(auth.auth)


@app.route('/')
@app.route('/ring')
@app.route('/game')
@app.route('/login', methods=['GET'])
@app.route('/register', methods=['GET'])
def home():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(port=10000)
