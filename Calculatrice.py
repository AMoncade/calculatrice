#Importer nos fonctions nécéssaires au script
import time


#Assigner mes variables principales
menu = f"Voici les opérations possibles: \n 1. Addition \n 2. Soustraction \n 3. Multiplication \n 4. Division \n 5: Quitter la calculatrice"


while True:
    num1 = (input("\nVeuillez entrez votre premier nombre: "))
    if not num1.isdigit():
        print("\nVeuillez seulement rentrez des nombres")
        pass
    else:
        num2 = (input("Veuillez entrez votre deuxième nombre: "))
        if not num2.isdigit():
            print("\nVeuillez seulement rentrez des nombres")
            pass
        else:
            print(menu)
            var = (input("Veuillez rentrez le nombre pour votre équation: "))
            if var == "5":
                print ("\nMerci d'avoir utiliser ma calculatrice :) ")
                break
            elif var == "1":
                print(f"\n = {float(num1) + float(num2)}")
            elif var == "2":
                print(f"\n = {float(num1) - float(num2)}")
            elif var == "3":
                print(f"\n = {float(num1) * float(num2)}")
            elif var == "4":
                if num2 == "0":
                    print ("\nIl est impossible de diviser par 0")
                else:
                    print(f"\n = {float(num1) / float(num2)}")
            else:
                print("\nVeuillez rentrez une opération valide")
                pass
    print("_"*50)
    time.sleep(2)















