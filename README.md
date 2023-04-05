# BioSim T07 Augensen & Overgaard
June block assignment Lars Øvergård & Jon Augensen!


# Herbivore & Carnivore population simulator
This is a software for testing different outcomes of a population containing herbivores and 
carnivores.
The user can change parameters for both herbivores and carnivores.
Calling set_animal_parameters for changing 
parameters for herbivore and/or carnivores. Look in documentation for more details.

Different landscapes and map layouts can be tested, this simulator contains parameters for desert, 
water, fence, mountain, highland and lowland. The parameters for these are availability, and 
the amount of food that herbivores can eat. These can be changed by calling set_landscape_parameters
and giving it the land and the new parameters. We have added an extra map example for testing, and 
it's relatively easy to add or change map layouts. Look in documentation for more details.
If the end-user is in need of more landscape-types, these can be added quite easily i e. freshwater. 

When running the simulation, the user can decide whether it wants the graphics window or just 
plain text as output. Use 'vis_years' to tell the simulator to show only years multiplied 
with your desired number. Setting 'vis_years' to 0 will disable graphics window.
Setting 'img_years' to 0 will not save any files, will as default save all images showed.
Setting a number to 'img_years' will automatically save every year multiplied with 'img_years'.

After the simulation is done, it can be set to make a movie with the saved images of the plots.
It will look for images in the folder you wanted it to store it in.
This function has been tested, and you can see the end results in our documentation under 
'simulation shown graphically'.
The video will be stored in a folder named video.
Function: 'make_movie'

The simulation can also return latest year simulated. 
Function: 'year'

The simulation can also return total number of animals at the end of the simulation. 
Function: 'num_animals'

The simulation can also return number of animals per species in island, as dictionary. 
Function: 'num_animals_per_species'


#Features added:
-Fence as barrier "F" (landscape)
-Mountain as biome "M" (landscape)

#Features not added yet:
-Colorbar for population distribution
Modifications for
    -Histograms for age, fitness and weight
    -Colorbar for population distribution


Look at the documentation for using more features not being mentioned here and for getting 
maximum usage of the simulator.

Please make sure to include our image directory, before viewing our documentation.

DISCLAIMER: We do not take any responsibility for third-party software and scripts not working 
with our code.
