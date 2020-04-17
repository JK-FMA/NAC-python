#!/bin/python3
from ck_17_04_functions import check_list_email, check_email, check_list_db_pass, check_placa, check_any
import os

os.system("clear")

print("###############################################################################")
print("""              _\n             | |\n             | |===( )   //////\n             |_|   |||  | o o|\n                    ||| ( c  )                  ____\n                     ||| \= /                  ||   \_\n                      ||||||                   ||     |\n                      ||||||                ...||__/|-"\n                      ||||||             __|________|__\n                        |||             |______________|\n                        |||             || ||      || ||\n                        |||             || ||      || ||\n------------------------|||-------------||-||------||-||-------\n                        |__>            || ||      || ||\n\n""")
print("		hit any option  to continue \n")
opc = input("[1]Buscar por usuarios e senhas \n[2]Buscar por email \n[3]Buscar placas vazadas \n[4]Buscar qualquer coisa \n")

while opc != "1" and  opc != "2" and opc != "3" and opc != "4":
	opc = input("[1]Buscar por usuarios e senhas \n[2]Buscar por email \n[3]Buscar placas vazadas \n[4]Buscar qualquer coisa \n") 

print("###############################################################################")
if opc == "1":
	senha = input("Informe o usuario que deseja pesquisar ou entao a senha \n")
	if check_list_db_pass(senha) == 1 :
		print ("nenhum dado encontrado")
elif opc == "2":
	
	domain_email = input("Escolha o Dominio do email: \n[1]Hotmail \n[2]Gmail \n[3]outlook \n[4]Para dominos de Empresa \n[5]Todos \n")
	while domain_email != "1" and  domain_email != "2" and domain_email != "3" and domain_email != "4" and domain_email != "5" and domain_email != "6":
		domain_email = input("Escolha o Dominio do email: \n [1]Hotmail \n [2]Gmail \n [3]outlook \n [5]Para dominios da Empresa \n [6]TODOS") 
	print("----------------------------------------------------------")
	if check_list_email(domain_email) == 1 :
		print ("nenhum dado encontrado")
elif opc == "3":
	placas = input("Infome a Placa, ou modelo do carro, ou a cor \n")
	typ = type(placas)
	if isinstance(placas, str):
		placas = placas.lower()
	if check_placa(placas) == 1 :
		print ("nenhum dado encontrado")
elif opc == "4":
	any_tk = input("Informe oque deseja pesquisar e veremos oq achamos \n")
	if check_any(any_tk) == 1 :
		print ("nenhum dado encontrado")

print("###############################################################################")
