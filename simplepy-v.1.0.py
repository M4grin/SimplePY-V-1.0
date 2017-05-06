import requests
import colorama
import json
from colorama import Fore
colorama.init()
def opt():
	print ("""
 _____ _           _     _____ __ __    _____   ___     ___ 
|   __|_|_____ ___| |___|  _  |  |  |  |  |  | |_  |   |   |
|__   | |     | . | | -_|   __|_   _|  |  |  |_ _| |_ _| | |
|_____|_|_|_|_|  _|_|___|__|    |_|     \___/|_|_____|_|___|
              |_|                                                             
		Codado por M4grin.
	1)Skype Resolver
	2)Consultar CEP
			+ MADE IN BRAZIL +
	""")
opt()
opc=input("[+] Digite a opcao: ")
if opc == '1':
	try:
		skp=input("[+] Skype: ")
		url='http://webresolver.nl/api.php?key=VNV4I-DMJ4L-6MDW8-MBXTO&json&action=resolve&string='+skp
		ir=requests.get(url)
		r=ir.text
		json=json.loads(r)
		if 'true' in r:
			ip=json['ip']
			user=json['username']
			print("""----------------#RESULTADO#----------------""")
			print(Fore.GREEN + "   [*] USUARIO: "+ Fore.WHITE +'',user)
			print(Fore.GREEN +"   [*] IP DO ALVO: " + Fore.WHITE +'',ip)
			print("""----------------#RESULTADO#----------------""")
		else:
			print(Fore.RED +"[-] NAO FOI POSSIVEL ENCONTRAR")
	except Exception as e:
		print("[-]Ouve algum erro: ", e)
elif opc == '2':
	try:
		cep=input("[+] Digite o CEP: ")
		if len(cep) >= 8:
			url='http://viacep.com.br/ws/'+cep+'/json/unicode'
			ir=requests.get(url)
			r=ir.text
			json=json.loads(r)
			cep_resultado=json['cep']
			rua=json['logradouro']
			complemento=json['complemento']
			bairro=json['bairro']
			cidade=json['localidade']
			estado=json['uf']
			ibge=json['ibge']
			print("""----------------#RESULTADO#----------------""")
			print(Fore.GREEN + "   [*] CEP: ",cep_resultado)
			print("   [*] RUA: ",rua)
			print("   [*] COMPLEMENTO: ",complemento)
			print("   [*] BAIRRO: ",bairro)
			print("   [*] CIDADE: ",cidade)
			print("   [*] ESTADO: ",estado)
			print("   [*] IBGE: ",ibge)
			print(Fore.WHITE +"""----------------#RESULTADO#----------------""")
		else:
			print("CEP INVALIDO")
	except Exception as e:
		print("[-]Ouve algum erro: ", e)
else:
	print(Fore.RED + "[-] Nenhuma Opcao Correta foi Selecionada")