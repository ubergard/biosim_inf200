# -*- coding: utf-8 -*-

__author__ = 'Jon Augensen & Lars Øvergård, NMBU'
__email__ = 'jon.augensen@nmbu.no / lars.overgard@hotmail.com'

"""
This file contains the class for the animals and classes for different animal species.
"""

from .math_funcs import qua, gaussian_weight, random_number


class Animal:
    """
    Here we create our animal class.
    """

    def __init__(self, params):
        """
        This docstring is related to Animal __init__ Will create an animal based on the parameters
        provided.
        An species object will be added to give it correct attributes and make it eat correctly.
        This object will also remember it's fitness, which will be calculated after it's created,
        it's stage during the annual cycle and which direction it will migrate.
        :param params: dictionary. Contains all the parameters an animal need to be created.
        """
        self.age = params['age']
        self.weight = params['weight']
        self.fitness = 1
        self.species = params['species']
        self.species_id = 0
        self.stage = 0
        self.direction = "None"

        if self.species == "Herbivore":
            self.species_id = Herbivores()

        elif self.species == "Carnivore":
            self.species_id = Carnivores()

        if self.weight < 0:
            raise ValueError("Animals can't have negative weight!")

        if self.age < 0:
            raise ValueError("Animals can't have negative age!")

        if params['age'] == 0:
            self.stage = 2

        self.fitness_update()

    def ages_weight(self):
        """
        Makes an animal increase it's age and lose it annual amount of weight.
        Weight-loss is calculated with it's own weight and class attribute eta.
        :return: None
        """
        self.age += 1
        self.weight -= self.species_id.eta * self.weight

    def feeding_type(self, cell_id):
        """
        This function call for the correct feeding function for the animals.
        This is needed since Herbivores and Carnivores do not eat the same nor the same way.
        :param cell_id: class object. Needed for the feeding functions for the different species.
        :return: None
        """
        self.species_id.feeding(cell_id, self)

    def fitness_update(self):
        """
        Calculates the fitness of an animal, dependent on it's age and weight, and multiple class
        attributes, a_half, phi_age, w_half and phi_weight.
        :return: float. Returns the fitness of an animal
        """
        if self.weight <= 0:
            delta = 0
        else:
            delta = qua(self.age, self.species_id.a_half, self.species_id.phi_age) * \
                    qua(self.weight, self.species_id.w_half, -self.species_id.phi_weight)
        self.fitness = delta
        return delta

    def birth(self, biome_id, animal_count):
        """
        This function will check the probability, if an animals will get a calf. If the animals will
        get a calf is dependent on it's fitness, weight and total amount of animals in their biome.
        When the animal get a calf, it will lose an amount of weight, which will be calculated
        with an attribute xi.
        :param biome_id: class object. Used to call biomes add_animal function
        :param animal_count: int. The total amount of animals of the same species, before animals
        are checked if they get a calf. Will be the same for all animals of the same species in the
        same cell during each year.
        :return: None
        """
        calf_weight = gaussian_weight(self.species_id.w_birth, self.species_id.sigma_birth)
        if self.weight > self.species_id.zeta * \
                (self.species_id.w_birth + self.species_id.sigma_birth) and \
                self.weight > self.species_id.xi * calf_weight:
            if animal_count >= 2:
                birth_prop = min(1.0, self.species_id.gamma *
                                 self.fitness_update() * (animal_count - 1))
                if random_number() <= birth_prop:
                    biome_id.add_animal({'species': self.species_id.name, 'age': 0,
                                         'weight': calf_weight})
                    self.weight -= self.species_id.xi * calf_weight

    def death(self, biomes_id):
        """
        Checks if an animal should be removed from it's cell.
        It will be removed if it's weight is below or is 0, if not there is a random
        chance it will die.
        This chance is checked with a random number compared to it's fitness multiplied with
        attribute omega.
        :param biomes_id: class object. Used to append dead animal to correct list, so it will be
        removed from current list being iterated, after it's done.
        :return: None
        """
        props_death = self.species_id.omega * (1 - self.fitness_update())
        if self.weight <= 0:
            biomes_id.dead_animal_list.append(self)
        elif random_number() <= props_death:
            biomes_id.dead_animal_list.append(self)

    def migration(self, place):
        """
        Determines if the animal will migrate at current year.
        This will be checked with a random number, if the random number is lower then the
        calculation, it will migrate. Dependent on fitness and attribute mu.
        :param place: class object. Used to append the animal to the current cell migrator list.
        :return: Boolean
        """
        if random_number() < self.species_id.mu * self.fitness_update():
            place.tot_migrators.append(self)


class Herbivores:
    """
    This class contains all the attributes to the Herbivores and how they eat.
    """
    w_birth = 8.0
    sigma_birth = 1.5
    beta = 0.9
    eta = 0.05
    a_half = 40
    phi_age = 0.6
    w_half = 10
    phi_weight = 0.1
    mu = 0.25
    gamma = 0.2
    zeta = 3.5
    xi = 1.2
    omega = 0.4
    F = 10
    name = 'Herbivore'

    @staticmethod
    def feeding(cell, animal):
        """
        Simulates a Herbivore eating.
        A Herbivore will eat an amount of fodder yearly, if there is not enough he will eat
        the remaining fodder, and if there is no fodder left, he will eat nothing.
        :param cell: class object. The current cell the Herbivore is in.
        :param animal: class object. The current Herbivore trying to eat.
        :return: None
        """
        food = Herbivores.beta * Herbivores.F
        foods = Herbivores.F
        if foods >= cell.fodder:
            food = Herbivores.beta * cell.fodder
            foods = cell.fodder
        animal.weight += food
        cell.eats_fodder(foods)


class Carnivores:
    """
    This class contains all the attributes to the Carnivores and how they eat.
    """
    w_birth = 6.0
    sigma_birth = 1.0
    beta = 0.75
    eta = 0.125
    a_half = 40
    phi_age = 0.3
    w_half = 4
    phi_weight = 0.4
    mu = 0.4
    gamma = 0.8
    zeta = 3.5
    xi = 1.1
    omega = 0.8
    F = 50
    DeltaPhiMax = 10
    name = 'Carnivore'

    @staticmethod
    def feeding(cell, animal):
        """
        Simulates a Carnivore eating.
        The Carnivores fitness will determined if they will eat their amount meat.
        The probability will be calculated with the lowest Herbivores fitness and their own fitness.
        As long the Carnivore hasn't eaten it's annual amount it will keep trying, while there is
        still Herbivores in the same cell and the Carnivore is fitter, if he eats or not will then
        be checked with a random number.
        :param cell: class object. Gives the current cell the animals is in.
        :param animal: class object. Gives the current animal. Only Carnivores.
        :return: None
        """
        herb_fitness_list = sorted(cell.herbivore_list, key=lambda x: x.fitness)
        food_eaten = 0
        herb_id = 0
        if herb_fitness_list:
            while herb_id < len(herb_fitness_list) and food_eaten < Carnivores.F and \
                    herb_fitness_list and animal.fitness > herb_fitness_list[herb_id].fitness and \
                    cell.herbivore_list:
                eat_prop = ((animal.fitness - herb_fitness_list[herb_id].fitness) /
                            Carnivores.DeltaPhiMax)
                if random_number() < eat_prop:
                    unfit_herb = herb_fitness_list[herb_id]

                    animal.weight += unfit_herb.weight * Carnivores.beta
                    animal.fitness_update()
                    food_eaten += unfit_herb.weight

                    herb_id += 1
                    cell.herbivore_list.remove(unfit_herb)
                else:
                    herb_id += 1
