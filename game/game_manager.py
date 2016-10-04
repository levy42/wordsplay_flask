import time
import game


class GameRequest(object):
    def __init__(self, user_id, username, move_time, language):
        self.user_id = user_id
        self.username = username
        self.move_time = move_time
        self.created_at = time.time()
        self.language = language


request_time_expiration = 120
game_requests = {}
move_time_cases = [120, 60, 45, 30, 15]
supported_languages = ['ua', 'en', 'ru']
games = {}


def create_game_request(user_id, username, move_time, language):
    game_request = GameRequest(user_id, username, move_time, language)
    game_requests[user_id] = game_request
    return game_request


def cencel_game_request(user):
    del game_requests[user]


def get_game_requests():
    return game_requests


def start_game(user1, user2):
    new_game = game.Words([user1, user2], 5, 'ua')
    return new_game


def move(id, index, char):
    pass


def surrender(id):
    pass


def apply_request(applier, user_id):
    game_request = game_requests[user_id]
    if not game_request:
        raise Exception('No such game request with user with id %s!' % user_id)
    start_game(game_requests[user_id].user_id, applier)
    del game_requests[user_id]


def game_configs():
    return move_time_cases, supported_languages
