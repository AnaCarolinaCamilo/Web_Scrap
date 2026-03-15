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
from ui import get_user_link
import requests
from bs4 import BeautifulSoup
import re


res = requests.get(get_user_link)
soup = BeautifulSoup(res.content,"html.parser")
print(f"Scrapping: {get_user_link}")
print(res)

# listando os tópicos do índice do artigo

artigo_indices = re.findall(r'<div+?class="/^[a-zA-Z0-9_-]+$/+toc+/^[a-zA-Z0-9_-]+$/"',soup)

nome_indices = []

for indices in artigo_indices:

    nome = re.findall(r'<div.+?class="vector-toc-text".+?span.+?</div>',indices)

    nome_indices.append(nome)

# listando todos os links para outros artigos do wit=kipedia 

artigo_links = re.findall(r'<a.+?/^[a-zA-Z0-9_-]+$/ href"/^[a-zA-Z0-9_-]+$/" title="/^[a-zA-Z0-9_-]+$/">/^[a-zA-Z0-9_-]+$/</a>',soup)
# para conseguir links válidos é necessário pergar o href e inserir em um padrão "https://pt.wikipedia.org"
for link in artigo_links:
    if link['href'].find("/wiki/") == -1:
        continue
    link = "https://pt.wikipedia.org"+link['href']
    break

print(link)

# listando todos as imagens presentes no artigo 

        



           
    





