import time
import game


class GameRequest(object):
    def __init__(self, user, move_time):
        self.user = user
        self.move_time = move_time
        self.created_at = time.time()


request_time_expiration = 120
test_r = GameRequest("rgg", 60)
game_requests = {"rgg": test_r}
move_time_cases = [120, 60, 45, 30, 15]
games = {}


def create_game_request(user, move_time):
    game_request = GameRequest(user, move_time)
    game_requests[user] = game_request
    return game_request


def cencel_game_request(user):
    del game_requests[user]


def get_game_requests():
    return game_requests


def start_game(user1, user2):
    new_game = game.Words([user1, user2], 5, 'ua')
    return new_game


def move():
    pass


def apply_request(applier, user):
    game_request = game_requests[user]
    if not game_request:
        raise Exception('No such game request with user with id %s!' % user)
    start_game(game_requests[user].user, applier)
    del game_requests[game_requests]
