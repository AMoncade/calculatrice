import random
num = random.randint(0,100)
import time


i = 0
print("\nDevinez le nombre mystère entre 0 et 100 en moins de 5 essaies!")
while i < 5:
    guess = int(input("\nDevinez le nombre: "))
    if guess > num:
        print("\nLe nombre est plus petit!")
        print (f"Il te reste {4 - i} essaie")

    elif guess < num:
        print("\nLe nombre est plus grand!")
        print(f"Il te reste {4 - i} essaie")

    else:
        print("Bravo! Tu as deviné le nombre!!")
        break

    i += 1

if "il te reste 0 essaie":
    print ("Dommage... Meilleur chance la prochaine fois!")

