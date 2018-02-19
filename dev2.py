#Bonjour JH Voici mon code.
#J'ai eu besoin de demander de l'aide pour modifier l'encodage du fichier csv parce que j'avais un message d'erreur comme quoi le fichier n'est pas en utf8






# coding: utf-8

import csv

fichier ="grants.csv"
f1= open(fichier, encoding='utf-8')
lignes = csv.reader(f1)
next(lignes)

n=0
for ligne in lignes:
	n+=1
	if ligne[16] == "CPF - Aid to publishers":
		print (ligne, ligne[13])
	elif ligne[16]=="CPF - Business Innovation":
		print (ligne, ligne[13])
	elif ligne[16]=="Collective Initiatives":
		print (ligne, ligne[13])

