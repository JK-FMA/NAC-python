lista_h = ["joao@hotmail.com", "alb@hotmail.com", "jhon@hotmail.com", "marcos@hotmail.com", "oliver@hotmail.com", "matsua@hotmail.com", "ola@hotmail.com", "testador@hotmail.com"]
lista_g = ["kol@gmail.com", "joaozinhogmaer@gmail.com", "cleito@gmail.com", "blberico@gmail.com", "clberico@gmail.com", "bruno@gmail.com", "testador@gmail.com"]
lista_o = ["rafel@outlook.com", "gustavo@outlook.com", "minhanossa@outlook.com", "colora1990@outlook.com"]
lista_p = ["foole@fiap.com.br", "hotlo@mercado.com", "gustavoss@fiap.com.br", "sara@cisco.com.br", "meuamigo@pricai.com", "kolap@fiap.com.br", "bruno@mercado.com", "contato@mercadolibre.com", "mega_de_loja_de_carros@padaria.com.br"]
placas = ["aaa-9999:corola:rreto", "bac-1233:rarati:rreto", "kol-8983:fuscao:preto", "tyr-7089:gol:amerelo", "hhs-7842:corsa:vermelho", "lpi-8854:camaro:vermelho", "des-6312:testador:preto", "mmn-1443:fusca:azul", "cxz-2288:fusca:verde", "avc-6676:parati:verde"]
db_pass = ["admin:admin", "admin:12345", "testador:12345", "kill:Fuscao", "Weer:P4SS0W0RD", "ResSE:11@(!#8", "FMA:@@ww32", "amendin:231020", "Owner:ONADO", "amante_de_fuscao:parati2005"]



def check_any(termo):
	result = 1 
	print("----------------------------------------------------------")
	for lista in lista_p:
		if termo in lista:
			print (" \n email : ", lista, " foi vazado \n ")
			result = 0
			print("----------------------------------------------------------")	
	for lista in lista_h:
		if termo in lista:
			print (" \n email -> ", lista, " foi vazado \n ")
			result = 0
			print("----------------------------------------------------------")		
	for lista in lista_g:
		if termo in lista:
			print (" \n email -> ", lista, " foi vazado \n ")
			result = 0
			print("----------------------------------------------------------")
	for lista in lista_o:
		if termo in lista:
			print (" \n email -> ", lista, " foi vazado \n ")
			result = 0
			print("----------------------------------------------------------")

	for info in placas:
		if termo in info:
			print(" A Placa -> ", info, ", foi vazada ")
			result = 0
			print("----------------------------------------------------------")				
	for info in db_pass:
		if termo in info:
			print (" foi vazado o -> ", info)
			result = 0
			print("----------------------------------------------------------")


def check_placa (termo):
	print("----------------------------------------------------------")
	result = 1
	for info in placas:
		if termo in info:
			print(" A Placa -> ", info, ", foi vazada ")
			result = 0
			print("----------------------------------------------------------")
	return result



def check_list_db_pass(termo):
	print("----------------------------------------------------------")
	result = 1
	for info in db_pass:
		if termo in info:
			print (" O usuario e senha -> ", info ,", foi vazado")
			result = 0
			print("----------------------------------------------------------")
			

	return result

def check_list_email( domain_email):
	
	result = 1
	if domain_email == "1" or  domain_email == "2" or domain_email == "3":
		nome_email = input("Informe nome do email sem o dominio \n").lower()
	elif domain_email == "4":
		nome_email = input("Informe o dominio que deseja pesquisar \n").lower()
	elif domain_email == "6":
		nome_email = input("Digite o termo que dejesa procurar \n").lower()

	print("----------------------------------------------------------")
	if domain_email == "1":
		alvo = nome_email + "@hotmail.com"
		for lista in lista_h:
			if alvo in lista:
				print (" \n email -> ", lista, " foi vazado \n ")
				print("----------------------------------------------------------")
				result = 0
				
			
	elif domain_email == "2":
		
		alvo = nome_email + "@gmail.com"		
		for lista in lista_g:
			if alvo in lista:
				print (" \n email -> ", lista, " foi vazado \n ")
				result = 0
				print("----------------------------------------------------------")
				
	elif domain_email == "3":
		alvo = nome_email + "@outlook.com"
		for lista in lista_o:
			if alvo in lista:
				print (" \n email -> ", lista, " foi vazado \n ")
				result = 0
				print("----------------------------------------------------------")	
				
	elif domain_email == "4":

		
		for lista in lista_h:
			if nome_domain in lista:
				print (" \n email -> ", lista, " foi vazado \n ")
				print("----------------------------------------------------------")
				result = 0
				
	elif domain_email == "5":
		
			alvo = "@" + nome_domain + ".com" 
			for lista in lista_p:
				if alvo in lista:
					print (" \n email -> ", lista, " foi vazado \n ")
					result = 0
					print("----------------------------------------------------------")					
			alvo = nome_email + "@hotmail.com"
			for lista in lista_h:
				if alvo in lista:
					print (" \n email -> ", lista, " foi vazado \n ")
					result = 0
					print("----------------------------------------------------------")
			alvo = nome_email + "@gmail.com"		
			for lista in lista_g:
				if alvo in lista:
					print (" \n email -> ", lista, " foi vazado \n ")
					result = 0
					print("----------------------------------------------------------")		 
			alvo = nome_email + "@outlook.com"
			for lista in lista_o:
				if alvo in lista:
					print (" \n email -> ", lista, " foi vazado \n ")
					result = 0
					print("----------------------------------------------------------")
	return result 



def check_email():
	
	domain_email = input("Escolha o Dominio do email: \n [1]Hotmail \n [2]Gmail \n [3]outlook \n [4]Para dominos de Empresa \n [5]Todos \n")
	while domain_email != "1" and  domain_email != "2" and domain_email != "3" and domain_email != "4" and domain_email != "5" and domain_email != "6":
		domain_email = input("Escolha o Dominio do email: \n [1]Hotmail \n [2]Gmail \n [3]outlook \n [5]Para dominios da Empresa \n [6]TODOS") 
	if check_list_email(nome_email, domain_email) == 1 :
		print ("nenhum dado encontrado")

