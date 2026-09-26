# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.6] - 2026-09-26

### Fixed
- `add_club_chips_to_player` now raises `ValueError` when PokerNow refuses the
  operation (HTTP 200 + `{"success": false}`), matching
  `remove_club_chips_from_player`. Previously a refused credit was returned as
  if it had succeeded, so callers could not tell that no chips had moved.
- `PokerGameConfig.to_dict(is_preset=True)` no longer emits malformed keys
  (`config[blinds][0][]]` -> `config[blinds][0][]`), which broke the form
  encoding used by `create_club_preset`.
- `get_club` raises a clear `ValueError` when the club page cannot be parsed
  instead of leaking an `IndexError` from the fallback parser.

### Added
- Optional `timeout` argument on `PokerNowSession` (and `login`) that bounds
  every HTTP request made through the session. Without one, a hung request
  blocks the caller indefinitely.

### Changed
- Chip operations, transaction history and credit limits document and expect
  the player's network `user_id` (`player.user_id`), not the club player id
  (`player.id`); README examples corrected.
- `set_landing_page` now advertises its actual `requests.Response` return
  value (it always returned the raw response; callers must check `success`).

## [0.1.0] - 2025-12-24

### Added
- Initial release
- PokerNowSession class for API interactions
- PokerNowClub class for club data management
- PokerNowPlayer class for player information
- PokerNowGame class for game/table management
- PokerNowTransaction class for wallet transactions
- PokerGameConfig class for game configuration
- Club management methods (create, get, update settings)
- Player management methods (add/remove chips, set roles, credit limits)
- Game management methods (create games, presets, close games)
- Transaction history retrieval
- Basic authentication support
- User profile update method

[Unreleased]: https://github.com/joseph-gerald/py-pokernow/compare/v0.2.6...HEAD
[0.2.6]: https://github.com/joseph-gerald/py-pokernow/releases/tag/v0.2.6
[0.1.0]: https://github.com/joseph-gerald/py-pokernow/releases/tag/v0.1.0
