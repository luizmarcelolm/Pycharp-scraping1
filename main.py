import requests
from bs4 import BeautifulSoup

# Faz a requisição HTTP à página e obtém o conteúdo
url = 'https://www.google.com.br/search?q=previs%C3%A3o+do+tempo+s%C3%A3o+jos%C3%A9+dos+campos%2C+sp&sca_esv=558460728&sxsrf=AB5stBjLDegGX0wv1C-I7ezahskLxAycGw%3A1692492540956&ei=_GLhZIT6OcKV0AbY2LWIAw&oq=previsa%7Eotempo&gs_lp=Egxnd3Mtd2l6LXNlcnAiDnByZXZpc2F-b3RlbXBvKgIIADIEEAAYRzIEEAAYRzIEEAAYRzIEEAAYRzIEEAAYRzIEEAAYRzIEEAAYRzIEEAAYR0i8DFAAWABwAHgCkAEAmAEAoAEAqgEAuAEByAEA4gMEGAAgQYgGAZAGCA&sclient=gws-wiz-serp'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}


site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, "html.parser")

attCidade = {'class':'BBwThe'}
cidade = soup.find("span", attrs=attCidade)
print("Cidade: ",cidade.text)

attTemp = {'class':'wob_t q8U8x'}
temp = soup.find("span", attrs=attTemp)
print("Temperatura: ",temp.text, "°")

attDia = {'class':'wob_dts'}
dia = soup.find("div", attrs=attDia)
print("Dia: ",dia.text)

attInfo = {'id':'wob_dc'}
info = soup.find("span", attrs=attInfo)
print("Informações: ",info.text)


