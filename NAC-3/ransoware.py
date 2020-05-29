#!/bin/python3
from funcrion_crypt import *
pwd = input("informe o caminho para o arq\n")
print("===============================\nPessima escolha meu amigo\n===============================\n")
cont = 0 
while cont < random.randint(10,15):
	key = bad_random_key()
	aes_cpt(key,pwd)
	cont = cont +1 
print("===============================\nJa era meu chapa, nao tem mais como recuperar\n===============================\n")
