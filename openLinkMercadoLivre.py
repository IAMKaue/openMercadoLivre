#!python3
# openLinkMercadoLivre - abrir o site da amazon com o objetivo de verificar todos os arquivos correspondentes

import webbrowser, bs4, requests, sys

# Pesquisando no Mercado Livre
print('Pesquisando no mercado livre...')

# Fazendo requisição no site

res = requests.get('https://lista.mercadolivre.com.br/' + ' '.join(sys.argv[1:]))
res.raise_for_status()
html_page = res.text

soupPage = bs4.BeautifulSoup(html_page, 'html.parser')

linkElems = soupPage.select('.ui-search-result__content a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i].get('href'))
