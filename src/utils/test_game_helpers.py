import unittest

import utils.game_helpers as game_helpers
from v1.player import Player


class TestGameHelper(unittest.TestCase):
    def setUp(self):
        self._under_test = game_helpers

    def test_find_player_by_name(self):
        names = [
            'John',
            'Jack',
            'Jill',
            'Jane'
        ]

        players = [Player(name) for name in names]

        with self.subTest('function finds player by name successfully'):
            found = self._under_test.find_player_by_name(players, 'Jack')

            self.assertIsNotNone(found)
            self.assertEqual(found.name, 'Jack')

        with self.subTest('function does not find player by name'):
            found = self._under_test.find_player_by_name(players, 'Doe')

            self.assertIsNone(found)

    def test_count_player_by_name(self):
        names = [
            'John',
            'John',
            'Jack',
            'Jill',
            'Jane',
            'John',
        ]

        players = [Player(name) for name in names]

        with self.subTest('function finds player by name successfully'):
            self.assertEqual(self._under_test.count_player_by_name(players, 'John'), 3)

        with self.subTest('function does not find player by name'):
            self.assertEqual(self._under_test.count_player_by_name(players, 'Doe'), 0)
