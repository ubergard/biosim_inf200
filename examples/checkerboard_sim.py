# -*- coding: utf-8 -*-

import textwrap
from biosim.simulation import BioSim

__author__ = 'Jon Augensen & Lars Øvergård, NMBU'
__email__ = 'jon.augensen@nmbu.no / lars.overgard@hotmail.com'

"""
This is file for running checkerboard test on migration.
When running it for multiple times, a pattern will be spotted.
Animals will chose direction at random, so some randomness will appear.
"""


if __name__ == '__main__':

    geogr = """\
               WWWWWWWWWWWWWWWWWWWWW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WLLLLLLLLLLLLLLLLLLLW
               WWWWWWWWWWWWWWWWWWWWW"""
    geogr = textwrap.dedent(geogr)

    ini_herbs = [{'loc': (10, 10),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(250)]}]

    sim = BioSim(island_map=geogr, ini_pop=ini_herbs, seed=123456)

    sim.set_animal_parameters('Herbivore', {'mu': 1, 'omega': 0, 'gamma': 0, 'a_half': 1000})
    sim.set_landscape_parameters('L', {'f_max': 600})

    sim.simulate(num_years=10)
