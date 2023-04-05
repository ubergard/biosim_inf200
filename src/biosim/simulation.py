# -*- coding: utf-8 -*-

__author__ = 'Jon Augensen & Lars Øvergård, NMBU'
__email__ = 'jon.augensen@nmbu.no / lars.overgard@hotmail.com'

"""
This file contains the interface for our biosimulation.
This code is developed by Copyright (c) 2021 Hans Ekkehard Plesser / NMBU,
and is used to control and modify our setup.
Only the code in the function is added by our team (Jon & Lars).
"""

import random
import os
from .island import Island
from .animals import Herbivores, Carnivores
from .biome import Lowland, Highland, Desert, Water, Fence, Mountain
from .graphics import Plot


class BioSim:
    """
    This is our biosim class.
    """
    def __init__(self, island_map, ini_pop, seed, vis_years=1, ymax_animals=None, cmax_animals=None,
                 hist_specs=None, img_dir=None, img_base=None, img_fmt='png', img_years=None,
                 log_file=None):
        """
        This docstring belongs to biosim __init__
        :param island_map: Multi-line string specifying island geography
        :param ini_pop: List of dictionaries specifying initial population
        :param seed: Integer used as random number seed
        :param ymax_animals: Number specifying y-axis limit for graph showing animal numbers
        :param cmax_animals: Dict specifying color-code limits for animal densities
        :param hist_specs: Specifications for histograms, see below
        :param vis_years: years between visualization updates (if 0, disable graphics)
        :param img_dir: String with path to directory for figures
        :param img_base: String with beginning of file name for figures
        :param img_fmt: String with file type for figures, e.g. ’png’
        :param img_years: years between visualizations saved to files (default: vis_years)
        :param log_file: If given, write animal counts to this file
        If ymax_animals is None, the y-axis limit should be adjusted automatically.
        If cmax_animals is None, sensible, fixed default values should be used.
        cmax_animals is a dict mapping species names to numbers, e.g.,
        {’Herbivore’: 50, ’Carnivore’: 20}
        hist_specs is a dictionary with one entry per property for which a histogram shall be shown.
        For each property, a dictionary providing the maximum value and the bin width must be
        given, e.g.,
        {’weight’: {’max’: 80, ’delta’: 2}, ’fitness’: {’max’: 1.0, ’delta’: 0.05}}
        Permitted properties are ’weight’, ’age’, ’fitness’.
        If img_dir is None, no figures are written to file. Filenames are formed as
        f’{os.path.join(img_dir, img_base}_{img_number:05d}.{img_fmt}’
        where img_number are consecutive image numbers starting from 0.
        img_dir and img_base must either be both None or both strings.

        Sets the random seed, creates the island, and adds animals, will add none if zero given.
        If desired, it will show plots and update it once to show initialized animals.
        """
        self.island_map = island_map
        self.ini_pop = ini_pop
        self.seed = seed
        self.vis_years = vis_years
        self.ymax_animals = ymax_animals
        self.cmax_animals = cmax_animals
        self.hist_specs = hist_specs
        self.img_dir = img_dir
        self.img_base = img_base
        self.img_fmt = img_fmt
        self.log_file = log_file
        self.plot_window = 0

        if img_years or img_years == 0:
            self.img_years = img_years
        else:
            self.img_years = vis_years

        random.seed(self.seed)
        self.island = Island(self.island_map)
        self.island.make_island()
        self.island.add_pop(self.ini_pop)
        if self.vis_years and self.vis_years != 0:
            self.plot_window = Plot(self.island_map, self.vis_years, self.img_years, self.img_fmt,
                                    self.img_dir, self.img_base, self.hist_specs, self.ymax_animals,
                                    self.cmax_animals)
            self.plot_window.update_plot(self.island.do_all_stats())

    @staticmethod
    def set_animal_parameters(species, params):
        """
        Set parameters for animal species.
        :param species: String, name of animal species
        :param params: Dict with valid parameter specification for species
        """
        if species == "Herbivore":
            for param in params:
                if hasattr(Herbivores, param):
                    setattr(Herbivores, param, params[param])
                else:
                    raise ValueError("'" + param + "' is not a parameter in " + species +
                                     ". Check spelling!")
        elif species == "Carnivore":
            for param in params:
                if hasattr(Carnivores, param):
                    setattr(Carnivores, param, params[param])
                else:
                    raise ValueError("'" + param + "' is not a parameter in " + species +
                                     ". Check spelling!")
        else:
            raise ValueError("'" + species + "' is not in this simulation. Check spelling!")

    @staticmethod
    def set_landscape_parameters(landscape, params):
        """
        Set parameters for landscape type.
        :param landscape: String, code letter for landscape
        :param params: Dict with valid parameter specification for landscape
        """
        if landscape == "D":
            for param in params:
                if hasattr(Desert, param):
                    setattr(Desert, param, params[param])
                else:
                    raise ValueError("'" + param + "' is not a parameter in " + landscape +
                                     ". Check spelling!")
        elif landscape == "W":
            for param in params:
                if hasattr(Water, param):
                    setattr(Water, param, params[param])
                else:
                    raise ValueError("'" + param + "' is not a parameter in " + landscape +
                                     ". Check spelling!")
        elif landscape == "L":
            for param in params:
                if hasattr(Lowland, param):
                    setattr(Lowland, param, params[param])
                else:
                    raise ValueError("'" + param + "' is not a parameter in " + landscape +
                                     ". Check spelling!")
        elif landscape == "H":
            for param in params:
                if hasattr(Highland, param):
                    setattr(Highland, param, params[param])
                else:
                    raise ValueError("'" + param + "' is not a parameter in " + landscape +
                                     ". Check spelling!")
        elif landscape == "M":
            for param in params:
                if hasattr(Mountain, param):
                    setattr(Mountain, param, params[param])
                else:
                    raise ValueError("'" + param + "' is not a parameter in " + landscape +
                                     ". Check spelling!")
        elif landscape == "F":
            for param in params:
                if hasattr(Fence, param):
                    setattr(Fence, param, params[param])
                else:
                    raise ValueError("'" + param + "' is not a parameter in " + landscape +
                                     ". Check spelling!")
        else:
            raise ValueError("'" + landscape + "' is not in simulation. Check spelling!")

    def simulate(self, num_years):
        """
        Run simulation while visualizing the result.
        Will also create a folder, if it doesn't exist, with a text file which contains a log over
        the population in the sim for each year. File will be save to a folder named logs, and it's
        name will be determined by the user and the current seed.
        :param num_years: number of years to simulate
        """
        if type(num_years) != int:
            raise ValueError("Year must be a whole number and can't be written!")
        elif num_years < 0:
            raise ValueError("Year can not be negative!")
        else:
            path_name = ''
            if self.log_file:
                path_name = '../logs/' + self.log_file + str(self.seed)
                if not os.path.isdir('../logs/'):
                    os.mkdir('../logs/')
            for year in range(num_years):
                self.island.simulate_island()
                if self.vis_years and self.vis_years != 0 and self.island.year % \
                        self.vis_years == 0:
                    self.plot_window.update_plot(self.island.do_all_stats())
                if self.log_file:
                    f = open(path_name, "a")
                    f.write('Year: ' + str(self.island.year) + ' Herbivores: '
                            + str(self.island.herbivore_pop_history[-1]) + ' Carnivores: ' +
                            str(self.island.carnivore_pop_history[-1]) + " \n")
                    f.close()

    def add_population(self, population):
        """
        Add a population to the island
        :param population: List of dictionaries specifying population
        """
        self.island.add_pop(population)

    @property
    def year(self):
        """Last year simulated."""
        return self.island.year

    @property
    def num_animals(self):
        """Total number of animals on island."""
        return self.island.herbivore_pop_history[-1] + self.island.carnivore_pop_history[-1]

    @property
    def num_animals_per_species(self):
        """Number of animals per species in island, as dictionary."""
        return {'Herbivore': self.island.herbivore_pop_history[-1],
                'Carnivore': self.island.carnivore_pop_history[-1]}

    def make_movie(self):
        """Create MPEG4 movie from visualization images saved."""
        if not os.path.isdir('../video/'):
            os.mkdir('../video/')
        os.system("ffmpeg -r 1 -i ../" + self.img_dir + "/" + self.img_base + "_0000%01d.png "
                                                                              "-vcodec "
                                                                              "mpeg4 -y "
                                                                              "../video/"
                                                                              "simulation_movie."
                                                                              "mp4")
