#exerice d'application niveau facile
print(" voici quelques exercice pour me mettre au top niveau")
print("                         ")
print("Exercice 1: Demande le prénom de l'utilisateur avec 'input' et affiche leur 'Bonjour[prenom]'")
prenom = input("Quel est votre prénom s'il vous plait :")
print("Bonjour", prenom, "!")
print(" ")
print("Exercice 2: crée deux variables a et b avec des nombres, affiche leur somme, difference et produit")
a=12 
b=10
somme= a + b
print("La somme de a + b =", somme)
difference = a - b
print("La difference de a - b = ", difference)
produit = a * b 
print("Le produit de a * b =", produit)
print("  ")
print("Excercice 3: Demande à l'age de l'utilisateur et affiche , 'tu as Xans' en inserant la valeur")
age=input("Quel est votre age? :")
age=int(age)
texte= " tu as {} ans"
print(texte.format(age))
print("   ")
print(" Exercice 4: Crée une variable prix et une autre quantité, affiche le total")
prix=2000
quantite=23
print("Le prix est ", prix, "fcfa et La quantité est de" , quantite, ".")
print("   ")
print("Exercice 5 :Affiche le type de trois variables differentes(un int, un float, un str) avec type()")
numb=14
prixhtTTC= 140.34
nom="dave"
print("numb est de",type(numb))
print("prixhtTTC est de ",type(prixhtTTC))
print("nom est de ",type(nom))