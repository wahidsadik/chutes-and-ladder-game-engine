import unittest

import utils.game_helpers as game_helpers
from v1.dice import Dice
from v1.game import Game
from v1.game_board import GameBoard


class TestGame(unittest.TestCase):
    def setUp(self):
        self._under_test = Game(GameBoard(size=5))

    def test_initialization_with_correct_state(self):
        self.assertFalse(self._under_test.is_game_still_on())
        self.assertEqual(self._under_test.iterations, 0)
        # TODO add more

    def test_register_usecases(self):
        with self.subTest(message='ensure non players are pre-registered'):
            self.assertEqual(len(self._under_test.players_all), 0)
            self.assertEqual(len(self._under_test.players_playing), 0)
            self.assertEqual(len(self._under_test.players_finished), 0)

        with self.subTest(message='register single player'):
            self.assertTrue(self._under_test.register_player('John'))
            self.assertTrue(game_helpers.find_player_by_name(self._under_test.players_all, 'John'))

        with self.subTest(message='register multiple players'):
            self.assertTrue(self._under_test.register_players(['Joe', 'Jill']))
            self.assertTrue(game_helpers.find_player_by_name(self._under_test.players_all, 'Joe'))
            self.assertTrue(game_helpers.find_player_by_name(self._under_test.players_all, 'Jill'))

        with self.subTest(message='reregister fails'):
            self.assertFalse(self._under_test.register_player('John'))
            self.assertTrue(game_helpers.count_player_by_name(self._under_test.players_all, 'John'))

    def test_start_game_usecases(self):

        with self.subTest(message='cannot start_game without adding players'):
            self.assertFalse(self._under_test.start_game())

        self._under_test.register_players(['Joe', 'Jill'])
        self.assertTrue(self._under_test.start_game())

        with self.subTest(message='test other invariants'):
            self.assertTrue(self._under_test.is_game_still_on())
            self.assertEqual(self._under_test.iterations, 0)
            self.assertEqual(len(self._under_test.players_playing), 2)

        with self.subTest(message='cannot call start_game on a active'):
            self.assertFalse(self._under_test.start_game())

        with self.subTest(message='cannot register after game starts'):
            self.assertFalse(self._under_test.register_player('JJ'))

    def test_reset_usecase(self):
        pass

    def test_iterations_usecases(self):
        self._under_test.register_player('John')

        with self.subTest(message='initial iterations should be 0'):
            self.assertEqual(self._under_test.iterations, 0)

        with self.subTest(message='must start_game() before start_iteration()'):
            self.assertFalse(self._under_test.start_iteration())
            self.assertEqual(self._under_test.iterations, 0)

        self.assertTrue(self._under_test.start_game())

        with self.subTest(message='start_iteration() after start_game()'):
            self.assertTrue(self._under_test.start_iteration())
            self.assertEqual(self._under_test.iterations, 1)

        with self.subTest(message='start_iteration() cannot be called until end_iteration'):
            self.assertFalse(self._under_test.start_iteration())
            self.assertEqual(self._under_test.iterations, 1)

        with self.subTest(message='end_iteration() does not change iterations'):
            self.assertTrue(self._under_test.end_iteration())
            self.assertEqual(self._under_test.iterations, 1)

        with self.subTest(message='end_iteration() cannot be called before start_iteration'):
            self.assertFalse(self._under_test.end_iteration())
            self.assertEqual(self._under_test.iterations, 1)

    def test_happy_path(self):
        dice = Dice()

        players_all = [
            "Tom",
            "Jerry",
            "Donald",
            "Micky",
            "Goofy",
        ]

        self._under_test.register_players(players_all)
        self._under_test.start_game()

        while self._under_test.is_game_still_on():
            self._under_test.start_iteration()
            for player in self._under_test.players_playing:
                self._under_test.player_rolls(player, dice.roll())

            self._under_test.end_iteration()
