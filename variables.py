#leçon du jour : Les varibales
""""
Nommer une variable :doit commencer par une lettre ou underscores
                      ne pas contenir de caractères spéciaux
                      ne pas contenir d'espaces 
                      utiliser des underscores(_)  
exemple de variable:
                      agePersonne
                      agepersonne
                      age_personne
                      AgePersonne
                      Age_Personne
                      _Age_Personne
type de donnée :    
                    entier numerique (int)
                    nombre flottant (float)
                    chaine de caractère (str)
                    booléen (bool)
""" 
agePersonne = 14            #type entier(int)
agePersonne2 = '25'         #type chaine de caratère (str)
prixHT = 120.46             #type flottant (float)
continuer_partie = False    #type booléen (bool)

print('agePersonne est de :',type(agePersonne))
print("agePersone2 est de :" , type(agePersonne2))
print('prixHT est de :', type(prixHT))
print("continuer_partie est de :",type(continuer_partie))

#type(): permet de determiner le type de variable

print(continuer_partie) #pour afficher le contenu de la varibale
print('continuer_partie') #pour afficher le texte dans la parenthèse

#pour saisir une information, on utilise la fonction "input"
#print permet d'afficher à l'ecran

nom = "David"
print("Bienvenu",nom)
nomJoueur = input("quel est votre nom :")
print('Bonjour joueur', nomJoueur, 'vous etes la Bienvenu dans l\'équipe')

texte="le nombre est {} et l'autre à virgule est {}"
print(texte.format(agePersonne2, prixHT))
"""format : pêrmet de d'inclure la valeur d'une variable dans les acolades
    ou la petie boite
"""
prixHT=input('entrer votre prixHT :')
prixHT=int(prixHT)
prixTTC = prixHT + (prixHT * 20 / 100)
print("prixTTC =", prixTTC)

#int(), float(), bool(), str() : sert à convertir une donnée

#je fais une petite revision de tout ce quenj'ai appris aujourd'hui 
print("--------------------------------------------------------------")
print("                                                              ")
name = "Dick"
age = 29
personne = "votre nom est {} et votre age est {}"
print(personne.format(name , age))
print("    ")
ncarrer = 3
sport = input('enter le nom de sport:')
Ajoutncarrer = input("ajouter un nombre de carriere pour votre sport:")
Ajoutncarrer = int(Ajoutncarrer)
NewAjoutcarrer = Ajoutncarrer + ncarrer
print("          ")
Ajout="vous avez deja {}ans de carrière sportive, vous avez ajouté {}ans à votre carrière, donc vous continuer pour {} ans"
print(Ajout.format(ncarrer ,Ajoutncarrer , NewAjoutcarrer))
print("------------------------------------------------------------")
print("                                                  ")
# je vais affiché le même resultat mais differentes façon d'écrire
print("vous avez deja", ncarrer,"ans de carrière sportive, vous avez ajouté",Ajoutncarrer, "donc vous continuer pour", NewAjoutcarrer, "ans")
