#!/bin/python3
from ck_17_04_functions import *
import os

os.system("clear")

print("###############################################################################")
print("""              _\n             | |\n             | |===( )   //////\n             |_|   |||  | o o|\n                    ||| ( c  )                  ____\n                     ||| \= /                  ||   \_\n                      ||||||                   ||     |\n                      ||||||                ...||__/|-"\n                      ||||||             __|________|__\n                        |||             |______________|\n                        |||             || ||      || ||\n                        |||             || ||      || ||\n------------------------|||-------------||-||------||-||-------\n                        |__>            || ||      || ||\n\n""")
print("		hit any option  to continue \n")
resp = "S"

while resp == "S":
	opc = input("[1]Buscar por usuarios\n[2]Buscar por senhas \n[3]Bucar por Leaks\n[4]Exbir Lista Geral\n[5]Exibir lista dos Leaks\n[6]Gereciar Lista\n")

	while opc != "1" and  opc != "2" and opc != "3" and opc != "4" and opc != "5" and opc != "6":
		opc = input("[1]Buscar por usuarios\n[2]Buscar por senhas \n[3]Bucar por Leaks\n[4]Exbir Lista Geral\n[5]Exibir lista dos Leaks\n[6]Gereciar Lista\n") 

	print("###############################################################################")
	if opc == "1":
		buscar_leaks("U")

	elif opc == "2":
		buscar_leaks("S")
	elif opc == "3":
		buscar_leaks("N")
	elif opc == "4":
		list_leaks()
		print("---------------------------------------------")
	elif opc == "5":
		list_leaks_tags()
		print("---------------------------------------------")
	elif opc == "6":
		select = input("Oque deseja fazer com os leaks ?\n[A]lterar\n[C]adastrar\n[D]eletar\n").upper()
		if select == "A":
			alterar_leak()
		elif select == "C":
			add_leak()
		elif select == "D":
			deletar_leaks()	
		
		#resul = add_leak()
		#list_leaks()

		#buscar_leaks()
		#alterar_leak()
		#deletar_leaks()
		list_leaks()
	
	resp = input("\n\nDeseja Continuar?\n[S]im\n[N]ao\n")
		
	
	print("###############################################################################")
