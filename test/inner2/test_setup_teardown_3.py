import pytest

class Dog:
    color = 'Black'
    def __init__(self):
        pass

@pytest.fixture(scope='session')
def session_fixture():
    print('\nBefore all session')
    yield Dog()
    print('\nAfter all session')


@pytest.fixture(scope='function')
def class_function():
    print('\nBefore each function')
    yield
    print('\nAfter each function')


def test_one(session_fixture, class_function):
    print('\nIs my test 1')
    pass

def test_two(session_fixture, class_function):
    print('\nIs my test 2')
    pass


