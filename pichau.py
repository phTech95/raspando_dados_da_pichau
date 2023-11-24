import requests
from bs4 import BeautifulSoup


url = 'https://www.pichau.com.br/hardware/placa-de-video'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}


#Filtrando as informações no site, orgonizando as filtagens.
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')



todas_pagina = soup.find('ul', class_='MuiPagination-ul')
ultima = todas_pagina.find_all('li')

nomes_placas = soup.find_all('h2', class_='MuiTypography-root jss78 jss79 MuiTypography-h6')
procurar_precos = soup.find_all('div', class_='jss81')
ultima_pagina = ultima[7].get_text()

lista_marcas = []
for placas in nomes_placas:
    lista_marcas.append(placas.get_text())

precos_lista = []
for precos in procurar_precos:
    precos_lista.append(precos.get_text())

with open('pichau.csv', 'a', newline='', encoding='UTF-8') as f:
    for i in range(int(ultima_pagina)):
        url_page = f'https://www.pichau.com.br/hardware/placa-de-video?page={i}'
        site = requests.get(url_page, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        nomes_placas = soup.find_all('h2', class_='MuiTypography-root jss78 jss79 MuiTypography-h6')
        procurar_precos = soup.find_all('div', class_='jss81')
        for preco, placa in zip(precos_lista, lista_marcas):
            linhas = f'{placa}; {preco} \n'
            f.write(linhas)
            print(linhas)

        print(url_page)








#resultados guardados em variaveis








