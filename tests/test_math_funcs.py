# -*- coding: utf-8 -*-

"""
    This file contains simple test for checking, if math_funcs.py delivers right types of variables.
    "test_qua" also checks for correct calculation.
"""

from biosim.math_funcs import qua, gaussian_weight, random_number


def test_qua():
    """Test the qua function, if it return correct number and type"""
    assert qua(1, 1, 1) == 1/2
    assert type(qua(1, 1, 1)) == float


def test_gaussian_weight():
    """Test the gaussian_weight function and if it returns correct type"""
    assert type(gaussian_weight(8.0, 1.5)) == float


def test_random_number():
    """Test the random_number function and if it returns correct type"""
    assert type(random_number()) == float
