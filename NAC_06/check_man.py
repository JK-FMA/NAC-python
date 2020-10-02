import hashlib
from datetime import datetime
import threading

 

pathsave=""
hashsaves=[]
bkps1=[]

def md5checksum(fname):
	
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)

	return hash_md5.hexdigest()




def copy_n(fname,pathsave):
	
	bkps=pathsave+fname.split("/")[-1]
	bkps1.append(bkps)

	f = open(fname, "r")
	fn = open(bkps, "a")

	for lines in f:
		fn.write(lines)

	f.close()
	fn.close()


def replace(origin, dest):
	org = open(origin, "r")
	fn = open(dest, "w")

	for lines in org:
		fn.write(lines)

	org.close()
	fn.close()

def monitor(files, fhash, bkpid):
	while True:	
		if md5checksum(str(files)) != fhash:
			
			
			replace(bkps1[bkpid],str(files))
			#print(bkps1[bkpid],str(files), fhash)
			print("O arquivo :"+str(files)+" foi alterado e realterado para a versao anterior as :"+str(datetime.now()))
			



def monitorL(flist, arrayhash):
	while True:
		for fils in flist:
			if md5checksum(str(fils)) != arrayhash[flist.index(fils)]:
				replace(str(fils), bkps1[flist.index(fils)])
				print("O arquivo :"+str(fils)+" foi alterado e realterado para a versao anterior as :"+str(datetime.now()))


pathsave = input("Informe o caminho para o diretorio de bkp (ele deve estar vazio)\n")

fname = input("informe caminho para os arq ou uma lista com os arq mas com ',' separando os arq\n")

if "," in fname:
	fname = fname.split(",")
	print(fname)
	for files in fname:
		copy_n(files,pathsave)
		hashsaves.append(md5checksum(files))
		
		x = threading.Thread(target=monitor, args=(files,hashsaves[fname.index(files)], bkps1.index(bkps1[fname.index(files)]),))
		x.start()

	
else:
	copy_n(fname,pathsave)
	hashs =md5checksum(fname)
	monitor(fname, hashs, 0)



#result = md5checksum(fname)


