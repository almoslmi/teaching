"""Test module for the Calculator library"""

import calculator

class TestCalculator:

    def test_add_with_positives():
        assert calculator.add(5, 6) == 11
    
    def test_add_with_negatives():
        assert calculator.add(-1, -37) == -38

    def test_add_with_zero():
        assert calculator.add(0, 1) == 1

    def test_subtract_with_all_positives():
        assert calculator.subtract(5, 4) == 1
    
    def test_subtract_with_first_negative():
        assert calculator.subtract(-1, 4) == -5

    def test_subtract_with_second_negative():
        assert calculator.subtract(1, -4) == 5

    def test_multiply_with_integers():
        assert calculator.multiply(4, 5) == 20

    def test_multiply_with_floats():
        assert calculator.multiply(1.2, 4) == 4.8

    def test_integer_divides_like_float():
        assert calculator.divide(5, 2) == 2.5
        assert calculator.divide(4, 2) == 2

    def test_divide_with_zero_returns_none():
        assert calculator.divide(4, 0) == None

    def test_square_root_with_positive():
        assert calculator.sqrt(81) == 9

    def test_square_root_with_negative_gives_none():
        assert calculator.sqrt(-5) == None

    def test_sqrt_of_zero_is_zero():
        assert calculator.sqrt(0) == 0

    def test_compare_greater_than():
        assert calculator.compare(20, 10) == 1

    def test_compare_less_than():
        assert calculator.compare(10, 20) == -1

    def test_compare_equal():
        assert calculator.compare(20, 20) == 0

    def test_clear_always_returns_zero():
        assert calculator.clear(1203) == 0
        assert calculator.clear(-123.45) == 0
        assert calculator.clear("Words?") == 0
        assert calculator.clear(None) == 0
        