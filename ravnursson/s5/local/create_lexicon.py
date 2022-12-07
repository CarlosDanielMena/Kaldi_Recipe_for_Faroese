#-*- coding: utf-8 -*- 
#############################################################################################
#create_lexicon.py

#Author   : Carlos Daniel Hernández Mena
#Date     : October 20th, 2021
#Location : Reykjavík University

#Uso:

#	$ python3 local/create_lexicon.py <ruta_al_diccionario_de_pronunciacion>

#Ejemplo de uso concreto:

#	$ python3 local/create_lexicon.py $prondict_orig

#This script creates the following Kaldi files:

#	data/local/dict/lexicon.txt
#	data/local/dict/lexiconp.txt

#Notice: This program is intended for Python 3
#############################################################################################
#Imports

import sys
import re
import os

#############################################################################################

#Output files
archivo_out = open("data/local/dict/lexicon.txt",'w')
archivo_out2= open("data/local/dict/lexiconp.txt",'w')

#Handle the input file
archivo_in = open(sys.argv[1],'r')

#############################################################################################
#Load the input file in a hash table and a python list.

max_len = 0
lista_dic=[]
lista_words = []

for linea in archivo_in:
	linea = linea.replace("\n","")
	linea = re.sub('\s+',' ',linea)
	linea = linea.strip()
	
	lista_linea = linea.split(" ")
	word = lista_linea[0]
	lista_linea.pop(0)
	
	trans = " ".join(lista_linea)
	trans = trans +" "

	lista_dic.append(trans)
	lista_words.append(word)

	longitud = len(word)

	#Verifica si es la palabra mas larga
	if longitud > max_len:
		max_len = longitud
	#ENDIF
#ENDFOR

#Add the symbol <UNK>
lista_dic.append("sil ")
lista_words.append("<UNK>")

#############################################################################################
#Arrange the dictionaries in the desired format.

LISTA_LEXICON=[]
LISTA_LEXICON_P=[]

for index in range(0,len(lista_words)):

	word=lista_words[index]
	trans=lista_dic[index]

	num_espacios = max_len - len(word)

	linea_lex = word +"\t"+trans+"\n"
	LISTA_LEXICON.append(linea_lex)

	linea_lexp = word + " "*num_espacios+" 1.0\t"+trans+"\n"
	LISTA_LEXICON_P.append(linea_lexp)
#ENDFOR

#############################################################################################
#Print in the output file
LISTA_LEXICON.sort()
for linea in LISTA_LEXICON:
	archivo_out.write(linea)
#ENDFOR

#############################################################################################
#Print in the output file
LISTA_LEXICON_P.sort()
for linea in LISTA_LEXICON_P:
	archivo_out2.write(linea)
#ENDFOR

#############################################################################################
archivo_in.close()
archivo_out.close()
archivo_out2.close()

