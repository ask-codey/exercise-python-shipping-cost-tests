# Your tests for Crafty Corner's shipping rules in shipping.py. The README lists the 12 behaviors to cover.
# Run them with: pytest (in the exercise folder, with the virtual environment on).
# Then run: python check.py, to see whether they catch the three bugs it plants in copies of shipping.py.
import pytest

from shipping import order_shipping, save_label, shipping_cost


# Behavior 1, the worked example, to show the shape. Add your own tests below it.
def test_1_shipping_cost_3_pounds_to_zone_2_is_8_50():
    assert shipping_cost(3, 2) == 8.5


# TODO: a test for each of the README's behaviors 2 to 12.
