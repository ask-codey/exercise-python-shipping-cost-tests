# Exercise: Shipping Cost Tests

Exercise code for the lesson **Exercise: Shipping Cost Tests** in the Python in Depth course on [ask-codey.com](https://www.ask-codey.com).

Crafty Corner, an online craft shop, works out its shipping with `shipping.py`: by weight and zone, free from $50, and a fee for rush orders. The code works, but nobody wrote tests for it, so the next person who changes it could break shipping and not find out until a customer does. You'll write the tests. Then `python check.py` plants three real bugs in copies of `shipping.py`, one at a time, and tells you whether your tests caught each one.

## What's here

- `shipping.py`: Crafty Corner's shipping rules, three functions: `shipping_cost`, `order_shipping` and `save_label`. The docstring under each says what it does, with examples. It works. Ready to use: don't change it.
- `quotes.py`: prints the shipping for five of today's orders with `shipping.py`, so you can see its rules at work. Ready to use.
- `tests/test_shipping.py`: your tests. It has one worked example. For you to finish.
- `check.py` and `check/`: the check that runs your tests against three copies of `shipping.py` with a bug planted in each. You don't need to change them, and it's more fun not to read the copies in `check/planted-bugs/` until you're done.
- `requirements.txt`: the one package the tests need, pytest, at an exact version. Ready to use.
- `pytest.ini`: tells pytest where the tests are and where to find `shipping.py`. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment and the files Python and pytest make as they run. Ready to use.

## Before you start

The tests need pytest, and pytest goes in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on.
- The third installs the packages `requirements.txt` lists into it: here, only pytest.

The `.venv` folder is in `.gitignore`, so Git leaves it out: these commands make it again on any computer.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

## The rules to test

Every weight is in whole pounds, and every price in dollars.

- **`shipping_cost(pounds, zone)`**: the first pound costs the zone's price, $4.50 for zone 1, $6.00 for zone 2 and $8.50 for zone 3, and each pound after it $1.25. A parcel weighs 1 to 70 pounds. Any other weight raises `ValueError: A parcel must weigh 1 to 70 pounds.`, and a zone that isn't 1, 2 or 3 raises `ValueError: There's no shipping zone 4.` (with that zone's number).
- **`order_shipping(order_total, pounds, zone, rush=False)`**: what the customer pays for shipping. Orders of $50.00 or more ship free; below that, the order pays `shipping_cost(pounds, zone)`. A rush order (`rush=True`) pays $12.00 more, even when it ships free.
- **`save_label(path, order_id, pounds, zone, rush=False)`**: writes the order's shipping label to the file at `path`: `Crafty Corner order <order_id>` on the first line, `<pounds> lb to zone <zone>` on the second, and `RUSH` on a third line for a rush order. Every line ends with a line break.

## Write your tests

```bash
pytest
```

It runs every test in `tests/test_shipping.py`. Cover every behavior below with at least one test, and work out each expected value by hand from the rules above before you write it down.

**`shipping_cost`**

1. `shipping_cost(3, 2)` returns `8.5`: $6.00 for the first pound, plus 2 more pounds at $1.25. (This is the worked example.)
2. `shipping_cost(1, 1)` returns `4.5`: the smallest parcel, with no extra pounds.
3. `shipping_cost(70, 3)` returns `94.75`: the biggest parcel, $8.50 plus 69 more pounds at $1.25.
4. `shipping_cost(0, 1)` and `shipping_cost(71, 1)` each raise a `ValueError` whose message is `A parcel must weigh 1 to 70 pounds.` Test both.
5. `shipping_cost(2, 4)` raises a `ValueError` whose message is `There's no shipping zone 4.`

**`order_shipping`**

6. `order_shipping(32.00, 3, 2)` returns `8.5`: below $50, the order pays `shipping_cost(3, 2)`.
7. `order_shipping(49.99, 3, 2)` returns `8.5`: one cent below free shipping still pays.
8. `order_shipping(50.00, 3, 2)` returns `0.0`: free shipping starts at exactly $50.00.
9. `order_shipping(32.00, 3, 2, rush=True)` returns `20.5`: $8.50 plus the $12.00 rush fee.
10. `order_shipping(64.00, 3, 2, rush=True)` returns `12.0`: the order ships free, and still pays the rush fee.

**`save_label`**

11. `save_label(path, 1042, 3, 2)` writes the file at `path` with exactly `"Crafty Corner order 1042\n3 lb to zone 2\n"`.
12. `save_label(path, 1043, 1, 1, rush=True)` writes the file at `path` with exactly `"Crafty Corner order 1043\n1 lb to zone 1\nRUSH\n"`.

## Check your work

```bash
python check.py
```

It runs your tests four times and prints a numbered line for each run:

1. **On the working `shipping.py`.** There must be tests, and every one must pass. If one fails here, the code is right and the test is wrong: work its expected value out again from the rules.
2. **On a copy where free shipping starts above $50.**
3. **On a copy that charges a zone that doesn't exist like zone 3.**
4. **On a copy that leaves the rush fee off orders that ship free.**

A planted bug counts as caught when at least one of your tests fails on its copy. If all your tests pass on a broken copy, that bug would reach real customers, and the line says what kind of test to add.

On the starter, check 1 passes (the worked example passes) and checks 2 to 4 don't: that's expected, because one test can't catch three bugs yet. When the last line says *All 4 checks pass*, your tests protect the shipping rules.

To see the rules at work, run:

```bash
python quotes.py
```

## The rules

- Don't change `shipping.py`. It works; the tests are your work.
- Write your tests in `tests/test_shipping.py` and bring the functions in from `shipping` (`from shipping import ...`), as the worked example does, so the check can swap in its planted-bug copies.
- Name every test after its behavior's number and what it checks, such as `test_8_order_of_exactly_50_ships_free`.
- Don't change `check.py` or the copies in `check/`.

## Tips

- Work out each expected value by hand first, from the rules above. A test that copies whatever the code returns proves nothing.
- Bugs hide at the edges: $49.99 and $50.00, 1 pound and 70, 0 and 71.
- `with pytest.raises(ValueError, match="...")` makes sure the code inside it raises a `ValueError` whose message contains those words.
- `@pytest.mark.parametrize` runs one test for each example in a list: 0 and 71 pounds, say.
- For `save_label`, give your test the `tmp_path` fixture and write the label into it: `label = tmp_path / "label-1042.txt"`. Then `label.read_text(encoding="utf-8")` reads the whole file back as one string.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step.
