"""PokerGameConfig key formatting (preset vs game)."""

import unittest

from pokernow import PokerGameConfig


class GameConfigKeyTests(unittest.TestCase):
    def setUp(self):
        self.config = PokerGameConfig(name="test-table", small_blind=10, big_blind=20)

    def test_preset_keys_are_balanced_and_prefixed(self):
        data = self.config.to_dict(is_preset=True)
        for key in data:
            self.assertEqual(key.count("["), key.count("]"), key)
        self.assertIn("config[tableName]", data)
        self.assertIn("config[blinds][0][]", data)
        self.assertIn("config[blindString]", data)

    def test_game_keys_are_unprefixed(self):
        data = self.config.to_dict(is_preset=False)
        self.assertIn("tableName", data)
        self.assertIn("blinds[0][]", data)
        self.assertIn("blindString", data)


if __name__ == "__main__":
    unittest.main()
