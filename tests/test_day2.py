import pytest


def is_valid_password(password: str) -> bool:
    """Temporary demo logic. Real framework code comes in Phase 1."""
    return len(password) >= 8 and any(ch.isdigit() for ch in password)


@pytest.mark.smoke
def test_valid_password_is_accepted():
    # Arrange
    password = "secret123"

    # Act
    result = is_valid_password(password)

    # Assert
    assert result is True


@pytest.mark.regression
@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("secret123", True, id="valid-8plus-with-digit"),
        pytest.param("short1", False, id="too-short"),
        pytest.param("nodigitshere", False, id="no-digit"),
        pytest.param("", False, id="empty"),
        pytest.param("abcdefg1", True, id="exactly-8-with-digit"),  # <- new line
    ],
)
def test_password_rules(password, expected):
    assert is_valid_password(password) is expected