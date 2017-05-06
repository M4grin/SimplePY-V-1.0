#!/usr/bin/python
#CRIADO POR M4GRIN/CREATED BY M4GRIN
#VERSÃO 1.0/VERSION 1.0
#DEIXE OS CREDITOS SE POSSIVEL
import requests #IMPORTO requests
import colorama #IMPORTO colorama
import json #IMPORTO json
from colorama import Fore #DO colorama IMPORTO Fore
colorama.init() # INICIO O colorama
def opt(): #FUNÇÃO DE MOSTRAR AS OPÇÕES E CREDITOS
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
opt() #CHAMO A FUNÇÃO ACIMA
opc=int(input("[+] Digite a opcao: ")) #PEÇO A OPÇÃO COMO UM INTEIRO
if opc == 1: #SE A OPÇÃO ACIMA FOR IGUAL A 1 FAÇA ISSO{
	try: #TENTE FAZER ISSO ABAIXO
		skp=input("[+] Skype: ") #PEDE O SKYPE DO ALVO
		url='http://webresolver.nl/api.php?key=VNV4I-DMJ4L-6MDW8-MBXTO&json&action=resolve&string='+skp #SALVO A API + O SKYPE DO ALVO
		ir=requests.get(url) #VO ATÉ A URL + SKYPE ACIMA COM REQUESTS
		r=ir.text # SALVO OQUE APARECE NA URL NA VARIAVEL R DE RESULTADO
		json=json.loads(r) #TRANSFORMO O RESULTADO EM JSON
		if 'true' in r: #SE APARECER TRUE(true e oque aparece na pagina se encontrar o ip) NO TEXTO DA PAGINA FAÇA ISSO{
			ip=json['ip'] #ARMAZENAR O IP QUE APARECE NO JSON LOAD, NESSA VARIAVEL IP
			user=json['username'] #ARMAZENAR O SKYPE QUE APARECE NO JSON LOAD NA VARIAVEL USER(PODERIA SIMPLESMENTE PUXAR A VARIAVEL skp LA DE CIMA PORÉM OPTEI POR ISSO)
			print("""----------------#RESULTADO#----------------""") #MOSTRA
			print(Fore.GREEN + "   [*] USUARIO: "+ Fore.WHITE +'',user) #MOSTRA COM A COR VERDE E BRANCO
			print(Fore.GREEN +"   [*] IP DO ALVO: " + Fore.WHITE +'',ip) #MOSTRA COM A COR VERDE E BRANCO
			print("""----------------#RESULTADO#----------------""") #MOSTRA
		else: #CASO NÃO FOR ENCONTRADO A STRING true NO IF ACIMA FAZ ISSO {
			print(Fore.RED +"[-] NAO FOI POSSIVEL ENCONTRAR") #MOSTRA
	except Exception as e: #CASO ACONTEÇA ALGUM ERRO NA TENTATIVA(try) ARMAZENO ESSE ERRO NA VARIAVEL e E FAÇO ISSO{
		print(Fore.RED+"[-]Ouve algum erro: ", e) #MOSTRA A MENSAGEM DEPOIS O ERRO
elif opc == 2: #MAIS SE A OPÇÃO FOR 2 FAZ ISSO{
	try: #TENTA FAZER ISSO ABAIXO
		cep=input("[+] Digite o CEP: ") #PEDE O CEP
		if len(cep) >= 8: #SE O TAMANHO DE CEP FOR MAIOR OU IGUAL A 8 FAZ ISSO {
			url='http://viacep.com.br/ws/'+cep+'/json/unicode' #ARMAZENA A API + O CEP PEDIDO NA VARIAVEL url
			ir=requests.get(url) #FAZ ENTRA NA URL ACIMA
			r=ir.text #SALVA OQUE TINHA NA URL ACIMA NESSA VARIAVEL
			json=json.loads(r) #TRANSFORMA A VARIAVEL r QUE TINHA O RESULTADO DO REQUEST EM UM JSON
			cep_resultado=json['cep'] #PEGA O CEP QUE APARECE NO JSON
			rua=json['logradouro'] #PEGA O LOGRADOURO QUE APARECE NO JSON
			complemento=json['complemento'] #PEGA O COMPLEMENTO QUE APARECE NO JSON
			bairro=json['bairro'] #PEGA O BAIRRO QUE APARECE NO JSON
			cidade=json['localidade'] #PEGA A LOCALIDADE QUE APARECE NO JSON
			estado=json['uf'] #PEGA O ESTADO QUE APARECE NO JSON
			ibge=json['ibge'] #PEGA O IBGE QUE APARECE NO JSON
			print("""----------------#RESULTADO#----------------""") #MOSTRA
			print(Fore.GREEN + "   [*] CEP: ",cep_resultado) #MOSTRA NA CORD VERDE O CEP RESULTADO
			print("   [*] RUA: ",rua) #MOSTRA NA CORD VERDE A rua
			print("   [*] COMPLEMENTO: ",complemento) #MOSTRA NA CORD VERDE O complemento
			print("   [*] BAIRRO: ",bairro) #MOSTRA NA CORD VERDE O bairro
			print("   [*] CIDADE: ",cidade) #MOSTRA NA CORD VERDE A cidade
			print("   [*] ESTADO: ",estado) #MOSTRA NA CORD VERDE O estado
			print("   [*] IBGE: ",ibge) #MOSTRA NA CORD VERDE O ibge
			print(Fore.WHITE +"""----------------#RESULTADO#----------------""") #MOSTRA BRANCO
		else: #CASO O CEP N SEJA MAIOR OU IGUAL A 8 FAÇA ISSO{
			print("CEP INVALIDO") #MOSTRA
	except Exception as e: #SE DER UM ERRO NA TENTATIVA (try) ARMAZENA O ERRO NA VARIAVEL e E FAZ ISSO{
		print(Fore.RED+"[-]Ouve algum erro: ", e) #MOSTRA
else: #CASO A OPÇÃO QUE O USUARIO ESCOLHEU NÃO FOR NENHUMA DAS DE CIMA FAÇA ISSO{
	print(Fore.RED + "[-] Nenhuma Opcao Correta foi Selecionada") #MOSTRA
