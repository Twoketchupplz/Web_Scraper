from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://mitel.dimi.uniud.it/ichi/#http://id.who.int/ichi/entity/1534640684")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj)
# for child in bsObj.find("table", {"class": "table 0table-bordered table-hover"}).children:
#     print(child)
