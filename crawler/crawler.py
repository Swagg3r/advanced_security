#!/usr/bin/env python

import os
import re
import sys

switch = 0
if len(sys.argv) > 1:
	if sys.argv[1] == "1":
		switch = 1

#Telechargement des pdf de la cible
url = "http://www.aurelien-mp.fr/index.html"
if switch == 1:
	url = "http://planete.inrialpes.fr/~lauradou/teaching.html"

#os.system('wget -r -A.pdf -A.html -w 5 --random-wait '+url)

#Listage des fichiers pdf telecharges
if switch == 1:
	os.chdir("planete.inrialpes.fr/~lauradou/file/")
else:
	os.chdir("www.aurelien-mp.fr/")

os.system("rm *.txt")


pdffiles = os.listdir('.')
for element in pdffiles:
	if element.find(".pdf") == -1:
		pdffiles.remove(element)


#Convertion des .pdf en .txt
#output2 = os.popen("/home/swagger/git/advanced_sec/pdfminer-20140328/tools/pdf2txt.py intro.pdf").readlines()
print "Liste des fichiers PDF : \n"
for element in pdffiles:
	print element
	if element.find(".pdf") != -1:
		#print ("pdftotext "+element+" -enc UTF-8 "+element+".txt")
		os.system("pdftotext "+element+" -enc UTF-8 "+element+".txt")


#ouvrir les fichiers .txt
contenu_fichier = ""
for element in pdffiles:
	fichier = open(element+".txt", "r")
	contenu_fichier += fichier.read();

#print contenu_fichier

#Creation de la wordlist
contenu_fichier = contenu_fichier.replace("\n"," ")

wordlist = [w for w in re.split('\W+', contenu_fichier) if w]
wordlist = list(set(wordlist)) 

for element in wordlist:
	if len(element) > 26:
		wordlist.remove(element)
	if len(element) < 4:
		wordlist.remove(element)

print "\nIl y a "+str(len(wordlist))+" mots dans la wordlist !\n"

#Listage des fichiers html telecharges
if switch == 1:
	os.chdir("../")
htmlfiles = os.listdir('.')

#ouvrir les fichiers .txt
print "Liste des fichers html :"
contenu_fichier_html = ""
for element in htmlfiles:
	if os.path.isfile(element):
		if element.find('.html') != -1:
			print element
			fichier2 = open(element, "r")
			contenu_fichier_html += fichier2.read()

#print contenu_fichier_html
wordlist2 = [w for w in re.split('\W+', contenu_fichier_html) if w]
wordlist2 = list(set(wordlist2)) 


for element in wordlist2:
	if len(element) > 26:
		wordlist2.remove(element)
	if len(element) < 4:
		wordlist2.remove(element)
	wordlist.append(element)

wordlist = list(set(wordlist)) 

print "\nIl y a maintenant "+str(len(wordlist))+" mots dans la wordlist !\n"