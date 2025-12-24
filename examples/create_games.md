```py
"""
Example: Creating and managing games
"""

from pokernow import PokerNowSession, PokerGameConfig

# Initialize session
session = PokerNowSession(apt_token="your_apt_token_here")
club = session.get_club("slug") # e.g https://www.pokernow.club/clubs/slug

# Create a standard Texas Hold'em game
config = PokerGameConfig(
    name="Friday Night Poker",
    small_blind=10,
    big_blind=20,
    maxQuantityPlayers='9',
    gameType='th',
    decisionTime='30',
    timebank='15',
    straddle='true',
    runItTwice='ask_players'
)

# Create the game using the club object
game_id = club.create_game(config)
print(f"Created game with ID: {game_id}")

# Create a PLO game preset for future use
plo_config = PokerGameConfig(
    name="PLO 50/100",
    small_blind=50,
    big_blind=100,
    maxQuantityPlayers='6',
    gameType='plo',
    decisionTime='25',
    timebank='20'
)

# Create preset using the club object
club.create_preset(plo_config)
print(f"Created preset: {plo_config.name}")

# List all games
print("\nAll games in club:")
for game in club.games:
    status = "🟢 Active" if not game.expired else "⚫ Closed"
    print(f"{status} {game.custom_table_name} ({game.small_blind}/{game.big_blind})")
```

```
Created game with ID: pgleLLul6wDbLF34Wppj3tLmc
Created preset: PLO 50/100

All games in club:
🟢 Active 50/100 (50/100)
🟢 Active 50/100 (50/100)
```