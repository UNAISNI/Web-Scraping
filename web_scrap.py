import html5lib
import requests
from bs4 import BeautifulSoup
import csv

url = "https://codewithharry.com"

r = requests.get(url)

filename = "test.csv"

htmlContent = r.content

soup = BeautifulSoup(htmlContent,"html.parser")

# paras = soup.find_all('p')
# print(paras)

csv_writter = csv.writer(open(filename,'w'))

csv_writter.writerow(soup)

