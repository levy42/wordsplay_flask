import json

from flask import Blueprint, session, g, jsonify
from game import game_manager as gm
from db.models import Game
from auth.auth import before_request as auth_context

api = Blueprint('api', __name__)


@api.before_request
def before_request():
    auth_context()


@api.route("/game/requests")
def game_requests():
    obj_list = []
    for x in gm.get_game_requests().values():
        dict = x.__dict__
        if x.user_id == g.user_id:
            dict['my'] = True
        obj_list.append(dict)

    return jsonify(obj_list)


@api.route("/game/create/<move_time>/<language>")
def create_request(move_time, language):
    r = gm.create_game_request(g.user_id, g.username, move_time, language)
    return jsonify(r.__dict__)


@api.route("/game/cencel")
def cencel_request():
    gm.cencel_game_request(g.user_id)
    return "OK"


@api.route("/game/apply/<user_id>")
def apply_game(user_id):
    return str(gm.apply_request(g.user_id, user_id))


@api.route("/game/<id>")
def get_game(id):
    g = Game.query.get(id)
    return str(g)


@api.route("/game/<id>/move/<index>/<char>")
def move(id, index, char):
    gm.move(id, index, char)


@api.route("/game/<id>")
def surrender(id):
    gm.surrender(id)


@api.route("/game/configs")
def game_configs():
    return jsonify(gm.game_configs())
