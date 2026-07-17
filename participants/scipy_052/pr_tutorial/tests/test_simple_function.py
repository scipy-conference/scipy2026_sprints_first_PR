import pytest

from pr_tutorial.simple_functions import factorial


def test_factorial_3():
    """Simplest test for one crete case"""

    assert factorial(3) == 6


def test_factorial_0():
    """Test base case"""
    assert factorial(0) == 1


def test_factorial_non_neg():
    """Error on negative value"""
    with pytest.raises(RuntimeError, match="negative"):
        factorial(-1)


def test_factorial_float():
    """Error (eventually) for float being passed"""
    with pytest.raises(RuntimeError, match="negative"):
        factorial(1.5)