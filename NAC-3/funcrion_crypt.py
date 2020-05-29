from Crypto.Cipher import AES
import base64
import string
import random
padrao = "1234567891234567"
def aes_cpt(chave,pwd):
	print(chave)
	aes = AES.new(chave, AES.MODE_ECB)
	#pwd=input("informe o caminho para o arq\n")

	with open(pwd, "rb") as var_arquivo:
		data = var_arquivo.read()
	

	data = base64.b64encode(data).decode()
	
	while len(data)%16 != 0:
		data = data + "="

	
	data = base64.b64encode(aes.encrypt(data)).decode()

	with open(pwd, "w") as arquivo:
	    arquivo.write(data)

def aes_des(chave,pwd):
	print(chave)
	aes = AES.new(chave, AES.MODE_ECB)
	#pwd=input("informe o caminho para o arq\n")
	with open(pwd, "r") as var_arquivo:
		data = var_arquivo.read()

	data = base64.b64decode(data)
	data = base64.b64decode(aes.decrypt(data))
	

	with open(pwd, "wb") as var_arquivo:
		var_arquivo.write(data)

def chave():
	print("----------------------------------------------")
	key = input("Informe a chave ou escolha as seguintes opçoes:\n[P]adrao\n[R]adomica\n")
	
	if key == "P":
		key = "1234567891234567"
	elif key == "R":
		range_cha = int(input("informe o tamanho da chave (senao for divisivel que 16 o programa vai aredondar para vc para mais)\n"))
		tmp = range_cha
		while tmp%16 != 0:
			tmp = tmp +1 
		
		key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(tmp))
		print("CHAVE:"+key)
	else:
		if len(key)%16 != 0:
			print("----------------------------------------------")
			
			saida = True
			while saida:
				resp_c = input("Sua chave nao e divisivel por 16. Deseja completar ela ou que o programa a complete por vc ?\n[S]im\n[N]ao\n").upper()
				if resp_c == "S":
					print("----------------------------------------------")
					range_cha = int(input("informe o tamanho da chave (senao for divisivel que 16 o programa vai aredondar para vc para mais)\n"))	
					tmp = range_cha
					while tmp%16 != 0:
						tmp = tmp +1 
					print("----------------------------------------------")
					print("O tamanho da sua senha sera: ",tmp)
					while len(key)%tmp != 0:
						print("----------------------------------------------")
						print("Sua chave atual :"+key)
						temp_c = len(key)
						while temp_c%tmp != 0:
							temp_c = temp_c +1 
						
						print("Faltam:",temp_c-len(key) ,"Caracteres")
						key_add = input("")
						key = key + key_add
						if len(key) > tmp:
							corte = len(key) - tmp
							key = key[:-corte]	
							print("----------------------------------------------")
							print("Sua senha foi ajustada para o tamanho desejado")			
					
					print("----------------------------------------------")
					print("Sua nova cahve e: "+key)
					saida = False
				elif resp_c == "N":			

					temp_c = len(key)
					while temp_c%16 != 0:
						temp_c = temp_c +1 
					temp_c = temp_c-len(key)
					print("----------------------------------------------")
					print("Faltavam:",temp_c ,"Caracteres")
					tmp = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(temp_c))

					key = key + tmp
					print("Sua chave é: " + key)
					saida = False
			
				
			print("----------------------------------------------")
	return key

def bad_random_key():	
	value = [ 16, 24, 32]
	tmp =int(random.randint(0,3))
	
	#print(tmp)
	key = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_letters + string.punctuation) for _ in range(value[tmp]))
	#print("\n\n",len(key),"\n\n")
	return key
