import requests
from bs4 import BeautifulSoup


def extract_data_bcv(money: str):
    try:
        website = 'https://www.bcv.org.ve/'

        result = requests.get(website).text

        soup = BeautifulSoup(result, 'lxml')

        soup = soup.find(
            'div', class_='views-row views-row-1 views-row-odd views-row-first views-row-last row')

        fecha = soup.find(
            'span', class_='date-display-single').get("content").split("T")

        fecha = fecha[0].split("-")

        tasa = soup.find('div', {'id': money})

        tasa = tasa.find('strong').get_text(strip=True)

        return fecha, tasa

    except Exception as e:
        print('Oops! That was no valid number.  Try again... ' + str(e))


print(extract_data_bcv('dolar'))
