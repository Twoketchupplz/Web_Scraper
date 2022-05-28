import certifi
import ssl
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

htmlUrl = "https://mitel.dimi.uniud.it/ichi/#http://id.who.int/ichi/entity/1534640684"


def getTitle(url):
    context = ssl.create_default_context(cafile=certifi.where())
    try:
        html = urlopen(url, context=context)
    except HTTPError as e:
        # 찾을수 없는 페이지, URL 해석 에러, 서버를 찾을 수 없을때
        print("HTTP ERROR!")
        print(e)
        return None
    try:
        # 존재하지 않는 태그
        bsObj = BeautifulSoup(html.read(), "html.parser")
        urlTitle = bsObj.body.h1
    except AttributeError as e:
        print("Attr Error")
        print(e)
        return None
    else:
        # 프로그램을 계속 실행
        print("GOOD!")
        return urlTitle


title = getTitle(htmlUrl)
if title is None:
    print("Title could not be found")
else:
    print(title)
