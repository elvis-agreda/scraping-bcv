from bs4 import BeautifulSoup

def tasa():
    import requests
    # Url destino
    url = "http://www.bcv.org.ve"

    # Petición
    requests = requests.get(url)

    # Tomamos el requests, lo parseamos a html para obtener un tipo de dato soup
    soup = BeautifulSoup(requests.content, "html.parser") 
    
    # status_code 200 es OK, en caso contrario web no disponible he imprimimos mensaje y codigo de error
    if requests.status_code == 200:      
        contenList = []

        for contenido in soup.find_all('strong')[4]: #<strong> del arbol que nos interesa
            dato = contenido
            contenList.append(dato.strip())
        
        tasa = contenList[0].replace(',','.')

        return(float(tasa))
    
    else:
        return("Error de conexión: Código ", requests.status_code)
