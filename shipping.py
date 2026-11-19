"""Crafty Corner's shipping rules.

This file works, and it's ready to use: don't change it. Your job is the tests in
tests/test_shipping.py, which prove it works and catch anyone who breaks it later.
Every price is in dollars, and every weight in whole pounds.
"""

FIRST_POUND = {1: 4.50, 2: 6.00, 3: 8.50}   # what the first pound costs, by shipping zone
EACH_EXTRA_POUND = 1.25                      # each pound after the first
FREE_SHIPPING_FROM = 50.00                   # orders of this much or more ship free
RUSH_FEE = 12.00                             # added to every rush order, even one that ships free


def shipping_cost(pounds, zone):
    """Return what it costs to send a parcel of pounds to a shipping zone: 1, 2 or 3.

    The first pound costs the zone's price, and each pound after it $1.25.
    A parcel weighs 1 to 70 pounds. Any other weight, or a zone that isn't
    1, 2 or 3, raises a ValueError.

    shipping_cost(3, 2) -> 8.5     ($6.00, plus 2 more pounds at $1.25)
    shipping_cost(1, 1) -> 4.5
    shipping_cost(0, 1) -> ValueError: A parcel must weigh 1 to 70 pounds.
    shipping_cost(2, 4) -> ValueError: There's no shipping zone 4.
    """
    if zone not in FIRST_POUND:
        raise ValueError(f"There's no shipping zone {zone}.")
    if pounds < 1 or pounds > 70:
        raise ValueError("A parcel must weigh 1 to 70 pounds.")
    return round(FIRST_POUND[zone] + (pounds - 1) * EACH_EXTRA_POUND, 2)


def order_shipping(order_total, pounds, zone, rush=False):
    """Return what a customer pays for shipping on an order.

    Orders of $50.00 or more ship free. A rush order pays $12.00 more, even
    when it ships free. The parcel's weight and zone are checked either way,
    so a bad weight or zone raises a ValueError, as in shipping_cost.

    order_shipping(32.00, 3, 2) -> 8.5
    order_shipping(50.00, 3, 2) -> 0.0
    order_shipping(32.00, 3, 2, rush=True) -> 20.5
    order_shipping(64.00, 3, 2, rush=True) -> 12.0
    """
    cost = shipping_cost(pounds, zone)
    if order_total >= FREE_SHIPPING_FROM:
        cost = 0.0
    if rush:
        cost = cost + RUSH_FEE
    return round(cost, 2)


def save_label(path, order_id, pounds, zone, rush=False):
    """Write an order's shipping label to the file at path.

    Two lines, and a third, RUSH, for a rush order:

    Crafty Corner order 1042
    3 lb to zone 2
    """
    with open(path, "w", encoding="utf-8") as label:
        label.write(f"Crafty Corner order {order_id}\n")
        label.write(f"{pounds} lb to zone {zone}\n")
        if rush:
            label.write("RUSH\n")
