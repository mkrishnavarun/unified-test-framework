class TestCart:
    def test_add_item(self, page):
        assert page["user"] == "kv_tester"

    def test_remove_item(self, page):
        assert page["url"] == "about:blank"


class TestProfile:
    def test_view_profile(self, page):
        assert page["user"] == "kv_tester"