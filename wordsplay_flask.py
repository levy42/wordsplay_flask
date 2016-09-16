from flask import Flask
from api import api
from flask_login
app = Flask(__name__)

app.config.from_pyfile('conf.conf')


@app.route('/')
def hello_world():
    return 'Hello World!'


app.register_blueprint(api.api)

if __name__ == '__main__':
    app.run(port=10000)
