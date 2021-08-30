import requests 
from bs4 import BeautifulSoup


url =  "https://www.doviz.com/"

veri =  requests.get(url).content 



soup =  BeautifulSoup(veri,"html.parser") 
durum=input('verileri gormek istiyormusun : ')

if durum=='evet':
    for i in soup.find_all("div",{"class":"market-data"}):
        for a in i.find_all("div",{"class":"item"}):
              for v in a.find_all('span',{'class':'name'}):
                  for c in a.find_all('span',{'data-socket-attr':'s'}):
                             print('-'*10)
                             print(f'{v.get_text().strip()} fiyat : {c.text.strip()}')
                             print('-'*10)

else:
    print('tmmdir')
 

    
              
    
              
    
    
              
    