#!/bin/python3
from funcrion_crypt import *
#pip3 install pycrypt
#sudo apt install python3-pip

S = "S"
while S == "S":
	print("-----------Oque deseja fazer?-----------")
	print("[C]riptografar")
	print("[D]escriptografar")
	print("[E]xit")
	print("----------------------------------------")
	resp = input("").upper()
	while True:
		if resp == "C":
			pwd = input("informe o caminho para o arq\n")
			aes_cpt(chave(),pwd)
			break
		elif resp == "D":
			pwd = input("informe o caminho para o arq\n")
			aes_des(chave(),pwd)
			break
		elif resp == "E":
			exit()
	S=input("Deseja continuar?\n[S]im\n[N]ao\n").upper()
	

#pwd = input("Informe o arq que deseja cryptografar \n")
#pwd = "a.jpg"
#aes_cpt(chave,pwd)
#tmp = input("AAAAAAAA")
#aes_des(chave,pwd)


