def test_valid_user_has_username(valid_user):
    assert valid_user["username"] == "kv_tester"


def test_admin_user_builds_on_valid_user(admin_user):
    assert admin_user["role"] == "admin"
    assert admin_user["username"] == "kv_tester"


def test_fresh_copy_part_1(valid_user):
    valid_user["username"] = "changed"
    assert valid_user["username"] == "changed"


def test_fresh_copy_part_2(valid_user):
    # Part 1 changed its copy. Do we still get the original?
    assert valid_user["username"] == "kv_tester"



def test_guest_user(guest_user):
    # Part 1 changed its copy. Do we still get the original?
    assert guest_user["role"] == "guest"