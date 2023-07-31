from pytest import mark
import pytest


def test_pass_sub():
    assert 2 + 2 == 4


def test_fail_sub():
    assert 2 + 2 == 5


def test_exception_sub():
    raise Exception('test exception')


@pytest.mark.skip(reason='skip this test')
def test_skip_sub():
    assert 2 + 2 == 4
