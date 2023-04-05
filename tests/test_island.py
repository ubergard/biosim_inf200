# -*- coding: utf-8 -*-

"""
    This file contains simple test for checking, if island.py delivers right types of variables.
"""

from biosim.island import Island
import textwrap
import pytest


def test_island_map():
    """Testing that an island can handle a map layout and values can be received at
    correct coordinates"""
    map_layout = """\
           WWW
           WLW
           WWW"""
    map_layout = textwrap.dedent(map_layout)
    island = Island(map_layout)
    assert island.map == ['WWW', 'WLW', 'WWW']
    assert island.map[1][1] == "L"


def test_island_map_type():
    """Testing that map layout is stored as correct type"""
    map_layout = """\
           WWW
           WDW
           WWW"""
    map_layout = textwrap.dedent(map_layout)
    island = Island(map_layout)
    assert type(island.map) == list
    assert type(island.map[1][1]) == str


def test_island_make_map_list():
    """Testing that cell layout is stored as correct type"""
    map_layout = """\
           WWW
           WDW
           WWW"""
    map_layout = textwrap.dedent(map_layout)
    island = Island(map_layout)
    island.make_island()
    assert type(island.cell) == list


def test_island_make_map_size():
    """Testing that map size is not changing after being created"""
    map_layout = """\
           WWW
           WDW
           WWW"""
    map_layout = textwrap.dedent(map_layout)
    island = Island(map_layout)
    island.make_island()
    edited_map = map_layout.split()
    assert len(island.cell) == len(map_layout.split())
    assert len(island.cell[0]) == len(edited_map)


def test_island_illegal_map():
    """Testing adding a map without complete barrier raises a ValueError"""
    with pytest.raises(ValueError):
        map_layout = """\
               DWW
               WDW
               WWW"""
        map_layout = textwrap.dedent(map_layout)
        island = Island(map_layout)
        island.make_island()


def test_island_empty_simulation():
    """Testing that 5 year can be simulated"""
    map_layout = """\
           WWW
           WDW
           WWW"""
    map_layout = textwrap.dedent(map_layout)
    island = Island(map_layout)
    island.make_island()
    years = 5
    for _ in range(years):
        island.simulate_island()
    assert island.year == years


def test_island_adding_herbivore():
    """Testing that herbivores can be added"""
    map_layout = """\
           WWW
           WDW
           WWW"""
    map_layout = textwrap.dedent(map_layout)
    animal_count = 50
    ini_herbs = [{'loc': (2, 2),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(animal_count)]}]
    island = Island(map_layout)
    island.make_island()
    island.add_pop(ini_herbs)


def test_island_adding_carnivore():
    """Testing that carnivores can be added"""
    map_layout = """\
           WWW
           WDW
           WWW"""
    map_layout = textwrap.dedent(map_layout)
    animal_count = 50
    ini_carns = [{'loc': (2, 2),
                  'pop': [{'species': 'Carnivore',
                           'age': 5,
                           'weight': 30}
                          for _ in range(animal_count)]}]
    island = Island(map_layout)
    island.make_island()
    island.add_pop(ini_carns)


def test_island_illegal_spawn():
    """Testing that adding animals at wrong coordinates will raise a ValueError"""
    with pytest.raises(ValueError):
        map_layout = """\
               WWW
               WDW
               WWW"""
        map_layout = textwrap.dedent(map_layout)
        animal_count = 50
        ini_herbs = [{'loc': (1, 2),
                      'pop': [{'species': 'Herbivore',
                               'age': 3,
                               'weight': 25}
                              for _ in range(animal_count)]}]
        island = Island(map_layout)
        island.make_island()
        island.add_pop(ini_herbs)


def test_island_herbivore_simulation():
    """Testing that 5 years can be simulated with herbivores"""
    map_layout = """\
           WWW
           WDW
           WWW"""
    map_layout = textwrap.dedent(map_layout)
    animal_count = 50
    ini_herbs = [{'loc': (2, 2),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(animal_count)]}]
    island = Island(map_layout)
    island.make_island()
    island.add_pop(ini_herbs)
    years = 5
    for _ in range(years):
        island.simulate_island()


def test_island_carnivore_simulation():
    """Testing that 2 year can be simulated with carnivores"""
    map_layout = """\
           WWW
           WDW
           WWW"""
    map_layout = textwrap.dedent(map_layout)
    animal_count = 50
    ini_carns = [{'loc': (2, 2),
                  'pop': [{'species': 'Carnivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(animal_count)]}]
    island = Island(map_layout)
    island.make_island()
    island.add_pop(ini_carns)
    years = 2
    for _ in range(years):
        island.simulate_island()


def test_island_do_count():
    """Testing that total animal counter is counting correct"""
    map_layout = """\
           WWW
           WDW
           WWW"""
    map_layout = textwrap.dedent(map_layout)
    animal_count = 50
    ini_herbs = [{'loc': (2, 2),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(animal_count)]}]
    island = Island(map_layout)
    island.make_island()
    island.add_pop(ini_herbs)
    island.do_count()
    assert island.herbivore_pop_history[-1] == animal_count


def test_island_do_all_stats():
    """Checking that do all stats will return a list, and total length of 11,
    which is all the data needed for plots"""
    map_layout = """\
           WWW
           WDW
           WWW"""
    map_layout = textwrap.dedent(map_layout)
    animal_count = 50
    ini_herbs = [{'loc': (2, 2),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(animal_count)]}]
    expected_list_len = 11
    island = Island(map_layout)
    island.make_island()
    island.add_pop(ini_herbs)
    data_list = island.do_all_stats()
    assert type(data_list) == list
    assert len(data_list) == expected_list_len
