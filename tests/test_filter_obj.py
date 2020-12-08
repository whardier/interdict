from interdict import filter_obj


class TestInterdictFilterObj:
    def test_empty_filter(self):
        val = filter_obj({}, {})
        assert val == {}
