import requests
from bs4 import BeautifulSoup


def extract_data_bcv(money: str):
    try:
        website = 'https://www.bcv.org.ve/'

        result = requests.get(website).text

        soup = BeautifulSoup(result, 'lxml')

        tasa = soup.find(
            'div', class_='views-row views-row-1 views-row-odd views-row-first views-row-last row')

        tasa = tasa.find('div', {'id': money})

        tasa = tasa.find('strong').get_text(strip=True)

        return tasa

    except Exception as e:
        print('Oops! That was no valid number.  Try again... ' + str(e))


print(extract_data_bcv('dolar'))
