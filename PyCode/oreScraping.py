from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


# 페이지에서 발견된 내부 링크를 모두 목록으로 만든다
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # /로 시작하는 링크 모두 찾기
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])

    return internalLinks


# 페이지에서 발견된 외부 링크를 모두 목록으로 만든다
def getExternalLinks(bsObj, excluderUrl):
    externalLinks = []
    # 현재 URL을 제외한 http, www로 시작하는 링크 탐색
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excluderUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])

    return externalLinks


def splitAddress(address):
    addressParts = address.replace("https://", "").split("/")
    return addressParts


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)

        # 이거 오타인가?
        return getExternalLinks(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def folloExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://opreilly.com")
    print("Random external links is:" + externalLink)
    folloExternalOnly(externalLink)


folloExternalOnly("http://oreilly.com")
