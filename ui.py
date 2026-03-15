## importando bibliotecas

import requests
from bs4 import BeautifulSoup
import re


def request_user_link() -> str | None:
    link = str(input("Insira um link sobre o tópico: "))
    padrao = r"https:/pt.wikipedia.org/wiki/\w+"

    if bool(re.fullmatch(padrao, link)):
        print("Link válido")

        return link

    else:
        print("Link inválido")
