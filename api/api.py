from flask import Blueprint
from flask_login import login_required
from game import game_manager as gm
import flask_user.passwords
api = Blueprint('api', __name__)



def login()
@api.route("/game/requests")
@login_required
def game_requests():
    return gm.get_game_requests()


@api.route("/game/create/<move_time>")
@login_required
def create_request(move_time):
    return gm.create_game_request()


@api.route("/game/apply/<user>")
def game(user):
    return gm.apply_request(None, user)
