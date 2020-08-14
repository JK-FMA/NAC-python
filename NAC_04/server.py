#Server
from funcrion_crypt import *
from socket import *
servidor = "127.0.0.1"
porta = 60011

key = chavea()

conexao = socket(AF_INET, SOCK_STREAM)
conexao.bind((servidor, porta))
conexao.listen(2)

print("Esperando Usuario...")
while True:
	con, cliente = conexao.accept()
	print("Conectado com: ", cliente)
	while True:
		msg_recebida = con.recv(1024)
		print(msg_recebida.decode())
		resposta = aes_des(key,msg_recebida.decode())
		print("Recebemos: ", resposta)
		msg_enviada = bytes(input("Digite uma mensagem: "), 'utf-8')
		conexao.send(bytes(aes_cpt(key,msg)))
		con.send(msg_enviada)
	con.close()
