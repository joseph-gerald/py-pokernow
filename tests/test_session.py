"""PokerNowSession plumbing: request timeouts and club-page parsing."""

import json
import unittest
from unittest.mock import MagicMock, patch

import requests

from pokernow import PokerNowClub, PokerNowSession


class TimeoutSessionTests(unittest.TestCase):
    def test_timeout_is_injected(self):
        session = PokerNowSession(apt_token="test-token", timeout=5)
        with patch.object(requests.Session, "request", return_value=MagicMock()) as req:
            session.session.request("GET", "https://example.test/")
        self.assertEqual(req.call_args[1].get("timeout"), 5)

    def test_explicit_timeout_wins(self):
        session = PokerNowSession(apt_token="test-token", timeout=5)
        with patch.object(requests.Session, "request", return_value=MagicMock()) as req:
            session.session.request("GET", "https://example.test/", timeout=1)
        self.assertEqual(req.call_args[1].get("timeout"), 1)

    def test_no_timeout_leaves_requests_default(self):
        session = PokerNowSession(apt_token="test-token")
        with patch.object(requests.Session, "request", return_value=MagicMock()) as req:
            session.session.request("GET", "https://example.test/")
        self.assertNotIn("timeout", req.call_args[1])


class GetClubParsingTests(unittest.TestCase):
    def _session_for_page(self, page_text: str) -> PokerNowSession:
        session = PokerNowSession(apt_token="test-token")
        response = MagicMock()
        response.text = page_text
        session.session = MagicMock()
        session.session.get.return_value = response
        return session

    def test_missing_club_data_raises_valueerror(self):
        session = self._session_for_page("<html><body>no club here</body></html>")
        with self.assertRaises(ValueError):
            session.get_club("club-slug")

    def test_embedded_club_is_parsed(self):
        payload = json.dumps({"slug": "club-slug", "players": []})
        session = self._session_for_page(
            f'<html><script id="embedded-club">{payload}</script></html>')
        club = session.get_club("club-slug")
        self.assertEqual(club.slug, "club-slug")
        self.assertEqual(club.players, [])


class LandingPageContractTests(unittest.TestCase):
    def test_club_set_landing_page_returns_the_raw_response(self):
        session = MagicMock()
        sentinel = MagicMock()
        session.set_club_landing_page.return_value = sentinel
        club = PokerNowClub({"slug": "club-slug", "players": []}, session=session)
        self.assertIs(club.set_landing_page("hello"), sentinel)


if __name__ == "__main__":
    unittest.main()
