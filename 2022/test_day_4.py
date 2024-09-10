
from day_4 import load_input, check_overlap


def test_load_input():

    data = load_input()

    assert isinstance(data, list)
    assert isinstance(data[0], tuple)
    assert isinstance(data[0][0], str)


def test_check_overlap():
    left = '2-3'
    right = '1-4'

    assert check_overlap(left, right) == True


def test_check_overlap():
    left = '100-105'
    right = '95-102'

    assert check_overlap(left, right) == False


def test_check_overlap():
    left = '6-1000'
    right = '90-300'

    assert check_overlap(left, right) == True
