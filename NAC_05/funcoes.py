#Cadastro
def cadastroElemento(leak, email, senha, val, tag):
	leak[tag] = [email, senha, val]
	
 
#Exibir
def exibirElementos(leak):
	for tag, lista in leak.items():
		mensagem = ("Tag " + tag + " Email " + lista[0]+ " Senha " + lista[1] + " Validade " +lista[2])
	return mensagem

 
#Busca
def buscarElemento(leak, busca):
	busca = busca.upper()
	if leak.get(busca) != None:
		lista = leak.get(busca)
		mensagem = ("Email: " + lista[0]+ ", Senha: " + lista[1] + ", Validade: " +lista[2])
		return mensagem
	else:
		mensagem = "Tag nao encontrada!"
		return mensagem
 
#Alteraca de Validade
def alterarValidade(leak, alteracao, valor):
	alteracao = alteracao.upper()
	if leak.get(alteracao) != None:
		lista = leak.get(alteracao)
		leak[alteracao] = [lista[0], lista[1], valor]
		lista = leak.get(alteracao)
		mensagem = ("Email " + lista[0]+ " Senha " + lista[1] + " Validade " +lista[2])
		return mensagem
	else:
		mensagem = "Tag nao encontrada!"
		return mensagem
 
#deletar
def deletarElemento(leak,deletar):
	if leak.get(deletar) != None:
		del leak[deletar]
		return "deletado com sucesso"
	else:
		return "Tag nao encontrada!"

#persistir
def salvarDados(leak):
	with open("vazamento.csv", "w") as arquivo:
		for tag, lista in leak.items():
			arquivo.write(tag + ";" + lista[0] + ";" + lista[1] + ";" + lista[2])
	return "Arquivo salvo!"
	

def loadDados(dicionario):
	with open("vazamento.csv", "r") as arquivo:
		retorno = arquivo.readlines()
		for linha in retorno:
			lista = linha.split(";")
			dicionario[lista[0]] = [lista[1], lista[2], lista[3]]
