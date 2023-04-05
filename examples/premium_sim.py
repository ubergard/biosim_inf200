# -*- coding: utf-8 -*-

"""
Full island simulation with herbivores and carnivores.
"""

__author__ = 'Jon Augensen & Lars Øvergård, NMBU'
__email__ = 'jon.augensen@nmbu.no / lars.overgard@hotmail.com'

import textwrap
from biosim.simulation import BioSim

if __name__ == '__main__':

    geogr = """\
              FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
              FWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWF
              FWMMMMMMWMMWWWMMWWWWWMWWWWWWWWWWWMMMMWF
              FWWMMMMMMMMMMMMMMMMMMMMWWWWMMMMMMMMMWWF
              FWWMMMMMMMMMMMWWWMMMMMMWWWWMMMMMMMWWWWF
              FWWMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMWWWF
              FWMMMMMMHHMMMMMMWWMMMMMMMMMMMMMMMMMMWWF
              FWMMMHHHHHHMMMMMMWHHHHHHHHHHHHHHHWWWWWF
              FWHHLLHHHHHHHHHHWWHHHHHHHHHHHHWWWWWWWWF
              FWLLLLLHHHHHHHHHWHHLLHHHHHHHHHWWWWWWWWF
              FWWLLLLLLLHHHHHWWHHHLLLHHHHHHHHHHLLWWWF
              FWWWLLLLLLLLWWWWWWLWWWLLLLHHHHHLLLLLWWF
              FWWLLLLLLLLWWLLLLWWWLWWLLLLLLLLLLLLWWWF
              FWLLLLLLLLLWLLLLLLLLLLWWWWWLLLLLLWWWWWF
              FWLLLLLLLLLWWWLLLLLLLLLLLLLLLLLLLLLWWWF
              FWLLLLLLLLLLLLWLLLLLLLLLLLLLLLLLLLLWWWF
              FWLLLLLWWWWLLLWLLLLLLLLLLLLLLLLLWWWWWWF
              FWLLLLLWWWWWLLWWLLLLLLLLLLLLLDDDDWWWWWF
              FWLLLLLWWWWWWLLWLLLLLLLLLLLDDDDDDDMWWWF
              FWLLLLLLLLLLWWWWLLLLLLLLLLDDDDDDDDMMMWF
              FWLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDMMWF
              FWLLLLLLLLLLLLLLLWWWWWWDDDDDDDDDDMMMWWF
              FWWWWWLLLLLLLWWWWWWWWWWWWWWWDDDMMMWWWWF
              FWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWF
              FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
               """
    geogr = textwrap.dedent(geogr)

    ini_herbs = [{'loc': (10, 7), 'pop': [{'species': 'Herbivore', 'age': 5, 'weight': 20}
                                          for _ in range(200)]}]

    ini_herbs_2 = [{'loc': (6, 24), 'pop': [{'species': 'Herbivore', 'age': 5, 'weight': 20}
                                            for _ in range(200)]}]

    ini_carns = [{'loc': (11, 9), 'pop': [{'species': 'Carnivore', 'age': 5, 'weight': 20}
                                          for _ in range(100)]}]

    ini_carns_2 = [{'loc': (6, 23), 'pop': [{'species': 'Carnivore', 'age': 5, 'weight': 20}
                                            for _ in range(60)]}]

    sim = BioSim(geogr, ini_herbs + ini_carns + ini_herbs_2 + ini_carns_2, seed=103, vis_years=4)

    sim.simulate(400)

    print("Year: ", sim.year)
    print("Total number of animals: ", sim.num_animals)
    print("Animals: ", sim.num_animals_per_species)
