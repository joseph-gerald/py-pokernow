```py
"""
Example: Basic club operations with py-pokernow
"""

from pokernow import PokerNowSession

# Initialize session with your apt token
session = PokerNowSession(apt_token="your_apt_token_here")

# Get club information
club = session.get_club("slug") # e.g https://www.pokernow.club/clubs/slug

# Display club information
print(f"Club: {club.name}")
print(f"Description: {club.description}")
print(f"Created: {club.created_at}")
print(f"Plan: {club.plan_type}")
print(f"Max Players: {club.max_players}")
print()

# List all players
print(f"Total Players: {len(club.players)}")
print("\nPlayers with balances:")
for player in club.get_players_with_balance():
    print(f"  {player.username}: {player.chips_balance} chips ({player.club_role})")
print()

# Show total chips in circulation
print(f"Total chips in club: {club.total_chips_in_club()}")
print()

# List active games
print(f"Active Games: {len(club.get_active_games())}")
for game in club.get_active_games():
    print(f"  {game.custom_table_name}")
    print(f"    Blinds: {game.small_blind}/{game.big_blind}")
    print(f"    Status: {game.status}")
    print(f"    Type: {game.game_type}")
    print()

```

```
Club: Joe's Dungeon
Description: XXXXX
Created: 2025-11-23 22:09:51+00:00
Plan: platinum
Max Players: 100

Total Players: 2

Players with balances:
  Joseph: 5422 chips (admin)
  Admin: 3819 chips (owner)

Total chips in club: 9241

Active Games: 1
  50/100
    Blinds: 50/100
    Status: waiting
    Type: th
```