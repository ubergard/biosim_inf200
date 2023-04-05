# -*- coding: utf-8 -*-

"""
    This file contains simple test for checking, if animals.py delivers right types of variables
    and numbers.
"""

from biosim.animals import Animal
import pytest


def test_herbivore_age():
    """Testing that a Herbivore gets the correct age"""
    age_start = 10
    animal_herbivore = Animal({'species': 'Herbivore', 'age': age_start, 'weight': 50})

    assert animal_herbivore.age == age_start


def test_herbivore_aging():
    """Testing that Herbivore get older after running age function"""
    age_start = 10
    animal_herbivore = Animal({'species': 'Herbivore', 'age': age_start, 'weight': 50})

    years = 2
    for _ in range(years):
        animal_herbivore.ages_weight()
    assert animal_herbivore.age == age_start + years


def test_herbivore_weight():
    """Testing that a Herbivore gets correct weight after parameters"""
    weight_start = 50
    animal_herbivore = Animal({'species': 'Herbivore', 'age': 10, 'weight': weight_start})

    assert animal_herbivore.weight == weight_start


def test_carnivore_age():
    """Testing that a Carnivore gets correct age after parameters"""
    age_start = 5
    animal_carnivore = Animal({'species': 'Carnivore', 'age': age_start, 'weight': 50})

    assert animal_carnivore.age == age_start


def test_negative_age():
    """Testing that a Carnivore with negative age will raise a ValueError"""
    with pytest.raises(ValueError):
        age_start = -5
        Animal({'species': 'Carnivore', 'age': age_start, 'weight': 50})


def test_negative_weight():
    """Testing that a Herbivore with negative weight will raise a ValueError"""
    with pytest.raises(ValueError):
        weight_start = -25
        Animal({'species': 'Herbivore', 'age': 10, 'weight': weight_start})


def test_new_born_stage():
    """Testing that new born calf gets the correct stage, in its annual cycle"""
    age_start = 0
    calf_stage = 2
    animal_carnivore = Animal({'species': 'Carnivore', 'age': age_start, 'weight': 50})

    assert animal_carnivore.stage == calf_stage


def test_carnivores_weight():
    """Testing that a Carnivore gets correct weight after Parameters"""
    weight_start = 20
    animal_herbivore = Animal({'species': 'Herbivore', 'age': 10, 'weight': weight_start})

    assert animal_herbivore.weight == weight_start


def test_herbivore_fitness_update():
    """Testing that a Herbivore gets a different fitness after weight loss"""
    weight_start = 50
    new_weight = 10
    animal_herbivore = Animal({'species': 'Herbivore', 'age': 10, 'weight': weight_start})
    old_fitness = animal_herbivore.fitness_update()
    animal_herbivore.weight = new_weight

    assert animal_herbivore.fitness_update() != old_fitness
