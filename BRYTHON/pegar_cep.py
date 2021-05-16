from bs4 import BeautifulSoup
import requests
import re


class CEP:
    def __init__(self, cep, proxy):
        parametro = { "relaxation":str(cep),"tipoCEP":"ALL", "semelhante":"N" }
        if(proxy == ""):
            url = requests.post("http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm",
                                data=parametro,  timeout=10).text
        else:
            url = requests.post("http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm",
                                data=parametro, proxies=proxy,  timeout=10).text
        self.pagina = BeautifulSoup(url, "lxml")

    def pegar_endereco(self):
        try:
            endereco = ["rua", "bairro", "cidade", "cep", 'estado']
            lista = {}

            for contagem, end in enumerate(self.pagina.find(class_="tmptabela").findAll("td")):
                if(contagem == 2):
                    lista[endereco[contagem]] = re.sub("\xa0", "", end.text).split("/")[0]
                    lista['estado'] = end.text.split("/")[1][:-1]
                else: lista[endereco[contagem]] = re.sub("\xa0", "", end.text)
            return lista
        except Exception as erro: print("NÃO EXISTE O CEP!({})".format(erro));   return False
#
# cep = CEP("60030001", {'https': 'https://192.168.0.254:10082/', 'http': 'http://192.168.0.254:10082/'})
# print(cep.pegar_endereco())
