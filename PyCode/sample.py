from urllib.request import urlopen
from bs4 import BeautifulSoup
# https://mitel.dimi.uniud.it/ichi/#http://id.who.int/ichi/entity/861153274
# https://www.naver.com

html = urlopen("https://mitel.dimi.uniud.it/ichi/#http://id.who.int/ichi/entity/861153274")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.title)