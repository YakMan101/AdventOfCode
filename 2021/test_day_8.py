import pytest

from day_8 import load_data, count_unique_numbers


def test_load_data():

    inputs, outputs = load_data()

    assert isinstance(inputs, list) and isinstance(outputs, list)
    assert isinstance(inputs[0], list) and isinstance(outputs[0], list)
    assert isinstance(inputs[0][0], str) and isinstance(outputs[0][0], str)


@pytest.mark.parametrize("output_list, number", [(['fdgacbe', 'cefdb', 'cefbgd', 'gcbe'], 2),
                                                 (['fcgedb', 'cgb',
                                                  'dgebacf', 'gc'], 3),
                                                 (['ed', 'bcgafe',
                                                  'cdgba', 'cbgef'], 1),
                                                 ([''], 0)])
def test_count_unique_numbers(output_list, number):

    assert count_unique_numbers(output_list) == number
