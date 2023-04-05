# -*- coding: utf-8 -*-

__author__ = 'Jon Augensen & Lars Øvergård, NMBU'
__email__ = 'jon.augensen@nmbu.no / lars.overgard@hotmail.com'

"""
This file contains the class for the island or other geographies that can be used on this
population simulator.
This class makes the island, makes the map, adds population, simulates and collects data from
the simulation.
"""

from .biome import Biomes


class Island:
    """
    Here we create our island class
    """
    def __init__(self, layout):
        """
        This docstring belongs to Island __init__ it splits the layout too makes it in to a list
        containing strings.
        Calculates the height and the width of the map and stores these and
        makes a empty map based of these numbers.
        Making instances for keeping track of the year and population history over time.
        :param layout: str. A layout of the geography of the environment.
        """
        self.map = layout.split()
        self.y = len(layout.split())

        temp_map = layout.split()
        self.x = len(temp_map[0])

        self.cell = [[Biomes(m, n, "W") for n in range(self.x)] for m in range(self.y)]

        self.year = 0
        self.herbivore_pop_history = []
        self.carnivore_pop_history = []

    def make_island(self):
        """
        Checks if the layout is correct and contains equal string length, for a correct map,
        then inputs a biome object to the corresponding cell, with data of the landtype.
        :return: None
        """
        for m in range(self.y):
            if len(self.map[m]) != self.x:
                raise ValueError("Map has unequal width!")
            elif (m == 0 or m == self.y-1) and ("D" in self.map[m] or "L" in self.map[m] or
                                                "H" in self.map[m] or "M" in self.map[m]):
                raise ValueError("Map has no boundary at row " + str(m + 1))
            else:
                for n in range(self.x):
                    if (n == 0 or n == self.x-1) and self.map[m][n] != "W" and self.map[m][n] != \
                            "F":
                        raise ValueError("Map has no boundary at", (n+1, m+1))
                    else:
                        self.cell[m][n] = Biomes(m, n, self.map[m][n])

        Biomes.island_map = self.cell

    def add_pop(self, params):
        """
        Adds animals to a given location with specified parameters.
        Tells the object in a given cell do to add_animal function
        :param params: list. Contains a list with dictionaries of animals that should be added to
        island. Dictionaries contain location and parameters of the animal(s).
        :return: None
        """
        for pop_param in params:
            (m, n) = pop_param['loc']
            if m > self.y:
                raise ValueError(str(m) + " is not a valid Y coordinate")
            elif n > self.x:
                raise ValueError(str(n) + " is not a valid X coordinate")
            else:
                for ani in pop_param['pop']:
                    self.cell[m - 1][n - 1].add_animal(ani)
        self.do_count()

    def simulate_island(self):
        """
        Simulates on year, in every cell of the map.
        Updates the year count, and updates land and list before the annual cycle of the
        cell is started.
        :return: None
        """
        self.year += 1
        for m in range(self.y):
            for n in range(self.x):
                self.cell[m][n].refresh_land()
                self.cell[m][n].order_lists()
                self.cell[m][n].life_cycle()
        self.do_count()

    def do_all_stats(self):
        """
        Collect data needed for plotting. Iterates through each cell of the map.
        :return: list. Containing all the data need to plot one slide of the graphics.

        Data being returned is year, population of Herbivores and Carnivores, list of fitness,
        weight and age for both all Herbivores and Carnivores,
        and a map of all the Herbivores and Carnivores
        """
        herbivore_map = [[0 for _ in range(self.x)] for _ in range(self.y)]
        carnivore_map = [[0 for _ in range(self.x)] for _ in range(self.y)]

        island_h_fitness_list = []
        island_h_age_list = []
        island_h_weight_list = []

        island_c_fitness_list = []
        island_c_age_list = []
        island_c_weight_list = []

        for m in range(self.y):
            for n in range(self.x):
                herbivore_map[m][n] = len(self.cell[m][n].herbivore_list)
                carnivore_map[m][n] = len(self.cell[m][n].carnivore_list)

                island_h_fitness_list.extend(self.cell[m][n].h_fitness_list)
                island_h_age_list.extend(self.cell[m][n].h_weight_list)
                island_h_weight_list.extend(self.cell[m][n].h_age_list)

                island_c_fitness_list.extend(self.cell[m][n].c_fitness_list)
                island_c_age_list.extend(self.cell[m][n].c_weight_list)
                island_c_weight_list.extend(self.cell[m][n].c_age_list)

        return [self.year, self.herbivore_pop_history[-1], self.carnivore_pop_history[-1],
                island_h_fitness_list, island_h_age_list, island_h_weight_list,
                island_c_fitness_list, island_c_age_list, island_c_weight_list, herbivore_map,
                carnivore_map]

    def do_count(self):
        """
        Sums up all the Herbivores and Carnivores on the map, then updates instances of
        population history of the Herbivores and Carnivores.
        :return: None
        """
        herbivore_count = 0
        carnivore_count = 0

        for m in range(self.y):
            for n in range(self.x):
                herbivore_count += len(self.cell[m][n].herbivore_list)
                carnivore_count += len(self.cell[m][n].carnivore_list)

        self.herbivore_pop_history.append(herbivore_count)
        self.carnivore_pop_history.append(carnivore_count)
