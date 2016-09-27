import os
import binascii
import time
from functools import wraps
import json

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
    obj_list = []
    user = get_user()
    for x in gm.get_game_requests().values():
        dict = x.__dict__
        if x.user == user:
            dict['my'] = True
        obj_list.append(dict)

    return json.dumps(obj_list)


@api.route("/game/create/<move_time>/<language>")
@auth_required
def create_request(move_time, language):
    r = gm.create_game_request(get_user(), move_time, language)
    return json.dumps(r.__dict__)


@api.route("/game/cencel")
@auth_required
def cencel_request():
    gm.cencel_game_request(get_user())
    return "OK"


@api.route("/game/apply/<user>")
@auth_required
def apply_game(user):
    return str(gm.apply_request(get_user(), user))


@api.route("/game/<id>")
@auth_required
def get_game(id):
    g = Game.query.get(id)
    return str(g)


@api.route("/game/<id>/move/<index>/<char>")
@auth_required
def move(id, index, char):
    gm.move(id, index, char)


@api.route("/game/<id>")
def surrender(id):
    gm.surrender(id)


@api.route("/start/<name>")
def start(name):
    clean_sessions()
    if name in users.values():
        return "Name is used", 201
    r = make_response(open('templates/index.html').read())
    if not request.cookies.get("token"):
        token = generate_token()
        r.headers['Set-Cookie'] = 'token=%s; path=/' % token
        r.headers['User'] = name
        users[token] = name
    else:
        users[request.cookies.get("token")] = name
    return r


@api.route("/quit")
@auth_required
def quit():
    del users[request.cookies.get("token")]
    r = make_response(open('templates/start.html').read())
    return r


@api.route("/game/configs")
def game_configs():
    return json.dumps(gm.game_configs())
