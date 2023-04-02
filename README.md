Very simple calculator that takes the equation F = k(q1q2/r^2), and makes a little app out of it. Assumes both charges (q1, q2) are in micro coulombs and distance (r) is in meters. For now the Coulomb Constant is rounded to 8.99x10^9.

However for the time being its only set up for one variation, I.e. only being able to solve for force, and not q2.

It is possible to adjust the script so you can input your own "power" for the charges, like instead of it being hardcoded at micro, you could also do nano, or mili. However I just didnt think about doing that until after I finished the app. If you wanted to do that, you would have to add another entry field asking what the power of the charge is, like -3, -6, -9, etc. Then use that value in place of the -6 in the calulateForce function. One way to do that would be to make another entry field asking for the number, and getting that value from the entry field, then using that value in place of the -6 in the calculateForce function.


****
Needs Physics.PNG in same directory as the script, else if you dont want the custom icon delete lines 17-18 in the script. This is Only if you are downloading the raw code, zip works fine*
****