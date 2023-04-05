Mapmaker's guide to the gala... err.. Island
==============================================
**Here is a quick "how to" for mapmakers:** |br|

We create the map by using textwrapper, which makes it very easy to configure the map in of itself. |br|
All we need to do is define the landscape types, which we have done in biome.py, assign a letter and color. |br|
to each and every landscape type, and after that just get creative. |br|
The landscape types we have implemented is the following: |br|

Lowland (L) (dark green) |br|
Highland (H) (light green) |br|
Desert (D) (yellow) |br|
Water (W) (blue) |br|
Mountains (M) (grey) |br|
Fence (F) (black) |br|

To create the actual map there is a few things to consider: |br|
The map creation tool is case sensitive. The map needs to have a 'border' of either fence or water. |br|
If saltwater fish is added, you need a fence to contain them to the actual map so they dont pop out of the map. |br|
You need to set a number of rows and columns and stick with it consistently for the entire map. |br|
The program will issue an error if this is not done correctly. |br|

**This will not work:** |br|
    WWWW |br|
    WLW  |br|
    WWWW |br|

**This will work:** |br|
    WWWW |br|
    WLLW |br|
    WWWW |br|

Here we have an example of a quick made world map with only lowland and water: |br|
Because of sphinx i will not include the full map, because some lines will seem longer than others |br|
because of a W takes more space than an L which can be seen on the "This will work" example above. |br|

.. image:: images/world_map.png
    :width: 400


.. |br| raw:: html

   <br />