import pytest


class TestCalculator:

    @pytest.mark.low
    @pytest.mark.parametrize(['x', 'y', 'value'], [[1, 2, 3], [4, 4, 8], [10, 5, 16]])
    def test_add(self, x, y, value):
        assert x + y == value

    @pytest.mark.low
    def test_subtract(self, variables):
        x, y, value = variables
        assert x - y == value

    @pytest.mark.high
    def test_multiply(self, variables):
        x, y, value = variables
        assert x * y == value

    @pytest.mark.high
    def test_devide(self, variables):
        x, y, value = variables
        assert x / y == value
