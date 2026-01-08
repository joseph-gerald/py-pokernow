```py
"""
Example: Managing player chips and transactions
"""

from pokernow import PokerNowSession

# Initialize session
session = PokerNowSession(apt_token="your_apt_token_here")
club = session.get_club("slug") # e.g https://www.pokernow.club/clubs/slug

# Get a specific player
player = club.get_player_by_username("Joseph Gerald")
if not player:
    print("Player not found!")
    exit(1)

print(f"Player: {player.username}")
print(f"Current balance: {player.chips_balance}")
print(f"Credit limit: {player.credit_limit}")
print()

# Add chips to player using the club object
amount_to_add = 1000
club.add_chips_to_player(
    user_id=player.user_id,
    amount=amount_to_add,
    reason="Weekly bonus"
)
print(f"Added {amount_to_add} chips")

# Send chips to another player using P2P transfer (requires P2P enabled in the club)
recipient = club.get_player_by_username("Alice")
if recipient:
    transfer_amount = 50
    club.send_chips_to_player(
        receiver_user_id=recipient.id,
        amount=transfer_amount
    )
    print(f"Sent {transfer_amount} chips to {recipient.username}")
else:
    print("Recipient 'Alice' not found for transfer")

# Set credit limit using the club object
new_credit_limit = 5000
club.set_credit_limit_for_player(
    user_id=player.user_id,
    amount=new_credit_limit
)
print(f"Set credit limit to {new_credit_limit}")
print()

# Get transaction history using the club object
print("Recent transactions:")
transactions = club.get_player_transactions(player.user_id)
for tx in transactions[:10]:  # Show last 10 transactions
    print(f"  {tx.created_at}: {tx.reason} - {tx.quantity} chips")
```

```
Player: Joseph
Current balance: 4422
Credit limit: 5000

Added 1000 chips
Set credit limit to 5000

Recent transactions:
  2025-11-24 17:36:04+00:00: Credit limit changed from 5000 to 5000 - 0 chips
  2025-11-24 17:36:04+00:00: Weekly bonus - 1000 chips
  2025-11-24 17:35:57+00:00: Credit limit changed from 8000 to 5000 - -3000 chips
  2025-11-24 17:35:56+00:00: Weekly bonus - 1000 chips
  2025-11-24 17:35:49+00:00: Weekly bonus - 1000 chips
  2025-11-24 01:02:13+00:00: INIT - -2578 chips
  2025-11-24 01:02:13+00:00: Credit limit changed from 8000 to 8000 - 0 chips
  2025-11-24 01:01:49+00:00: Credit limit changed from 8000 to 8000 - 0 chips
  2025-11-24 01:01:21+00:00: Credit limit changed from 2000 to 8000 - 6000 chips
  2025-11-24 01:00:57+00:00: D - 500 chips
```