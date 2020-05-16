
leaks = { "GMAIL_LEAK":[{"user":"kol@gmail.com", "pass":"12234"}, {"user":"joaozinhogmaer@gmail.com", "pass":"joaogames"}, {"user":"cleito@gmail.com", "pass":"cleitao"}, {"user":"blberico@gmail.com", "pass":"alrecio"}, {"user":"clberico@gmail.com", "pass":"terceiraoirmao"}, {"user":"bruno@gmail.com", "pass":"789mudar"}, {"user":"testador@gmail.com", "pass":"testado"}], "HOTMAIL_LEAK":[{"user":"joao@hotmail.com", "pass":"humanosdemais"}, {"user":"alb@hotmail.com", "pass":"verdadeiroalberico"}, {"user":"jhon@hotmail.com", "pass":"senhamegaforte"}, {"user":"marcos@hotmail.com", "pass":"88923marco"}, {"user":"oliver@hotmail.com", "pass":"matsua@hotmail.com"}, {"user":"ola@hotmail.com", "pass":"adeus2222"}, {"user":"testador@hotmail.com", "pass":"olhaminhasenhasenhsenha"}], "OUTLOOK_LEAK":[{"user":"rafel@outlook.com", "pass":"malwares"}, {"user":"gustavo@outlook.com", "pass":"gustavogrande142"}, {"user":"minhanossa@outlook.com", "pass":"misserioll22"}, {"user":"colora1990@outlook.com", "pass":"testadororiginal"}], "MIX_LEAKS":[{"user":"foole@fiap.com.br", "pass":"oopa231s@"}, {"user":"hotlo@mercado.com", "pass":"mercadolivrecopia"}, {"user":"gustavoss@fiap.com.br", "pass":"koooaao233"}, {"user":"sara@cisco.com.br", "pass":"ciscolegal"}, {"user":"meuamigo@pricai.com", "pass":"Franztake"}, {"user":"bruno@mercado.com" , "pass":"kool"}, {"user":"contato@mercadolibre.com", "pass":"mercadolibre133"}, {"user":"mega_de_loja_de_carros@padaria.com.br", "pass":"koool"}], "PROTON_LEAK":[{"user":"juninho@protonmail.com", "pass":"1234junior"}, {"user":"silvio@protonmail.com", "pass":"1234jacare"}, {"user":"alguemtemgmail@protonmail.com", "pass":"123456hotmail.com"}, {"user":"meunomenaoejhon@protonmail.com", "pass":"umfilmeruim"}, {"user":"goolilao@protonmail.com", "pass":"umabobanda"}]}


def add_leak():
	tag_leak = input("Nome do leak \n").upper()
	resp="S"
	lista = []
	while resp == "S":
		lista.append({"user":input("Informe o usuario \n"), "pass":input("Informe a senha\n")})
		resp = input("Deseja adicionar mais conteudo ?\n[S]im\n[N]ao\n").upper()
	leaks[tag_leak]=lista

	return leaks

def list_leaks():
	for tag,lista in leaks.items():
		print("---------------------------------------------")
		print(tag)
		for resp in lista:
			print("\nUser......... ", resp["user"])
			print("Senha......... ", resp["pass"])
		
def list_leaks_tags():
	for tag,lista in leaks.items():
		print("---------------------------------------------")
		print(tag)
		
def buscar_leaks(query):
	resp = "S"
	while resp == "S":
		resp_found = 0
		if query == "U":
			users = input("Informe o usuario que deseja buscar?\n")
			print("---------------------------------------------")
			for tag,lista in leaks.items():
				for resp in lista:
					if users in resp["user"]:
						print(tag)
						print("User......... ", resp["user"])
						print("Senha......... ", resp["pass"])
						print("---------------------------------------------")
						resp_found = 1
			if resp_found == 0:
				print("Nao foi encontrado nada")
				print("---------------------------------------------")
			resp = input("Deseja continuar?\n[S]im\n[N]ao\n").upper()
		elif query == "S":
			senhas = input("Informe a senha que deseja buscar?\n")
			print("---------------------------------------------")
			for tag,lista in leaks.items():
				for resp in lista:
					if senhas in resp["pass"]:
						print(tag)
						print("User......... ", resp["user"])
						print("Senha......... ", resp["pass"])
						print("---------------------------------------------")
						resp_found=1
			if resp_found == 0:
				print("Nao foi encontrado nada")
				print("---------------------------------------------")
			resp = input("Deseja continuar?\n[S]im\n[N]ao\n").upper()
		elif query == "N":
			tags = input("Informe o nome do leak que deseja buscar?\n")
			print("---------------------------------------------")
			for tag,lista in leaks.items():
				if tag == tags:
					for resp in lista:
						print(tag)
						print("User......... ", resp["user"])
						print("Senha......... ", resp["pass"])
						print("---------------------------------------------")
						resp_found=1
			if resp_found == 0:
				print("Nao foi encontrado nada")
				print("---------------------------------------------")
			resp = input("Deseja continuar?\n[S]im\n[N]ao\n").upper()
		else:
			print("Selecione uma opçao valida")



def alterar_leak():
	resp = "S"
	while resp == "S":
		resp_found = 0
		query = input("O que deseja Alterar ?\n[U]ser\n[S]enha\n[N]ome do leak\n")
		if query == "U":
			for tag,lista in leaks.items():
				print(tag)		
			leak = input("Selecione um dos leaks que deja alterar, ou * para alterar em todos que ele achar\n")
			users = input("Informe o usuario que deseja alterar?\n")
			print("---------------------------------------------")
			for tag,lista in leaks.items():
				for resp in lista:
					if users in resp["user"] and (tag == leak or leak == "*"):
						resp["user"] = input("Informe o novo usuario\n")
						print("alterado com sucesso!")
						print("---------------------------------------------")
						resp_found=1
						
			if resp_found == 0:
				print("Nao foi encontrado nada")
				print("---------------------------------------------")
			resp = input("Deseja continuar?\n[S]im\n[N]ao\n").upper()
		elif query == "S":
			for tag,lista in leaks.items():
				print(tag)		
			leak = input("Selecione um dos leaks que deja alterar, ou * para alterar em todos que ele achar\n")
			senhas = input("Informe a senha que deseja alterar ?\n")
			print("---------------------------------------------")
			for tag,lista in leaks.items():
				for resp in lista:
					if senhas in resp["pass"] and (tag == leak or leak == "*"):
						resp["pass"] = input("Informe a nova senha\n")
						resp_found=1
						print("alterado com sucesso!")
						print("---------------------------------------------")
			if resp_found == 0:
				print("Nao foi encontrado nada")
				print("---------------------------------------------")
			resp = input("Deseja continuar?\n[S]im\n[N]ao\n").upper()
		elif query == "N":
			tags = input("Informe o nome do leak que deseja buscar?\n")
			print("---------------------------------------------")
			for tag,lista in leaks.items():
				if tag == tags:
					new_name=input("Informe o novo nome do Leak \n")
					leaks[new_name] = leaks[tag]
					del leaks[tag]
					print("alterado com sucesso!")
					print("---------------------------------------------")
			
			if resp_found == 0:
				print("Nao foi encontrado nada")
				print("---------------------------------------------")
			resp = input("Deseja continuar?\n[S]im\n[N]ao\n").upper()
		else:
			print("Selecione uma opçao valida")

def deletar_leaks():
	resp = "S"
	while resp == "S":
		resp_found = 0
		query = input("O que deseja Deletar ?\n[U]ser\n[S]enha\n[N]ome do leak\n")
		if query == "U":
			for tag,lista in leaks.items():
				print(tag)		
			leak = input("Selecione um dos leaks que deja deletar, ou * para deletar em todos que ele achar\n")
			users = input("Informe o usuario que deseja deletar?\n")
			print("---------------------------------------------")
			for tag,lista in leaks.items():
				for resp in lista:
					if users in resp["user"] and (tag == leak or leak == "*"):
						lista.remove(resp)
						print("excluido com sucesso!")
						print("---------------------------------------------")
						resp_found = 1
			if resp_found == 0:
				print("Nao foi encontrado nada")
				print("---------------------------------------------")
			resp = input("Deseja continuar?\n[S]im\n[N]ao\n").upper()
		elif query == "S":
			for tag,lista in leaks.items():
				print(tag)		
			leak = input("Selecione um dos leaks que deja deletar, ou * para deletar em todos que ele achar\n")
			senhas = input("Informe a senha que deseja deletar?\n")
			print("---------------------------------------------")
			for tag,lista in leaks.items():
				for resp in lista:
					if senhas in resp["pass"] and (tag == leak or leak == "*"):
						lista.remove(resp) 
						print("excluido com sucesso!")
						print("---------------------------------------------")
						resp_found=1
			if resp_found == 0:
				print("Nao foi encontrado nada")
				print("---------------------------------------------")
			resp = input("Deseja continuar?\n[S]im\n[N]ao\n").upper()
		elif query == "N":
			tags = input("Informe o nome do leak que deseja deletar?\n")
			print("---------------------------------------------")
			for tag,lista in leaks.items():
				if tag == tags:
					del leaks[tag]
					print("excluido com sucesso!")
					print("---------------------------------------------")
					resp_found=1
					break
			if resp_found == 0:
				print("Nao foi encontrado nada")
				print("---------------------------------------------")
			resp = input("Deseja continuar?\n[S]im\n[N]ao\n").upper()
		else:
			print("Selecione uma opçao valida")


