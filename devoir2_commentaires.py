### BONJOUR, ICI JHR ###
### Mes notes et corrections sont encore précédées de trois dièses ###


#Bonjour JH Voici mon code.
#J'ai eu besoin de demander de l'aide pour modifier l'encodage du fichier csv parce que j'avais un message d'erreur comme quoi le fichier n'est pas en utf8


### Bravo!
### Demander de l'aide fait partie du boulot dans ce domaine
### C'est aussi une excellente façon de compléter les apprentissages


# coding: utf-8

import csv

### Je modifie simplement le nom du fichier pour faire rouler ton code sur mon ordi

fichier ="../grants.csv"
f1= open(fichier, encoding='utf-8')
lignes = csv.reader(f1)
next(lignes)

n=0
for ligne in lignes:
### Je déplace ton compteur dans les conditions afin de ne compter que les subventions provenant du FCP (ou CPF in English)
	# n+=1
	if ligne[16] == "CPF - Aid to publishers":
		# n+=1
### J'imprime «n» également, histoires d'avoir un décompte des subventions
		print (ligne, ligne[13], n)
	elif ligne[16]=="CPF - Business Innovation":
		# n+=1
		print (ligne, ligne[13], n)
	elif ligne[16]=="Collective Initiatives":
		# n+=1
		print (ligne, ligne[13], n)

### Bien, mais pourquoi tester toutes ces conditions?
### Ici, il suffisait de chercher «Fonds du Canada pour les périodiques» ou «FCP» dans un même «if»:
### «if "Fonds du Canada pour les périodiques" in ligne[17] or "FCP -" in ligne[17]:»

### En outre, ton code imprime bien la date («ligne[13]»), mais je demandais d'en extraire l'année.