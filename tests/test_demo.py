from pytest import mark
import pytest
import time


def test_pass():
    time.sleep(1)
    assert 2 + 2 == 4


def test_fail():
    time.sleep(1)
    assert 2 + 2 == 5


def test_exception():
    time.sleep(1)
    raise Exception('test exception')


@pytest.mark.skip(reason='skip this test')
def test_skip():
    assert 2 + 2 == 4
