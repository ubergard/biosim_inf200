Formulas used in our simulation
===============================
Related to weight:
------------------------------------------------------

**Animals are born with weight:** |br|
:math:`{\omega}` ~ :math:`N ({\omega}_{weight}` , :math:`{\sigma}_{weight})` |br|
Which is drawn from a Gaussian distribution.

**Yearly weightloss:** |br|
:math:`{\eta}{\omega}` |br|

**Feasting:** |br|
When an animal eats an amount F(fodder), weight increases by |br|
:math:`{\beta}F` |br|


Related to fitness:
---------------------
**Fitness calculation:** |br|
:math:`{\phi}` ={ :math:`q^+(a,a_{\frac{1}{2}}, {\phi}_{age})`
X :math:`q^-({\omega},{\omega}_{\frac{1}{2}}, {\phi}_{weight})`, :math:`{\omega}<= 0` |br|
where
:math:`q^+(x,x_{\frac{1}{2}},{\phi}) =` :math:`{\frac{1}{1+e^{+{\phi}(x-x_{\frac{1}{2}})}}}`
OR :math:`q^-(x,x_{\frac{1}{2}},{\phi}) =` :math:`{\frac{1}{1+e^{-{\phi}(x-x_{\frac{1}{2}})}}}` |br|
note that: :math:`0<= {\phi} <= 1`

Related to migration:
----------------------
**Migration probability:** |br|
:math:`{\mu}{\phi}` |br|
Migrates depending on fitness. Once per year, cannot swim over water. |br|
Animal moves to one out of 4 adjacent cells.

Related to birth:
-----------------
**Birth probability:** |br|
min(1, :math:`{\gamma}` X :math:`{\phi}` X (N - 1)) |br|
N = number of the same species in the same cell. |br|
IF weight is :math:`{\omega} < {\zeta}({\omega}_{weight}` , :math:`{\sigma }_{weight})` or N < 2, |br|
probability = 0


Related to carnivores hunt:
---------------------------
**probability for successful hunt:** |br|
p ={ :math:`{\frac{{\phi}_{carn} - {\phi}_{herb}}{{\Delta}{\phi}_{max}}}`,
if :math:`{\phi}_{carn}<={\phi}_{herb}`
if :math:`0 < {\phi}_{carn} - {\phi}_{herb} < {\Delta}{\phi}_{max}` otherwise |br|
Max = 1, Min = 0 |br|

**Weight gain after hunting:** |br|
When a carnivore hunts and eats successfully, its weight will increase according to this formula  |br|
:math:`{\beta}{\omega}_{herb}` |br|
where :math:`{\omega}_{herb}` is the weight of the herbivore killed.


Related to death:
-----------------
**Death probability:** |br|
:math:`{\omega}(1 - {\phi})` |br|
**Death certainty:** |br|
When :math:`{\omega} = 0` |br|

Parameters used:
-----------------
**The parameters are:** |br|
:math:`{\omega}_{birth}, {\sigma}_{birth}, {\beta}, {\eta}, a_{\frac{1}{2}}, {\omega}_{\frac{1}{2}}`
:math:`{\phi}_{age}, {\phi}_{weight}, {\mu}, {\gamma}, {\zeta}, {\xi}, {\omega}, F, {\Delta}{\phi}_{max}` |br|
The parameters are identical to all the animals of the same species, although they may vary between
herbivores and carnivores. |br|
:math:`{\sigma}` hereby referred to as sigma is different from the one used in the assignment documentation,
the reason for this is that as far as i can tell, Sphinx can only differentiate between this version of sigma and
the sigma notation which is used commonly as summation notation.





.. |br| raw:: html

   <br />