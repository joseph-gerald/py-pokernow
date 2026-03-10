# Remove/Kick Player from Club

This example demonstrates how to remove or kick a player from a club.

## Using the Club object

```python
from pokernow import login

# Login to your account
def get_otp(email):
    return input(f"Enter OTP sent to {email}: ")

session = login("your@email.com", get_otp)

# Get your club
club = session.get_club("your-club-slug")

# Remove a player using their network user ID
club.remove_player(user_id="683999")
```

## Using the Session object directly

```python
from pokernow import login

# Login to your account
def get_otp(email):
    return input(f"Enter OTP sent to {email}: ")

session = login("your@email.com", get_otp)

# Remove a player from a specific club
session.remove_player_from_club(
    club_id="9dccdac5-aafb-4dd1-b30c-21cf7356ddc3",
    user_id="683999"
)
```

## Important Notes

- The `user_id` parameter should be the player's **network user ID**, not their club player ID
- You can find the network user ID in the player's `user_id` property: `player.user_id`
- Only club owners and managers can remove players
- Attempting to remove a player without proper permissions will raise a `ValueError`

## Getting the User ID from a Player Object

```python
from pokernow import login

# Login and get club
session = login("your@email.com", lambda e: input(f"Enter OTP: "))
club = session.get_club("your-club-slug")

# Find a player by username
player = club.get_player_by_username("player_name")

if player:
    # Remove the player using their network user ID
    club.remove_player(user_id=player.user_id)
    print(f"Removed player: {player.username}")
else:
    print("Player not found")
```
