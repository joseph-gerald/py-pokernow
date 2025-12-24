```py
"""
Example: Club configuration and settings
"""

from pokernow import PokerNowSession

# Initialize session
session = PokerNowSession(apt_token="your_apt_token_here")
club = session.get_club("slug") # e.g https://www.pokernow.club/clubs/slug

print(f"Configuring club: {club.name}")
print()

# Enable visibility for all members using the club object
print("Enabling visibility settings for all members...")
club.set_ledger_visibility(show=True)
club.set_play_report_visibility(show=True)
club.set_game_archive_visibility(show=True)
print("✓ Ledger, play report, and archive now visible to all members")
print()

# Enable player-to-player transfers using the club object
print("Enabling P2P transfers...")
club.set_p2p_transfers(enabled=True)
print("✓ Players can now transfer chips to each other")
print()

# Set auto approve
print("Setting club to require manual approval...")
club.set_exclusivity(
    option='approve',  # Options: 'manual', 'approve', 'reject'
    message=""
)
print("✓ New members will require approval to join")
print()

# Promote a player to manager using the club object
player = club.get_player_by_username("jeff")
if player:
    club.set_player_role(
        player_user_id=player.user_id,
        role='manager'  # Options: 'member', 'manager', 'owner'
    )
    print(f"✓ {player.username} promoted to manager")
else:
    print("Player 'jeff' not found!")
```

```
Configuring club: Dungeon

Enabling visibility settings for all members...
✓ Ledger, play report, and archive now visible to all members

Enabling P2P transfers...
✓ Players can now transfer chips to each other

Setting club to require manual approval...
✓ New members will require approval to join

Player 'jeff' not found!
```