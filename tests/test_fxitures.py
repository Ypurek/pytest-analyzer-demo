from pytest import mark
import time


def test_pass_fixture(meaning_of_life):
    time.sleep(1)
    assert meaning_of_life + 8 == 50


def test_fail_fixture(failed_fixture):
    time.sleep(1)
    assert 2 + 2 == 4
