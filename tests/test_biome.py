# -*- coding: utf-8 -*-

"""
    This file contains simple test for checking, if biome.py delivers right types of variables.
"""

from biosim.biome import Biomes
import pytest


def test_biome_landtype():
    """Testing that landtype D works and gets applied"""
    x = 2
    y = 1
    landtype = "D"
    cell = Biomes(x, y, landtype)
    assert cell.land_type == landtype


def test_biome_water_availability():
    """Testing that landtype W works and gets correct availability, Checking default value"""
    x = 1
    y = 1
    landtype = "W"
    cell = Biomes(x, y, landtype)
    assert not cell.availability


def test_biome_highland_availability():
    """Testing that landtype H works and gets correct availability, Checking default value"""
    x = 3
    y = 1
    landtype = "H"
    cell = Biomes(x, y, landtype)
    assert cell.availability


def test_biome_empty_list():
    """Testing that landtype F works and has a empty list at start"""
    x = 1
    y = 1
    landtype = "F"
    cell = Biomes(x, y, landtype)
    assert not cell.herbivore_list


def test_biome_adding_animal_herb():
    """Testing that landtype M works and that we can add animals to it"""
    x = 1
    y = 3
    landtype = "M"
    cell = Biomes(x, y, landtype)
    animal_params = {'species': 'Herbivore', 'age': 10, 'weight': 50}
    cell.add_animal(animal_params)
    assert cell.herbivore_list


def test_biome_adding_animal_carn():
    """Testing that landtype L works and that we can add animals to it"""
    x = 1
    y = 1
    landtype = "L"
    cell = Biomes(x, y, landtype)
    animal_params = {'species': 'Carnivore', 'age': 10, 'weight': 20}
    cell.add_animal(animal_params)
    assert cell.carnivore_list


def test_biome_adding_illegal_specie():
    """Testing that adding a specie that is not in the simulator will raise a ValueError"""
    with pytest.raises(ValueError):
        x = 1
        y = 3
        landtype = "D"
        cell = Biomes(x, y, landtype)
        animal_params = {'species': 'Human', 'age': 23, 'weight': 72}
        cell.add_animal(animal_params)


def test_biome_adding_false_availability():
    """Testing that adding a specie at a cell with false availability will raise ValueError"""
    with pytest.raises(ValueError):
        x = 2
        y = 1
        landtype = "W"
        cell = Biomes(x, y, landtype)
        animal_params = {'species': 'Carnivore', 'age': 10, 'weight': 20}
        cell.add_animal(animal_params)


def test_biome_life_cycle():
    """Testing that landtype L works and that life cycle will run without problems"""
    x = 1
    y = 1
    landtype = "L"
    cell = Biomes(x, y, landtype)
    cell.life_cycle()


def test_biome_refresh_land():
    """Testing that land will update the amount of fodder after refresh land is called"""
    x = 1
    y = 2
    landtype = "M"
    years = 5
    cell = Biomes(x, y, landtype)
    old_fodder_amount = cell.fodder
    fodder_amount = 30
    for _ in range(years):
        cell.eats_fodder(fodder_amount)
    cell.refresh_land()
    assert cell.fodder == old_fodder_amount


def test_biome_eats_fodder():
    """Testing that eats fodder will decrease the amount of fodder"""
    x = 1
    y = 1
    landtype = "L"
    cell = Biomes(x, y, landtype)
    old_fodder = cell.fodder
    fodder_amount = 50
    cell.eats_fodder(fodder_amount)
    assert cell.fodder == old_fodder - fodder_amount


def test_biome_herbivore_eat_update():
    """Testing that a herbivore eating fodder will decrease the amount of fodder."""
    x = 4
    y = 1
    landtype = "H"
    cell = Biomes(x, y, landtype)
    animal_params = {'species': 'Herbivore', 'age': 10, 'weight': 10}
    cell.add_animal(animal_params)
    old_fodder = cell.fodder
    fodder_amount = 10
    cell.herbivore_list[0].feeding_type(cell)
    assert cell.fodder == old_fodder - fodder_amount


def test_biome_update_lists():
    """Testing that biome will remove an animal after it dies and update it"""
    x = 1
    y = 1
    landtype = "L"
    cell = Biomes(x, y, landtype)
    animal_params = {'species': 'Herbivore', 'age': 10, 'weight': 50}
    cell.add_animal(animal_params)
    cell.dead_animal_list.append(cell.herbivore_list[0])
    cell.update_lists(cell.herbivore_list)
    assert cell.herbivore_list == []


def test_biome_adding_migrator():
    """Testing an animal can be added as migrator from a different cell"""
    x = 1
    y = 2
    x_2 = 2
    y_2 = 2
    landtype = "D"
    landtype_2 = "M"
    cell = Biomes(x, y, landtype)
    cell_2 = Biomes(x_2, y_2, landtype_2)
    animal_params = {'species': 'Herbivore', 'age': 10, 'weight': 50}
    cell.add_animal(animal_params)
    cell_2.add_migrator(cell.herbivore_list[0])
    assert cell_2.herbivore_list
