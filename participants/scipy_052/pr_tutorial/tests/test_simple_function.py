from pr_tutorial.simple_functions import factorial


def test_factorial_3():
    """Simplest test for one crete case"""

    assert factorial(3) == 6


def test_factorial_0():
    """Check base case"""
    assert factorial(0) == 1
