from flask import Flask
from flask import send_from_directory
from api import api
from db import models

app = Flask(__name__)
app.config.from_pyfile('conf.cfg')
db = models.db
db.init_app(app)
app.register_blueprint(api.api)


@app.route('/')
def hello_world():
    return app.send_static_file('start.html')


if __name__ == '__main__':
    app.run(port=10000)
