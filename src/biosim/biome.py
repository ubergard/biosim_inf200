# -*- coding: utf-8 -*-

__author__ = 'Jon Augensen & Lars Øvergård, NMBU'
__email__ = 'jon.augensen@nmbu.no / lars.overgard@hotmail.com'

"""
This file contains the class for the biomes and classes for different landscapes.
"""

import random
from .animals import Animal
from .math_funcs import random_number


class Biomes:
    """
    A nested list will be given to this class, which contains all the cells/biomes of the map.
    """
    island_map = []

    def __init__(self, y, x, land_type):
        """
        This docstring belongs to Biomes __init__ it makes a object contain it's x and y
        coordinates and landtype.
        It will also create empty lists it need during the simulation.
        An object based on the landtype will also be stored and used to specify what parameters
        this object will have, and for updating these regularly.
        :param y: int. Y-coordinate of the biome.
        :param x: int. X-coordinate of the biome.
        :param land_type: string. Gives what landtype this biome will be.
        """
        self.x = x
        self.y = y
        self.land_type = land_type
        self.land_id = 0
        self.herbivore_list = []
        self.carnivore_list = []
        self.dead_animal_list = []
        self.tot_migrators = []

        self.h_fitness_list = []
        self.h_weight_list = []
        self.h_age_list = []

        self.c_fitness_list = []
        self.c_weight_list = []
        self.c_age_list = []

        if self.land_type == "L":
            self.land_id = Lowland()
        elif self.land_type == "H":
            self.land_id = Highland()
        elif self.land_type == "D":
            self.land_id = Desert()
        elif self.land_type == "W":
            self.land_id = Water()
        elif self.land_type == "M":
            self.land_id = Mountain()
        elif self.land_type == "F":
            self.land_id = Fence()
        else:
            raise ValueError(self.land_type + " is not a valid landtype!")

        self.availability = self.land_id.availability
        self.fodder = self.land_id.f_max

    def add_animal(self, animal_params):
        """
        Will check what specie it is, if it's not in the simulation, it will raise an error.
        If it is in the simulation in will create an objects based of the parameters and add it
        to the correct list in this biome.
        :param animal_params: Dictionary contain all the necessary parameters for an animal.
        :return: None
        """
        if self.availability:
            if animal_params['species'] == "Herbivore":
                ani = Animal(animal_params)
                self.herbivore_list.append(ani)
            elif animal_params['species'] == "Carnivore":
                ani = Animal(animal_params)
                self.carnivore_list.append(ani)
            else:
                raise ValueError("'" + animal_params['species'] +
                                 "' is not a specie in this simulation!")
        else:
            raise ValueError("Animals can't spawn here at " + str(self.y+1) + "," + str(self.x+1))

    def add_migrator(self, animal):
        """
        Adds a migrating animal to the cell's list containing all the animals.
        The migrator will be checked, soo it's being added to the correct list,
        dependent of species.
        :param animal: class object
        :return: None
        """
        if animal.species == "Herbivore":
            self.herbivore_list.append(animal)
        elif animal.species == "Carnivore":
            self.carnivore_list.append(animal)

    def update_lists(self, specie_list):
        """
        Takes a list, and checks if it contains animals that have died during the annual
        cycle of a cell. It will be checked up after a list containing dead animals.
        :param specie_list: list. A list contain one specie of animals in one cell
        :return: None
        """
        for ani_id in self.dead_animal_list:
            if ani_id in specie_list:
                specie_list.remove(ani_id)
        self.dead_animal_list = []

    def update_migrators(self, map_list):
        """
        Sends the animals to the correct neighbour cells and moves the object to the correct list,
        then gets removed from old landscape/biome list.
        Migrators list is emptied after all the animals have been iterated over.
        :param map_list: Nested list, this contains all the landscape/biomes objects,
        in a sorted way by "coordinates"
        Used to find neighbour cell, which a animal can migrate to.
        :return: None
        """
        if self.tot_migrators:
            x = self.x
            y = self.y

            for migrator in self.tot_migrators:
                migrated = False
                direction = random_number()
                if direction < 0.25:
                    if map_list[y - 1][x].availability:
                        # Go up
                        map_list[y - 1][x].add_migrator(migrator)
                        migrated = True
                elif direction < 0.50:
                    if map_list[y + 1][x].availability:
                        # Go down
                        map_list[y + 1][x].add_migrator(migrator)
                        migrated = True
                elif direction < 0.75:
                    if map_list[y][x + 1].availability:
                        # Go right
                        map_list[y][x + 1].add_migrator(migrator)
                        migrated = True
                elif direction <= 1:
                    if map_list[y][x - 1].availability:
                        # Go left
                        map_list[y][x - 1].add_migrator(migrator)
                        migrated = True

                if migrated:
                    if migrator in self.herbivore_list:
                        self.herbivore_list.remove(migrator)
                    elif migrator in self.carnivore_list:
                        self.carnivore_list.remove(migrator)
            self.tot_migrators = []

    def order_lists(self):
        """
        The list in this cell are being sorted after specifications from task description.
        Herbivores are shuffled at random, for random eating order.
        Carnivores are being sorted after fitness, since the fittest Carnivore eat first.
        (High - Low)
        :return: None
        """
        random.shuffle(self.herbivore_list)
        self.carnivore_list = sorted(self.carnivore_list, key=lambda x: x.fitness, reverse=True)

    def eats_fodder(self, amount):
        """
        This function updates the amount of fodder this cell has, after a Herbivore
        has eaten from this cell.
        :param amount: float. The amount a Herbivore has eaten.
        :return: None
        """
        self.fodder -= amount

    def refresh_land(self):
        """
        This function updates the amount of fodder, when it's called.
        This function is called at the start of the year.
        :return: None
        """
        self.fodder = self.land_id.f_max

    def life_cycle(self):
        """
        This function does the full annual cycle for all animals in the current cell,
        simultaneously. It has a stage check, soo the animals only go trough the steps once per
        year, if the are migrated to another cell.
        The lists are being updated after migrating and culling of animals.
        :return: None
        """
        lists = [self.herbivore_list, self.carnivore_list]
        for list_ani in lists:
            for pet in list_ani:
                if pet.stage == 0:
                    pet.stage = 1
                    pet.feeding_type(self)
        for list_ani in lists:
            total_count = len(list_ani)
            for pet in list_ani:
                if pet.stage == 1:
                    pet.stage = 2
                    pet.birth(self, total_count)
        for list_ani in lists:
            for pet in list_ani:
                if pet.stage == 2:
                    pet.stage = 3
                    pet.migration(self)
            self.update_migrators(self.island_map)
        for list_ani in lists:
            for pet in list_ani:
                if pet.stage == 3:
                    pet.stage = 4
                    pet.ages_weight()
        for list_ani in lists:
            for pet in list_ani:
                if pet.stage == 4:
                    pet.stage = 0
                    pet.death(self)
            self.update_lists(list_ani)
        self.count_stats(lists)

    def count_stats(self, animal_lists):
        """
        This function iterates over the animal-list that been updated from lifecycle.
        It collects data from the objects in the list. Data being collected is fitness, age
        weight and this is collected in separate list for Carnivores and Herbivores.
        The data is only being collected for the current landscape/cell.
        :param animal_lists: list. Takes the current list from lifecycle.
        :return: None
        """
        self.h_fitness_list = []
        self.h_weight_list = []
        self.h_age_list = []

        self.c_fitness_list = []
        self.c_weight_list = []
        self.c_age_list = []
        for animal_list in animal_lists:
            for pet in animal_list:
                if pet.species == "Herbivore":
                    self.h_fitness_list.append(pet.fitness)
                    self.h_weight_list.append(pet.weight)
                    self.h_age_list.append(pet.age)
                elif pet.species == "Carnivore":
                    self.c_fitness_list.append(pet.fitness)
                    self.c_weight_list.append(pet.weight)
                    self.c_age_list.append(pet.age)


class Lowland:
    """
    Contains the attributes of Lowland.
    Max amount of fodder and availability.
    """
    f_max = 800
    availability = True


class Highland:
    """
    Contains the attributes of Highland.
    Max amount of fodder and availability.
    """
    f_max = 300
    availability = True


class Desert:
    """
    Contains the attributes of Desert.
    Max amount of fodder and availability.
    """
    f_max = 0
    availability = True


class Water:
    """
    Contains the attributes of Water.
    Max amount of fodder and availability.
    """
    f_max = 0
    availability = False


class Mountain:
    """
    Contains the attributes of Mountain.
    Max amount of fodder and availability.
    """
    f_max = 50
    availability = True


class Fence:
    """
    Made to rute animals, and to be used as a barrier.
    Contains the attributes of fence.
    Max amount of fodder and availability.
    """
    f_max = 0
    availability = False
