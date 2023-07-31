from pytest import mark


def test_pass_fixture_sub(meaning_of_life):
    assert meaning_of_life + 8 == 50


def test_fail_fixture_sub(failed_fixture):
    assert 2 + 2 == 4
