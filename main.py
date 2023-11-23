import requests
from bs4 import BeautifulSoup
import csv


URL_BASE = 'https://www.larvf.com/domaines/alpha/a'

URL_TESTE = 'https://www.larvf.com/,domaine-de-l-a,10476,403953.asp'

def extrair_url(url):
    resposta = requests.get(url)
    parsing = BeautifulSoup(resposta.content, 'html.parser')
    lista_desordenada = parsing.find('ul', class_='DomainList-domains')
    urls = lista_desordenada.find_all('a')
    lista = []
    for links in urls:
        lista.append(links)
        print(lista)





def extrair_dados(url):
    resposta = requests.get(url)
    parsing = BeautifulSoup(resposta.content, 'html.parser')
    span = parsing.find('span', class_='Article-metaValue')

    # Verifique se o span foi encontrado
    if span:
        # Obtenha o texto dentro do span
        nome_produtor = span.get_text(strip=True)
        print(f'região: {nome_produtor}')
    else:
        print('Span não encontrado.')

    LISTA = []

    html_subregiao = '<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Libourne</font></font>'
    parsing_html = BeautifulSoup(html_subregiao, 'html.parser')
    print(f'subregião: {parsing_html.get_text()}')

    html_proprietario = '<font style="vertical-align: inherit;">Christine e Stéphane Derenoncourt</font>'
    parsing_proprietario = BeautifulSoup(html_proprietario, 'html.parser')
    print(f'nome: {parsing_proprietario.get_text(strip=True)}')

    garrafas_html = '<font style="vertical-align: inherit;">40.000</font>'
    numeros_garrafa = BeautifulSoup(garrafas_html, 'html.parser')
    print(f'numeros de garrafas por ano: {numeros_garrafa.get_text(strip=True)}')

    area_html = '<font style="vertical-align: inherit;">12 hectares</font>'
    area_plantada = BeautifulSoup(area_html, 'html.parser')
    print(f'Área plantada: {area_plantada.get_text(strip=True)}')

    html_colheita = '<font style="vertical-align: inherit;">Manual</font>'
    metodo_colheita = BeautifulSoup(html_colheita, 'html.parser')
    print(f'metodo de colheita: {metodo_colheita.get_text(strip=True)}')

    html_compra_uva = '<font style="vertical-align: inherit;">Não</font>'
    compra_de_uvas = BeautifulSoup(html_compra_uva, 'html.parser')
    print(f'compra de uvas: {compra_de_uvas.get_text(strip=True)}')

    merlot = '<font style="vertical-align: inherit;">Merlot</font>'
    merlot1 = BeautifulSoup(merlot, 'html.parser')
    cabernetfranc = '<font style="vertical-align: inherit;">Cabernet franc</font>'
    cabernetfranc2 = BeautifulSoup(cabernetfranc, 'html.parser')
    print(f'castas tintas: {merlot1.get_text(strip=True)} {cabernetfranc2.get_text(strip=True)}')


    html_casta = '<font style="vertical-align: inherit;">Chardonnay</font>'
    casta_branca = BeautifulSoup(html_casta, 'html.parser')
    print(f'castas brancas: {casta_branca.get_text(strip=True)}')

    email_html = '<font style="vertical-align: inherit;">contato@domainedela.com</font>'
    email = BeautifulSoup(email_html, 'html.parser')
    print(f'email: {email.get_text(strip=True)}')


    telefone_html = '<font style="vertical-align: inherit;">Tel: 05 57 24 92 43 </font>'
    telefone = BeautifulSoup(telefone_html, 'html.parser')
    print(f'telefone: {telefone.get_text(strip=True)}')












def csv(nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        pass




extrair_dados(URL_TESTE)

""""
    - Nome do Produtor
    - A região
    - A sub-região
    
    - Nombre de bouteilles par an
    - Superfície plantada (apenas o primeiro número, não a subdivisão)
    - Modo de vendange
    - Âge moyen des vignes
    - Cépages rouges (sem porcentagens)
    - Cépages blancs (sem porcentagens)
    - Email address
    - Address

"""
