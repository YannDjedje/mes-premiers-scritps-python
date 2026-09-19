#Exercice d'application niveau moyen
print("Exercice 1 : Demande 2 nombre à l'utilisateur , convertis-les en entier puis affiche leur somme")
print("--------------------------")
n1= input("Entrez votre premier nombre :")
n1=int(n1)
n2=input("Entrez votre deuxième nombre :")
n2=int(n2)
somme = n1 + n2
text= " la somme de nombre 1 et nombre 2 = {}."
print(text.format(somme))
print("---------------------------------------------------------------------------------------------------------")
print("Exercise 2 : Demande une temperature en celsuis et affiche-la convertie en Fahrenheit(formule:  F = C * 9/5 + 32 ")
C = input("Quel est la temperature")
C = int(C)
F = C * 9/5 + 32
print(" Farhenheit = " , F)
print("----------------------------")
print("Exercice 3 : Demande un nombre et affiche s'il est pair ou impair, en te basant uniquement sur le résultat de % ")
nombre = input("Entrez un nombre :")
nombre=int(nombre)
print("le reste de la divison par 2 est:", nombre%2)
print("----------------------------------------------")
print("Excercie 4 : creer deux variables Bbooléennes à partir d'une comparaison (== et #) entre deux nombre et affiche les")
x = 2
y = 3
egalite = x==y
difference = x!=y
print("l'egalité est :", egalite)
print("la difference est :", difference)
print("---------------------------------------------------------------------------------")
print("Exercice 5 : Demande un prix HT ( hors Taxes) et affiche le prix TTC avec une TVA de 18%")
prixHT= input("Enrez le prixHT :")
prixHT=int(prixHT)
TVA = 18
prixTTC = prixHT + TVA
print("PriXTTC = ", prixTTC)