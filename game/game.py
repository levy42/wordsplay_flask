# -*- coding: utf-8 -*-
import os
import random


ALPHABET = 'game/alphabet/%s'


class Words(object):
    def __init__(self, players, n, language, word=None):
        # check if n is odd, game rules requires that
        if not n & 1:
            raise Exception('Not valid board size, it must be odd!')
        # check if initial word has the same lenght as board, it must cover it
        if word and len(word) != n:
            raise Exception('Not valid word lenght')
        if not word:
            word = generate_start_word(n)
        self.players = players
        self.board = [[0 for i in range(n)] for j in range(n)]
        # put initial word to the board
        self.board[n/2] = [i for i in word]
        # shuffle player to change their move order
        random.shuffle(players)
        self.words = {player: [] for player in players}
        self.start_word = word
        self.words_hist = [(word, 0)]
        self.current_pl = 0
        self.language = language
        self.cells_left = n * n - n
        self.moves = 0
        with open(ALPHABET % language) as data:
            self.alphabet = data.readlines()

    def move(self, player, coord, letter):
        if player != self.players[self.current_pl]:
            raise Exception('Not this player move turn!')
        _letter = letter.upper()
        if _letter not in self.alphabet:
            raise Exception('Invalid letter! Not present in allowed list')
        # check if cell is empty (value==0)
        if not self.board[coord[0]][coord[1]]:
            raise Exception('cell is not empty!')
        self.board[coord[0]][coord[1]] = _letter
        self.cells_left -= 1
        self.moves += 1
        new_words = self._calc_move(coord)
        self.words[player].extends([word.word for word in new_words])
        self.words_hist.extend([(word.word, player) for word in new_words])
        self.current_pl = self.current_pl if self.current_pl + 1 < len(self.players) else 0
        return new_words

    def status(self):
        if self.moves == 0:
            return 'start'
        if self.cells_left == 0:
            return 'finish'
        return 'play'

    def game_result(self):
        return self._who_win()

    def _who_win(self):
        results = [[player, ] for player in self.players]
        for result in results:
            for w in self.words[result[0]]:
                result[1] += w
        return sorted(results, key=lambda res: res[1])

    # TODO: method must return Word (class) list that appeared on a board after adding letter
    def _calc_move(self, coord):
        return []


class Word(object):
    def __init__(self, path, word):
        self.word = word
        self.path = path


def generate_start_word(n):
    return 'ПОХЕР'
