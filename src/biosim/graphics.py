
__author__ = 'Jon Augensen & Lars Øvergård, NMBU'
__email__ = 'jon.augensen@nmbu.no / lars.overgard@hotmail.com'

"""
Parts of this code is developed by Copyright (c) 2021 Hans Ekkehard Plesser / NMBU,
and is used to display our simulation.
This file contains the class for the plots window and it's features.
"""

import matplotlib.pyplot as plt
import os


class Plot:
    """
    Here we create plots for visualization
    """
    def __init__(self, map_layout, vis_years, img_years, img_fmt, img_dir, img_base, hist_specs,
                 ymax_ani, cmax_ani):
        """
        This docstring belongs to Plot __init__ it creates the plot layout and creates and adds
        the simulation map.
        Removes all axes, adds text and creates a folder for images, if asked for and there is
        no folder with the given name.
        :param map_layout: string. Contains the map layout.
        :param img_years: int. Tells which years that will be saved of the plots.
        :param img_fmt: string. The format to the images being saved.
        :param img_dir: string. Gives which folder the images are saved to.
        :param img_base: string. Gives the name, the images will be saved with.
        """
        self.map = map_layout
        self.vis_years = vis_years
        self.img_years = img_years
        self.img_fmt = img_fmt
        self.img_dir = img_dir
        self.img_base = img_base
        self.hist_specs = hist_specs
        self.ymax_counter = ymax_ani
        self.color_max_ani = cmax_ani
        self.years_saved = 0

        fig = plt.figure(constrained_layout=True)
        gs = fig.add_gridspec(3, 3)
        # Subplots
        self.ax_years_counted = fig.add_subplot(gs[0, 0])
        self.ax_map = fig.add_subplot(gs[0, 1])
        self.ax_map.set_title("Island map")
        self.ax_pop_counted = fig.add_subplot(gs[0, 2])
        self.ax_carni_distribution = fig.add_subplot(gs[1, 0])
        self.ax_carni_distribution.set_title("Carnivore distribution")
        self.ax_animal_counter = fig.add_subplot(gs[1, 1])
        self.ax_animal_counter.set_title("Animal Counter")
        self.ax_herbi_distribution = fig.add_subplot(gs[1, 2])
        self.ax_herbi_distribution.set_title("Herbivore distribution")
        self.ax_age = fig.add_subplot(gs[2, 0])
        self.ax_age.set_title("Age")
        self.ax_fitness = fig.add_subplot(gs[2, 1])
        self.ax_fitness.set_title("Fitness")
        self.ax_weight = fig.add_subplot(gs[2, 2])
        self.ax_weight.set_title("Weight")

        self.path_name = ''

        axes = [self.ax_map, self.ax_years_counted, self.ax_carni_distribution, self.ax_pop_counted,
                self.ax_herbi_distribution]

        for ax in axes:
            ax.set_xticks([])
            ax.set_yticks([])

        #                   R    G    B
        rgb_value = {'W': (0.0, 0.0, 1.0),  # blue
                     'L': (0.0, 0.6, 0.0),  # dark green
                     'H': (0.5, 1.0, 0.5),  # light green
                     'M': (0.5, 0.5, 0.5),  # light green
                     'F': (0.1, 0.1, 0.1),  # Dark brown
                     'D': (1.0, 1.0, 0.5)}  # light yellow

        map_rgb = [[rgb_value[column] for column in row] for row in self.map.splitlines()]

        self.ax_map.imshow(map_rgb)
        self.ax_map.set_xticks([])
        self.ax_map.set_yticks([])

        self.y_max_for_animals = 0
        self.years_total = 1

        self.herbivore_count = 0
        self.carnivore_count = 0

        self.ax_years_counted.axis('off')
        self.timer = 'Year: {:5d}'
        self.txt_year = self.ax_years_counted.text(0.5, 0.5, self.timer.format(0),
                                                   horizontalalignment='center',
                                                   verticalalignment='center',
                                                   transform=self.ax_years_counted.transAxes)

        self.ax_pop_counted.axis('off')
        self.population = 'Total population: {:5d}'
        self.txt_pop = self.ax_pop_counted.text(0.5, 0.5, self.population.format(0),
                                                horizontalalignment='center',
                                                verticalalignment='center',
                                                transform=self.ax_pop_counted.transAxes)

        if self.ymax_counter:
            self.ax_animal_counter.set_ylim(0, self.ymax_counter)
        if self.hist_specs:
            print("This simulator does not support modification of histograms yet!")
        if self.color_max_ani:
            print("This simulator does not support modification of colormap yet!")

        if self.img_years % self.vis_years != 0:
            raise ValueError("'img_years' must be a multiple of 'vis_years'!")

        if self.img_years and self.img_years != 0 and self.img_dir:
            if os.path.isdir('../' + self.img_dir + '/') and self.img_dir != ".":
                for f in os.listdir('../' + self.img_dir + '/'):
                    os.remove(os.path.join('../' + self.img_dir + '/', f))
                self.path_name = '../' + self.img_dir + '/'
            elif not os.path.isdir('../' + self.img_dir + '/') and self.img_dir != ".":
                os.mkdir('../' + self.img_dir + '/')
                self.path_name = '../' + self.img_dir + '/'
            if self.img_dir == ".":
                self.path_name = ''

    def update_animal_counter(self, years):
        """
        Updates the animal counter, with both herbivores and carnivores.
        Adds a point for each species, each time the function is called. (x, y) is taken from the
        year and total amount of animal of one specie.
        :param years: int. The current year being displayed.
        :return: None
        """
        self.ax_animal_counter.plot(years, self.herbivore_count, 'go', markersize=4, alpha=0.5)
        self.ax_animal_counter.plot(years, self.carnivore_count, 'ro', markersize=4, alpha=0.5)

    def update_distribution(self, herbi_distribution, carni_distribution):
        """
        Updates the distribution maps and show a color which tells how many animals there is at a
        given cell. These color are taken from dictionary with rgb values.
        :param herbi_distribution: list. A nested list with all total amount of herbivores at
        a current cell.
        :param carni_distribution: list.A nested list with all total amount of carnivores at
        a current cell.
        :return: None
        """
        herbivore_range = [5, 20, 60, 100, 150, 200]
        carnivore_range = [2, 10, 20, 30, 40, 50]
        herbivore_distribution = self.adjust_distribution(herbi_distribution, herbivore_range)
        carnivore_distribution = self.adjust_distribution(carni_distribution, carnivore_range)
        rgb_value_h = {0: (1.0, 1.0, 1.0),  # white
                       1: (0.0, 1.0, 0.0),  # green 20%
                       2: (0.0, 0.8, 0.0),  # green 40%
                       3: (0.0, 0.6, 0.0),  # green 60%
                       4: (0.0, 0.4, 0.0),  # green 80%
                       5: (0.0, 0.2, 0.0)}  # green 100%
        map_rgb_h = [[rgb_value_h[column] for column in row] for row in herbivore_distribution]

        rgb_value_c = {0: (1.0, 1.0, 1.0),  # white
                       1: (1.0, 0.0, 0.0),  # red 20%
                       2: (0.8, 0.0, 0.0),  # red 40%
                       3: (0.6, 0.0, 0.0),  # red 60%
                       4: (0.4, 0.0, 0.0),  # red 80%
                       5: (0.2, 0.0, 0.0)}  # red 100%
        map_rgb_c = [[rgb_value_c[column] for column in row] for row in carnivore_distribution]

        self.ax_herbi_distribution.imshow(map_rgb_h)
        self.ax_carni_distribution.imshow(map_rgb_c)

    def update_histograms(self, h_age, c_age, h_fit, c_fit, h_weg, c_weg):
        """
        Updates all the histograms.
        First it clears all the histograms, then updates the titles and then applies all the values.
        :param h_age: list. A list with all ages for herbivores.
        :param c_age: list. A list with all ages for carnivores.
        :param h_fit: list. A list with all fitness' values for herbivores.
        :param c_fit: list. A list with all fitness' values for carnivores.
        :param h_weg: list. A list with all weights for herbivores.
        :param c_weg: list. A list with all weights for carnivores.
        :return: None
        """
        self.ax_age.cla()
        self.ax_age.set_title("Age")
        self.ax_age.hist(h_age, 20, color='g', alpha=0.5)
        self.ax_age.hist(c_age, 20, color='r', alpha=0.5)

        self.ax_fitness.cla()
        self.ax_fitness.set_title("Fitness")
        self.ax_fitness.hist(h_fit, 20, color='g', alpha=0.5)
        self.ax_fitness.hist(c_fit, 20, color='r', alpha=0.5)

        self.ax_weight.cla()
        self.ax_weight.set_title("Weight")
        self.ax_weight.hist(h_weg, 20, color='g', alpha=0.5)
        self.ax_weight.hist(c_weg, 20, color='r', alpha=0.5)

    @staticmethod
    def adjust_distribution(map_distribution, h_or_c_range_list):
        """
        Needed to give update_distribution function values to update the distribution map with
        colors specified at an amount of animals.
        :param map_distribution: list. A nested list with the amount of animals of a species at
        all cells.
        :param h_or_c_range_list: list. Decides at what levels the color will be set at.
        :return: list. A nested list, with values to update the distribution map with colors.
        """
        y_len = len(map_distribution)
        x_len = len(map_distribution[0])
        for m in range(y_len):
            for n in range(x_len):
                if map_distribution[m][n] < h_or_c_range_list[0]:
                    map_distribution[m][n] = 0
                elif map_distribution[m][n] < h_or_c_range_list[1]:
                    map_distribution[m][n] = 1
                elif map_distribution[m][n] < h_or_c_range_list[2]:
                    map_distribution[m][n] = 2
                elif map_distribution[m][n] < h_or_c_range_list[3]:
                    map_distribution[m][n] = 3
                elif map_distribution[m][n] < h_or_c_range_list[4]:
                    map_distribution[m][n] = 4
                else:
                    map_distribution[m][n] = 5

        return map_distribution

    def update_plot(self, data_list):
        """
        Used to update plots to show current years data. Updates year, population, distribution of
        species, and histograms of age, fitness and weight for herbivores and carnivores.
        If given, it will also store a picture of the plot after it is updated, in a given folder.
        :param data_list: list. This list contains all the data needed for updating all the plots,
        with dynamic plots.
        :return: None
        """
        self.years_total = data_list[0]
        self.herbivore_count = data_list[1]
        self.carnivore_count = data_list[2]
        herbi_distribution = data_list[9]
        carni_distribution = data_list[10]

        self.txt_year.set_text(self.timer.format(self.years_total))
        self.txt_pop.set_text(self.population.format(self.herbivore_count + self.carnivore_count))
        self.update_distribution(herbi_distribution, carni_distribution)
        self.update_animal_counter(self.years_total)
        self.update_histograms(data_list[4], data_list[7], data_list[3], data_list[6], data_list[5],
                               data_list[8])
        plt.draw()
        plt.pause(1)
        if self.img_years and self.years_total % self.img_years == 0 and self.img_years != 0 and \
                self.img_dir and self.img_base:
            if self.vis_years == 0:
                return
            plt.savefig(self.path_name + self.img_base + "_0000" +
                        str(self.years_saved) + "." + self.img_fmt)
            self.years_saved += 1
