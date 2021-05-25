from time import sleep

from selenium.webdriver import Firefox
from bs4 import BeautifulSoup


# Url inicial de busca
url = "https://www.pensador.com/"

# Realiza a navegação
firefox = Firefox()
firefox.get(url)

# Faz a busca do texto na página
entrada = firefox.find_element_by_css_selector('input[name="q"]')
busca = firefox.find_element_by_css_selector('button[type="submit"]'    )

sleep(1.5)
entrada.send_keys('saudade pablo neruda')
sleep(1.5)
busca.click()

# Obtem uma lista com as poesias encontradas
html = BeautifulSoup(firefox.page_source, 'html.parser')

divs = html.find_all('div', {'class': 'thought-card'})
poesias = [div.find('p').text for div in divs]

# Texto a ser buscar entre as poesias encontradas
texto_procurado = "O maior dos sofrimentos é nunca ter sofrido"

poesia_saudade = ''
for poesia in poesias:
    if texto_procurado in poesia.split('\n')[-1]:
        poesia_saudade += poesia

# Obtem a quantidade de aparições da palavra saudade
quantidade_saudade = poesia_saudade.lower().count('saudade')

# Fecha o navegador
sleep(2)
firefox.quit()

poesia_saudade += f"\n\nPablo Neruda utiliza {quantidade_saudade} vezes" \
            "a palavra saudade(s) para explicar seu significado." \
            "\nBelíssima é a Língua Portuguesa!\n\n"

with open('saudade_pablo_neruda.txt', 'w') as arquivo:
    arquivo.write(poesia_saudade)

print(f"\n\n{poesia_saudade}")