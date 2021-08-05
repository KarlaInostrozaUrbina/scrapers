from urllib.request import urlopen #IMPORTAR URL ABIERTA
from bs4 import BeautifulSoup
import time
import logging 

logging.basicConfig(filename='portaldelagro.log',
                    filemode='a',format='%(asctime)s : %(levelname)s : %(message)s',
                    datefmt='%d/%m/%y %H:%M:%S',
                    level=logging.INFO)
logging.info('Scraper portal del agro Chile')
start = time.process_time()
url_scraper = "https://www.portaldelagro.cl/category/agroindustria/"
request_pagina = urlopen(url_scraper) #VAMOS A SOLICITAR LA PÁGINA
pagina_html = request_pagina.read() #SE LEE LA RESPUESTA
request_pagina.close()
html_soup = BeautifulSoup(pagina_html, 'html.parser')# PÁGINA Y ANALIZADOR HTML
contenido_pagina = html_soup.find_all('div', class_="jeg_postblock_content")

filename = 'portaldelagro.csv'
f = open(filename, 'w')
headers = 'Titulo,Descripcion,Fecha,Hipervinculo,Imagen\n'
f.write(headers)

for contenido in contenido_pagina:
    titulo = contenido.find('h3',class_="jeg_post_title").text
    descripcion = contenido.find('p').text
    fecha = contenido.find('div', class_="jeg_meta_date").text
    hipervinculo = contenido.find('a').get('href')
    logging.info('Titulo de la noticia: '+str(titulo))
    f.write(titulo+","+descripcion+'\n'+","+fecha+'\n'+","+str(hipervinculo)+'\n')

logging.warning('Cada titulo y fecha esta individualizado por cda noticia')
end = time.process_time()
logging.info('Tiempo total de ejecucion: '+str(end - start))
f.close()   