from math import sqrt

a = 1
b = 4
c = -10


ans1 = ((-b+sqrt((b**2)-4*a*c))/(2*a))
ans2 = ((-b-sqrt((b**2)-4*a*c))/(2*a))
if ((b**2)-4*a*c) < 0:
    print ("existe pas, racine carré négative")
else:
    print (f"{ans1} et {ans2}")