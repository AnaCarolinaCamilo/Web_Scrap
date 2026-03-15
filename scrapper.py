# Objetivos do projeto:

# Primeira parte:
# Perguntar ao usuário qual link do artigo que ele deseja analisar
# utilizando expressões regulares verificar se o link é válido ou não
# verificar se pertence ou não ao domínio pt.wikipedia.org

# Segunda parte:
# Mostrar ao usuário um menu onde seja possível selecionar qual tipo de informação deseja-se extrair da página

# Funcionalidades MINIMAS:
# Listar os tópicos do índice do artigo
# Listas todos os nomes de arquivos de imagens presentes no artigo;
# Listar todos os links para outros artigos da Wikipédia que são citados no conteúdo do artigo.

# classe dos tópicos: class="toc" // uma das classes , class="vector-toc vector-pinnable-element"
# para as imagens pegar pela extensão
# para os links pegar https


# importando bibliotecas
import requests
from bs4 import BeautifulSoup
import re


class Crawler:
    url: str
    indexes: list[str]
    links: list[str]
    images: list[str]
    content: str

    def __init__(self, url: str) -> None:
        self.url = url

    def craw(self) -> None:
        headers = {
            # https://phabricator.wikimedia.org/T400119
            "User-Agent": "CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org) generic-library/0.0"
        }

        response = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        self.content = str(soup)
        print(f"crawling {self.url}...")

        self.__craw_indexes()
        self.__craw_links()
        self.__craw_images()

    def __craw_indexes(self) -> None:
        names = re.findall(
            r'<span class="vector-toc-numb">\d+</span>\s*<span>(.*?)</span>',
            self.content,
            flags=re.DOTALL,
        )
        self.indexes = names

    def __craw_links(self) -> None:
        tags = re.findall(r'<a[^>]+href=["\'](/wiki/[^"\']+)["\'][^>]*>', self.content)
        self.links = ["https://pt.wikipedia.org" + tag for tag in tags]

    def __craw_images(self) -> None:
        images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', self.content)
        images = [image.split("/")[-1] for image in images]
        self.images = images
