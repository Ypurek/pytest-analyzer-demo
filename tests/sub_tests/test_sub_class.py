from pytest import mark
import pytest


class TestDemo:

    def test_pass_cls_sub(self):
        assert 2 + 2 == 4

    def test_fail_cls_sub(self):
        assert 2 + 2 == 5

    def test_exception_cls_sub(self):
        raise Exception('test exception')

    @pytest.mark.skip(reason='skip this test')
    def test_skip_cls_sub(self):
        assert 2 + 2 == 4
