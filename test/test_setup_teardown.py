import pytest

@pytest.fixture(scope='session')
def session_fixture():
    print('\nBefore all session')
    yield
    print('\nAfter all session')
def test_one(session_fixture):
    print('\nIs my test 1')
    pass

def test_two(session_fixture):
    print('\nIs my test 2')
    pass


