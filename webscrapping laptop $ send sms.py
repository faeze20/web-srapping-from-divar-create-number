import requests
from bs4 import BeautifulSoup
import ghasedakpack
import random

import random
# create number for sed sms
def create_phone():
    numbers=[]
    for i in range(9):
        numbers.append(str(random.randint(0,9)))
    return("09"+"".join(numbers))    





# api_key for sms
sms = ghasedakpack.Ghasedak("39a79a573ba0e90ee353b76acb178b8d33ee0626ed96cd7cb9ec984cf2612ac6")



pages=requests.get("https://divar.ir/s/tehran/laptop-notebook-macbook?q=%D9%84%D9%BE%20%D8%AA%D8%A7%D9%BE")
soup=BeautifulSoup(pages.content,"html.parser")
# print(soup)

import re
# find all price laptop
result=soup.find_all("div",attrs={"class":"kt-post-card__description"})
# print(result)
for item in result:
    r=re.sub(r"\s+","",item.get_text().strip())
    print(r)
    # number=str(random.choices([0,9,9]))
    sms.send({ 'message':r,  'receptor' :create_phone() })
