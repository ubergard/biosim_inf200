# -*- coding: utf-8 -*-

__author__ = 'Jon Augensen & Lars Øvergård, NMBU'
__email__ = 'jon.augensen@nmbu.no / lars.overgard@hotmail.com'

"""
This file contains functions need for different classes.
It contain functions needed for fitness updates, gives random number and a random
calf weight based on gaussian distribution.
"""

import math
import random


def qua(x_1, x_2, phi):
    """
    Calculates the terms need to calculate the fitness of different animals.
    This function is called twice during a fitness update.
    Different values vs the first and second run. (1st/2nd)
    :param x_1: float/int. Age of the animal/weight of the animal
    :param x_2: int/int. Age half / weight half  - Parameter,
    used to determine when animal should lose fitness
    :param phi: float/float. phi age/ phi weight  - Parameter, used
    to determine when animal should lose fitness
    :return: float. Half of the fitness calculation.
    """
    qu = 1 / (1 + math.exp(phi * (x_1 - x_2)))

    return qu


def gaussian_weight(w_birth, sigma_birth):
    """
    Randomly generates a weight using the mean weight for a calf and the variance.
    Dependent of the species.
    :param w_birth: float. Mean birth weight of the animals.
    :param sigma_birth: float.  Variance of birth weight of the animals.
    :return: float. Calf weight.
    """
    return random.gauss(w_birth, sigma_birth)


def random_number():
    """
    Generates a random number, uses a random seed, which is added to the random module
    from the simulation.py file.
    :return: float. Random number between 0 <= x <= 1
    """
    return random.random()
