from urllib.request import urlopen #IMPORTAR URL ABIERTA
from bs4 import BeautifulSoup
import time
import logging 

logging.basicConfig(filename='minagri.log',
                    filemode='a',format='%(asctime)s : %(levelname)s : %(message)s',
                    datefmt='%d/%m/%y %H:%M:%S',
                    level=logging.INFO)
logging.info('Scraper minagri')
start = time.process_time()

url_scraper = "https://www.minagri.gob.cl/prensa/noticias/"
request_pagina = urlopen(url_scraper) #VAMOS A SOLICITAR LA PÁGINA
pagina_html = request_pagina.read() #SE LEE LA RESPUESTA
request_pagina.close()
html_soup = BeautifulSoup(pagina_html, 'html.parser')# PÁGINA Y ANALIZADOR HTML
contenido_pagina = html_soup.find_all('article', class_="caluga-noticia")
hipervinculo_titulo = html_soup.find_all('div', class_="box-cuerpo-noticia-calugas")

filename = 'minagri.csv'
f = open(filename, 'w', encoding='utf-8')
headers = 'imagen, titulo, descripcion, temas, HIBERVINCUL\n'
f.write(headers)

for cont in hipervinculo_titulo:
    hipervinculo = cont.find('a').get('href')
for contenido in contenido_pagina:
    imagen = contenido.find('img', class_="img-responsive").get('src')
    titulo = contenido.find('h5', class_="titulo-noticia").text
    categoria = contenido.find('a',   rel = "category tag").text
    descripcion = contenido.find('p', class_= "box-cuerpo-noticia").text
    logging.info('Titulo de la noticia: '+str(titulo))
    f.write(titulo+","+descripcion+","+categoria+","+str(imagen)+","+str(hipervinculo))

logging.warning('Cada titulo y fecha esta individualizado por cda noticia')
end = time.process_time()
logging.info('Tiempo total de ejecucion: '+str(end - start))
f.close()      