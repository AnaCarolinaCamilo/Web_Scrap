# Objetivos do projeto:

# Primeira parte:
# ui.py
# Perguntar ao usuário qual link do artigo que ele deseja analisar
# utilizando expressões regulares verificar se o link é válido ou não
# verificar se pertence ou não ao domínio pt.wikipedia.org
# Mostrar ao usuário um menu onde seja possível selecionar qual tipo de informação deseja-se extrair da página

# Segunda parte:
# scrapper.py
# Funcionalidades MINIMAS:
# Listar os tópicos do índice do artigo
# Listas todos os nomes de arquivos de imagens presentes no artigo;
# Listar todos os links para outros artigos da Wikipédia que são citados no conteúdo do artigo.

# classe dos tópicos: class="toc" // uma das classes , class="vector-toc vector-pinnable-element"
# para as imagens pegar por <img
# para os links pegar a extenção e fazer um link válido


# importando bibliotecas
import requests
from bs4 import BeautifulSoup
import re

# usando conceitos de poo para facilitar o funcionamento da aplicação
class Crawler:
    # definições
    url: str
    indexes: list[str]
    links: list[str]
    images: list[str]
    content: str
    text: str

    # métodos da classe
    @classmethod
    # método de iniciação da classe
    def __init__(self, url: str) -> None:
        self.url = url
    #método para adquirir o conteúdo da página 
    def craw(self) -> None:
        headers = {
            # para adquirir o conteúdo da wipedia é necessário o uso de um agente
            # fonte: https://phabricator.wikimedia.org/T400119
            "User-Agent": "CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org) generic-library/0.0"
        }
        # fazendo o requerimento para acessar o site
        response = requests.get(self.url, headers=headers)
        # usando a biblioteca BeautifulSoup para receber o HTML da página
        soup = BeautifulSoup(response.content, "html.parser")
        self.content = str(soup)
        # confirmação de que a extração do HTML está ocorrendo
        print(f"crawling {self.url}...")
        
        # declarando as funções antes da implementação para que o compilador otimize seu uso
        self.__craw_indexes()
        self.__craw_links()
        self.__craw_images()
        self.__craw_text()

    # função responsável por extrair os índices 
    def __craw_indexes(self) -> None:
        names = re.findall(
            # usando expressões regulares para extrair os nomes
            r'<span class="vector-toc-numb">\d+</span>\s*<span>(.*?)</span>',
            self.content,
            flags=re.DOTALL,
        )
        # atribuindo os nomes adiquiridos ao atributo da classe
        self.indexes = names

    # função responsável por extrair os links para outros artigos
    def __craw_links(self) -> None:
        # usando expressões regulares para extrair apenas os links para outros artigos
        # que são os que contém /wiki/conteúdo do outro artigo
        tags = re.findall(r'<a[^>]+href=["\'](/wiki/[^"\']+)["\'][^>]*>', self.content)
        # atribuindo os links adiquiridos ao atributo da classe
        self.links = ["https://pt.wikipedia.org" + tag for tag in tags]
    
    # função responsável por extrair os nomes dos arquivos de imagem 
    def __craw_images(self) -> None:
        # usando expressões regulares para extrair apenas o nome dos arquivos
        images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', self.content)
        # separando os nomes
        images = [image.split("/")[-1] for image in images]
        # atribuindo os nomes dos arquivos ao atributo da classe
        self.images = images
   
    def __craw_text(self) -> None:
        # usando expressões regulares para adquirir apenas o texto do artigo
        paragraphs = re.findall(r'<p>(.*?)</p>', self.content, re.DOTALL)
        # criando uma lista para o texto limpo
        cleaned_paragraphs = []
        for p in paragraphs:
            # remove qualque tag html presente no texto
            clean_text = re.sub(r'<[^>]+>', '', p)
            # remove referências que estão no texto
            clean_text = re.sub(r'\[\d+\]', '', clean_text)
            # adiciona se não for parágrafos
            if clean_text.strip():
                cleaned_paragraphs.append(clean_text.strip())
        # junta todos os parágrafos com uma quebra de duas linhas
        self.text = '\n\n'.join(cleaned_paragraphs)
    
   

        


