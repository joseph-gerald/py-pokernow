# Quick Start Guide

## Installation from PyPI

Once published:
```bash
pip install py-pokernow
```

## Installation from Source

```bash
git clone https://github.com/yourusername/py-pokernow.git
cd py-pokernow
pip install -e .
```

## Getting Your Authentication Token

Run this in your browser console whilst on pokernow.club:

```js
document.cookie.split("apt=")[1].split(";")[0]
```

or follow these steps:

1. Go to [pokernow.club](https://www.pokernow.club)
2. Log in to your account
3. Open browser DevTools (F12)
4. Go to Application/Storage → Cookies
5. Find the `apt` cookie and copy its value

## Basic Usage

```python
from pokernow import PokerNowSession

# Initialize with your token
session = PokerNowSession(apt_token="your_apt_token_here")

# Get club data
club = session.get_club("your-club-slug")

# Display club info
print(f"Club: {club.name}")
print(f"Players: {len(club.players)}")
print(f"Total chips: {club.total_chips_in_club()}")
```

## Common Operations

### Adding Chips to a Player

```python
player = club.get_player_by_username("username")
session.add_club_chips_to_player(
    club_id=club.id,
    player_id=player.id,
    amount=1000,
    reason="Bonus"
)
```

### Creating a Game

```python
from pokernow import PokerGameConfig

config = PokerGameConfig(
    name="Friday Night",
    small_blind=10,
    big_blind=20,
    maxQuantityPlayers='9'
)

game_id = session.create_club_game(club.id, config)
```

### Getting Transactions

```python
transactions = session.get_club_player_transactions(club.id, player.id)
for tx in transactions:
    print(f"{tx.reason}: {tx.quantity} chips")
```

## Examples

Check the [`examples/`](examples/) directory for more detailed examples:
- [`basic_club_info.py`](examples/basic_club_info.py) - View club information
- [`manage_player_chips.py`](examples/manage_player_chips.py) - Manage player balances
- [`create_games.py`](examples/create_games.py) - Create and manage games
- [`configure_club.py`](examples/configure_club.py) - Configure club settings

## Documentation

See the full [README.md](README.md) for complete API documentation.

## Support

- GitHub Issues: [Report bugs or request features](https://github.com/yourusername/py-pokernow/issues)
- Documentation: See [README.md](README.md)

## License

AGPL-3.0 - See [LICENSE](LICENSE)
