from pytest import mark
import pytest
import time


class TestDemo:

    def test_pass_cls(self):
        time.sleep(1)
        assert 2 + 2 == 4

    def test_fail_cls(self):
        time.sleep(1)
        assert 2 + 2 == 5

    def test_exception_cls(self):
        time.sleep(1)
        raise Exception('test exception')

    @pytest.mark.skip(reason='skip this test')
    def test_skip_cls(self):
        assert 2 + 2 == 4
