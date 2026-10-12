"""Root-level conftest.

Registers the ``--headed`` command-line option so it is available to the
whole test suite, including plain ``pytest -q`` runs from the project root.
"""


def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", help="Show the E2E browser window")
