import os
import binascii
import time
from functools import wraps

from flask import Blueprint
from flask import request
from flask import make_response
from game import game_manager as gm
from db.models import Game

api = Blueprint('api', __name__)
users = {}  # token : user_name
sessions = {}  # token: last_update
_expiration_time = 3600


def clean_sessions():
    if len(sessions) < 1000:
        return
    current = time.time()
    for k, v in sessions.items():
        if v < current - _expiration_time:
            del sessions[k]


def generate_token():
    return (binascii.hexlify(os.urandom(40)))


def get_user():
    return users.get(request.cookies.get("token"))


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get("token")
        user = users.get(token)
        if not user:
            return "No session"
        sessions[token] = time.time()
        return func(*args, **kwargs)

    return wrapper


@api.route("/game/requests")
@auth_required
def game_requests():
    return str([])


@api.route("/game/create/<move_time>")
@auth_required
def create_request(move_time):
    gm.create_game_request(get_user(), move_time)
    return "OK"


@api.route("/game/cencel")
@auth_required
def cencel_request():
    gm.cencel_game_request(get_user())
    return "OK"


@api.route("/game/apply/<user>")
@auth_required
def apply_game(user):
    return gm.apply_request(get_user(), user)


@api.route("/game/<id>")
@auth_required
def get_game(id):
    g = Game.query.get(id)
    return str(g)


@api.route("/start/<name>")
def start(name):
    clean_sessions()
    r = make_response(open('templates/index.html').read())
    if not request.cookies.get("token"):
        token = generate_token()
        r.headers['Set-Cookie'] = 'token=%s; path=/' % token
        users[token] = name
    else:
        users[request.cookies.get("token")] = name
    return r