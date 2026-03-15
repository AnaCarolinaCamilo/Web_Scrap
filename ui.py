## importando bibliotecas

import requests
from bs4 import BeautifulSoup
import re


link = str(input('Insira um link sobre o tópico: ')) # recebendo user input 
padrao = r"https:/pt.wikipedia.org/wiki/\w+" # padrão dos links 

if bool(re.fullmatch(padrao,link)): # se o link for válido
    print("Link válido")
    def get_user_link():
        return link

else: # se não for
    print("Link inválido")








