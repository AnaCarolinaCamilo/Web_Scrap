## importando bibliotecas

import requests
from bs4 import BeautifulSoup
import re
from scrapper import Crawler

# função de verificação do link do usuário
def request_user_link() -> str | None:
    link = str(input("Insira um link sobre o tópico: "))
    padrao = r"^https?:\/\/(?:[a-zA-Z]{2,3}\.)?pt\.wikipedia\.org\/wiki\/[^ ]*$"


    if bool(re.fullmatch(padrao, link)):
        print("\nLink válido")

        return link

    else:
        print("\nLink inválido")
        exit()
# iniciação da classe
user_scrapping = Crawler(request_user_link())
# processo de adiquirir o conteúdo da página
user_scrapping.craw()

# menu de operações para o usuário
print("""
      ----- Menu para as operações ----
      Digite 1 para ver os tópicos do artigo
      Digite 2 para ver os links para outros artigos presentes no artigo selecionado
      Digite 3 para ver o nome dos arquivos de imagem do artigo 
      Digite 4 para ver o texto do artigo
      Digite 0 para encerrar
      """)

while True:
    print("\n")
    opr = int(input("Qual vai ser a operação selecionada? "))

    if opr == 1:
        print("\n")
        print(user_scrapping.indexes)
    elif opr == 2:
        print("\n")
        print(user_scrapping.links)
    elif opr == 3:
        print("\n")
        print(user_scrapping.images)
    elif opr == 4:
        print("\n")
        print(user_scrapping.text)
    elif opr == 0:
        print("\n")
        print("Operação encerrada!")
        break
    else:
        print("\n")
        print("Operação inválida! Digite um número válido")

