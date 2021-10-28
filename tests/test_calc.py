import pytest
# /079352/tests$ pytest --first_arg=10 --second_arg=20 --result=6 test_calc.py
# pytest -m high --first_arg=10


class TestCalculator:

    @pytest.mark.add
    @pytest.mark.low
    @pytest.mark.parametrize(['x', 'y', 'value'], [[1, 2, 3], [4, 4, 8], [10, 5, 16]])
    def test_add(self, x, y, value):
        assert x + y == value

    @pytest.mark.subtract
    @pytest.mark.low
    def test_subtract(self, variables):
        x, y, value = variables
        assert x - y == value

    @pytest.mark.multiply
    @pytest.mark.high
    def test_multiply(self, variables):
        x, y, value = variables
        assert x * y == value

    @pytest.mark.devide
    @pytest.mark.high
    def test_devide(self, variables):
        x, y, value = variables
        assert x / y == value
