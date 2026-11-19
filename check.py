"""The check for this exercise: are your tests good enough to catch real bugs?

It runs your tests (every test in tests/) four times, each time in a copy of this folder:
  1) with the working shipping.py: there must be tests, and every one must pass;
  2) to 4) with a copy of shipping.py that has one bug planted in it: at least one of your tests must fail.

Run it with: python check.py (with the virtual environment on). You don't need to change this file,
and it's more fun not to read the planted bugs in check/planted-bugs/ until you're done.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent

PLANTED_BUGS = [
    ("bug-1", "free shipping that starts above $50",
     "Test an order of exactly $50.00: it ships free."),
    ("bug-2", "a zone that doesn't exist, charged like zone 3",
     "Check that shipping_cost refuses zone 4 with a ValueError, using pytest.raises."),
    ("bug-3", "the rush fee left off orders that ship free",
     "Test a rush order of $50 or more: it still pays the $12.00 rush fee."),
]


def run_your_tests(shipping_file):
    """Copies your tests and pytest.ini into a new folder with shipping_file as shipping.py, runs pytest there,
    and gives back pytest's exit code: 0 every test passed, 1 a test failed, 5 there were no tests."""
    with tempfile.TemporaryDirectory() as folder:
        copy = Path(folder)
        shutil.copytree(HERE / "tests", copy / "tests", ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copy(HERE / "pytest.ini", copy / "pytest.ini")
        shutil.copy(shipping_file, copy / "shipping.py")
        run = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
            cwd=copy, capture_output=True, text=True,
        )
        return run.returncode


print("Checking your tests against the working shipping.py and three copies with a bug planted in each.")
print()

checks_passed = 0
working = run_your_tests(HERE / "shipping.py")
if working == 0:
    print("1) your tests pass on the working shipping.py: yes")
    checks_passed += 1
elif working == 5:
    print("1) your tests pass on the working shipping.py: not yet")
    print("   There are no tests yet: write them in tests/test_shipping.py.")
else:
    print("1) your tests pass on the working shipping.py: not yet")
    print("   A test fails on the working code, so the test is the one to fix. Run pytest to see which,")
    print("   and work its expected value out again from the README.")

for number, (folder, bug, tip) in enumerate(PLANTED_BUGS, start=2):
    print(f"{number}) your tests catch planted bug {number - 1}, {bug}: ", end="")
    if working != 0:
        print("not yet")
        print("   Get check 1 passing first: a bug only counts as caught when your tests pass on the working code.")
    elif run_your_tests(HERE / "check" / "planted-bugs" / folder / "shipping.py") != 0:
        print("yes")
        checks_passed += 1
    else:
        print("not yet")
        print("   Every one of your tests passed on the copy with this bug, so it would reach real customers.")
        print(f"   {tip}")

print()
if checks_passed == 4:
    print("All 4 checks pass: your tests catch every planted bug.")
else:
    print(f"{checks_passed} of 4 checks pass so far.")
    sys.exit(1)
