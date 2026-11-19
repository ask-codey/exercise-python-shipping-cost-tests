# Prints today's shipping for a few Crafty Corner orders with shipping.py, so you can see its rules at work.
# Ready to use. Run it with: python quotes.py
from shipping import order_shipping

orders = [
    (1040, 32.00, 3, 2, False),
    (1041, 49.99, 3, 2, False),
    (1042, 50.00, 3, 2, False),
    (1043, 32.00, 3, 2, True),
    (1044, 64.00, 3, 2, True),
]

print("Crafty Corner: today's shipping")
for order_id, total, pounds, zone, rush in orders:
    cost = order_shipping(total, pounds, zone, rush)
    speed = "standard"
    if rush:
        speed = "rush"
    print(f"Order {order_id}: ${total:.2f}, {pounds} lb to zone {zone}, {speed}: ${cost:.2f} shipping")
