from pytest import fixture


@fixture(scope='function')
def meaning_of_life():
    return 42


@fixture(scope='function')
def failed_fixture():
    raise Exception('all tests with this fixture will fail')
