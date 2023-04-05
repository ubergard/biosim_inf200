readME
=======

::

    BioSim T07 Augensen & Overgaard
    June block assignment Lars Øvergård & Jon Augensen!

**Herbivore & Carnivore population simulator** |br|
This is a software for testing different outcomes of a population containing herbivores and carnivores. |br|

**The user can:** |br|
change parameters for both herbivores and carnivores. |br|
Calling set_animal_parameters for changing |br|
parameters for herbivore and/or carnivores. Look in documentation for more details. |br|

Different landscapes and map layouts can be tested, this simulator contains parameters for desert, |br|
water, fence, mountain, highland and lowland. The parameters for these are availability, and |br|
the amount of food that herbivores can eat. These can be changed by calling set_landscape_parameters |br|
and giving it the land and the new parameters. We have added an extra map example for testing, and |br|
it's relatively easy to add or change map layouts. Look in documentation for more details. |br|
If the end-user is in need of more landscape-types, these can be added quite easily i e. freshwater. |br|

When running the simulation, the user can decide whether it wants the graphics window or just |br|
plain text as output. Use 'vis_years' to tell the simulator to show only years multiplied |br|
with your desired number. Setting 'vis_years' to 0 will disable graphics window. |br|
Setting 'img_years' to 0 will not save any files, will as default save all images showed. |br|
Setting a number to 'img_years' will automatically save every year multiplied with 'img_years'. |br|

After the simulation is done, it can be set to make a movie with the saved images of the plots. |br|
It will look for images in the folder you wanted it to store it in. |br|
This function has been tested, and you can see the end results in our documentation under |br|
'simulation shown graphically'. |br|
The video will be stored in a folder named video. |br|
Function: 'make_movie'|br|

**The simulation can also return latest year simulated.** |br|
Function: 'year' |br|

**The simulation can also return total number of animals at the end of the simulation.** |br|
Function: 'num_animals' |br|

**The simulation can also return number of animals per species in island, as dictionary.** |br|
Function: 'num_animals_per_species' |br|


**Features added:** |br|
-Fence as barrier "F" (landscape) |br|
-Mountain as biome "M" (landscape) |br|

**Features not added yet:** |br|
-Colorbar for population distribution |br|
**Modifications for:** |br|
-Histograms for age, fitness and weight |br|
-Colorbar for population distribution |br|


Look at the documentation for using more features not being mentioned here and for getting
maximum usage of the simulator. |br|

Please make sure to include our image directory, before viewing our documentation. |br|

**DISCLAIMER: We do not take any responsibility for third-party software and scripts not working**
**with our code.** |br|


.. |br| raw:: html

   <br />