"""Chip operation response handling.

PokerNow signals a refused chip operation with HTTP 200 +
``{"success": false, "errmsg": ...}`` — a 200 alone is not success. These
tests pin the contract that both add and remove raise on a refusal, and that
a successful add still exposes the movement id + updated balance.
"""

import unittest
from unittest.mock import MagicMock

from pokernow import PokerNowSession


class ChipOperationResponseTests(unittest.TestCase):
    def setUp(self):
        self.session = PokerNowSession(apt_token="test-token")
        self.http = MagicMock()
        self.session.session = self.http

    def _response(self, payload):
        response = MagicMock()
        response.json.return_value = payload
        return response

    def test_add_raises_when_pokernow_refuses(self):
        """Regression: HTTP 200 + success:false must not look like a credit."""
        self.http.post.return_value = self._response(
            {"success": False, "errmsg": "not enough chips"}
        )
        with self.assertRaises(ValueError) as ctx:
            self.session.add_club_chips_to_player("club", "user", 10, "test")
        self.assertIn("not enough chips", str(ctx.exception))

    def test_add_returns_result_on_success(self):
        self.http.post.return_value = self._response({
            "success": True,
            "result": {
                "movement": {"id": "mv-1"},
                "updatedPlayer": {"chips_balance": 125},
            },
        })
        result = self.session.add_club_chips_to_player("club", "user", 10, "test")
        self.assertTrue(result.success)
        self.assertEqual(result.movement_id, "mv-1")
        self.assertEqual(result.new_balance, 125)

    def test_remove_raises_when_pokernow_refuses(self):
        self.http.post.return_value = self._response(
            {"success": False, "errmsg": "insufficient balance"}
        )
        with self.assertRaises(ValueError):
            self.session.remove_club_chips_from_player("club", "user", 10, "test")


if __name__ == "__main__":
    unittest.main()
