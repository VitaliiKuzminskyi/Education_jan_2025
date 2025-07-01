import pytest

@pytest.fixture(scope='session')
def session_fixture():
    print('\nBefore all session')
    yield
    print('\nAfter all session')


@pytest.fixture(scope='package')
def package_fixture():
    print('\nBefore each package')
    yield
    print('\nAfter each package')


@pytest.fixture(scope='class')
def class_fixture():
    print('\nBefore each class')
    yield
    print('\nAfter each class')


@pytest.fixture(scope='function')
def class_fixture():
    print('\nBefore each function')
    yield
    print('\nAfter each function')


def test_one(session_fixture, package_fixture, class_fixture):
    print('\nIs my test 1')
    pass

def test_two(session_fixture, package_fixture, class_fixture):
    print('\nIs my test 2')
    pass


