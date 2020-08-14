#Cliente
from funcrion_crypt import *
from socket import *
servidor = "127.0.0.1"
porta = 60011

key = chavea()
while True:
	conexao = socket(AF_INET, SOCK_STREAM)
	conexao.connect((servidor, porta))
	while True:
		msg = input("Digite uma mensagem: ")
	
		conexao.send(bytes(aes_cpt(key,bytes(msg, 'utf-8')), 'utf-8'))
		resposta = conexao.recv(1024)
		resposta = str(aes_des(key,resposta))
		print("Recebemos: ", resposta)
	conexao.close()
