#!/usr/bin/python3

from common.entities import Game
from random import randint


class GamesStorage(obj):
    def __init__(self, games: List[Game]) -> None:
        self._games = games

    def get_random_games() -> List[Game]:
        games_list = []

        for i in range(10):
            games_list.append(Game(randint(0, 1000))

		return games_list

	def add_game(game: Game) -> None:
		self._games.append(game)

	def get_games() -> List[Game]:
		return self._games

