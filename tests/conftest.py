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