import pytest


@pytest.fixture
def valid_user():
    """A fresh user dict for every test that asks for it."""
    return {"username": "kv_tester", "password": "secret123"}


@pytest.fixture
def admin_user(valid_user):
    """Builds on valid_user: same user, plus an admin role."""
    return {**valid_user, "role": "admin"}


@pytest.fixture
def guest_user(valid_user):
    """Builds on valid_user: same user, plus an admin role."""
    return {**valid_user, "role": "guest"}


@pytest.fixture(scope="session")
def app_config():
    print("\n  >> SESSION setup: loading config")
    yield {"base_url": "https://example.com", "env": "qa"}
    print("\n  >> SESSION teardown: closing the restaurant")


@pytest.fixture(scope="class")
def logged_in_user(app_config):
    print(f"\n  >> CLASS setup: logging in on {app_config['env']}")
    yield {"name": "kv_tester", "token": "abc123"}
    print("\n  >> CLASS teardown: logging out")


@pytest.fixture
def page(logged_in_user):
    print("\n  >> FUNCTION setup: open a fresh page")
    yield {"url": "about:blank", "user": logged_in_user["name"]}
    print("\n  >> FUNCTION teardown: close the page")