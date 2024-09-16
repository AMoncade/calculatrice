# Importez nos module
import time
import sys

# Définition de nos fonctions mathématiques
def add(a, b):
    return a + b

def sous(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == "0":
        print ("Une division par 0 est impossible")
        sys.exit()
    return a / b

def format():
    print("\n" + "-" * 50 + "\n")
    time.sleep(2)

# Définition de la variable menu
menu = "Opération possible: \n 1. Additioner ( + ) \n 2. Soustraire ( - ) \n 3. Multiplication ( * ) \n 4. Division   ( / ) \n 5. Quitter la calculatrice \n Veuillez choisir votre opération: "

# Créer le méchanisme de la calculatrice
while True:
    op = input(menu)
    if op == "5":
        print ("Merci d'avoir utiliser ma calculatrice :) ")
        break
    num1 = input("Veuillez rentrer votre premier nombre: ")
    if not num1.isdigit():
        print ("Veuillez rentrer seulement des nombres!")
        pass
    num2 = input("Veuillez rentrer votre deuxième nombre: ")
    if not num2.isdigit():
        print ("Veuillez rentrer seulement des nombres!")
        pass
    if op == "1":
        print (add(num1, num2))
        format()
    elif op == "2":
        print (sous(num1, num2))
        format()
    elif op == "3":
        print (mult(num1, num2))
        format()
    elif op == "4":
        print (div(num1, num2))
        format()
    else:
        print ("Veuillez choisir une option valide (Valeur entre 1 et 5)")
        pass

format()






