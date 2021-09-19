import requests
import urllib.request
from bs4 import BeautifulSoup
import re  

def get_phones():
   Number_phone = []
   try:
      Tels = re.findall("[+][\d]{3}[ ][(][\d][)][ ][\d]{2}[ ][\d]{2}[ ][\d]{2}[ ][\d]{2}", response.text)
      Number_phone = Number_phone + Tels 
   except:
      pass
   try:
      Tels = re.findall("[+][\d]{3}[ ][\d]{2}[ ][\d]{2}[ ][\d]{2}[ ][\d]{2}", response.text)
      Number_phone = Number_phone + Tels 
   except:
      pass
   try:
      Tels = re.findall("[+][\d]{3}[ ][(][\d][)][ ][\d]{3}[ ][\d]{2}[ ][\d]{2}[ ][\d]{2}", response.text)
      Number_phone = Number_phone + Tels 
   except:
      pass
   return Number_phone
  
        
def get_mails():
   Liste_Mails = []
   try:
      Mails = re.findall("([A-z0-9\.]+@[A-z0-9]+\.[A-z.]+)", response.text)
      Liste_Mails = Liste_Mails + Mails
   except:
      pass
   return Liste_Mails


# Here you should put your urls in (str)
urls = [url1,url2]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    for Tel in get_phones():
         print (Tel)
         
    for Mail in get_mails():
         print (Mail)
