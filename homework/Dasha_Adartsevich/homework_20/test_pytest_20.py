import pytest
import requests


@pytest.fixture(scope='session')
def print_phrases_for_session():
    print('before all')
    yield
    print('after all')


@pytest.fixture(scope='function')
def print_phrases_for_each_test():
    print('hello')
    yield
    print('goodbye')


@pytest.mark.simple
def test_1(print_phrases_for_session, print_phrases_for_each_test):
    assert 1 == 1


@pytest.mark.hard
def test_2(print_phrases_for_each_test):
    assert 2 + 3 == 5


@pytest.mark.simple
def test_3(print_phrases_for_each_test):
    assert 1 < 4


@pytest.mark.simple
def test_4(print_phrases_for_each_test):
    assert 6 != 8


@pytest.mark.hard
def test_5(print_phrases_for_each_test):
    assert 3 + 7 == 10


@pytest.mark.hard
def test_6(print_phrases_for_each_test):
    assert 10 - 6 == 4


@pytest.mark.hard
@pytest.mark.parametrize('data', [(4, 5), (2, 10), (20, 1)])
def test_7(print_phrases_for_each_test, data):
    a, b = data
    assert a * b == 20


@pytest.mark.hard
def test_8(print_phrases_for_each_test):
    assert 15 / 5 != 2


@pytest.mark.hard
@pytest.mark.skip(reason='bug #12345')
def test_9(print_phrases_for_each_test):
    assert 34 * 0.5 == 17


@pytest.mark.simple
def test_10(print_phrases_for_each_test):
    assert 6 == 6
