from selenium import webdriver
# 공식홈페이지 Documentation 에도 ChromeOptions()가 적혀있지만 안된다
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import time

mainPage = 'https://mitel.dimi.uniud.it/ichi/'

opt = Options()
# opt.add_argument('headless')
opt.add_argument('--blink-settings=imagesEnabled=false')
s = Service('../BrowserDriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=opt)
print("driver ready")
driver.get(mainPage)
driver.implicitly_wait(10)
time.sleep(1)


def getNth(prntLiIndex: int):
    # index 는 1부터 시작
    return ':nth-of-type(' + str(prntLiIndex) + ')'


def getAriaLevel(ariaDepth: int):
    return ' li[aria-level="' + str(ariaDepth) + '"]'


def DFS(prntList: list[WebElement], prntSelector: str, paramListDepth: int):
    li_nth = 1
    tab: str = '  + ' * (paramListDepth - 1)

    # print()
    print(tab + "* * * * * * * * * * * * * * *")
    print(tab + prntSelector)  # cur item List
    print(tab + "Current Depth:" + str(paramListDepth))
    print(tab + "size: " + str(len(prntList)))

    for li in prntList:
        # get anchor
        trg_anchor = li.find_element(By.TAG_NAME, value='a')
        webdriver.ActionChains(driver).double_click(trg_anchor).perform()
        # time.sleep(1.1)

        # get nth List Item
        nth_li_elmt = driver.find_element(By.CSS_SELECTOR, value=prntSelector + getNth(li_nth))
        # if "jstree-leaf" in prntList[idx].get_attribute('class'):  # leaf 노드인 경우
        if 'jstree-leaf' in nth_li_elmt.get_attribute('class'):
            # Get Right Contents(leaf format)
            print(tab + '-+- ' + str(li_nth) + '. ' + trg_anchor.text)  # print a
            pass
        else:
            print()
            print(tab + "aria-level: " + nth_li_elmt.get_attribute('aria-level'))
            print(tab + "parent node")
            # Get Right Contents
            # nth Li의 depth+1노드를 찾는다. li[aria-level='depth']/:nth-of-type('nth')/ li[aria-level='depth+1']
            print(tab + str(li_nth) + '. ' + trg_anchor.text)  # print a

            next_selector: str = prntSelector + getNth(li_nth) + getAriaLevel(paramListDepth + 1)
            childList = driver.find_elements(By.CSS_SELECTOR, value=next_selector)
            DFS(childList, next_selector, paramListDepth + 1)
        li_nth = li_nth + 1


DFS(driver.find_elements(By.CSS_SELECTOR, value='#tree li[aria-level="1"]'), '#tree li[aria-level="1"]', 1)

while(True):
    pass


# rootLiVal = '#tree li[aria-level="1"]'
# rootLiList = driver.find_elements(By.CSS_SELECTOR, value=rootLiVal)
# time.sleep(0.5)
#
# print("length:", len(rootLiList))
# print()
#
# nth = 1
# for li in rootLiList:
#     # li = driver.find_element(By.CSS_SELECTOR, value=rootLiVal + getNextSelector(nth))
#     nextCSS = 'li[aria-level="1"]:nth-of-type(' + str(cnt + 1) + ') li[aria-level="' + str(2) + '"]'
#
#
#     anc = li.find_element(By.TAG_NAME, value='a')
#     print("href: " + anc.get_attribute('href'))
#     print("text: " + anc.text)
#     print()
#     time.sleep(1)  # headless 에서도 필요한가
#
#     webdriver.ActionChains(driver).double_click(anc).perform()
#     time.sleep(1.1)  # data-delay = 1000
#
#     lv2LiList = driver.find_elements(By.CSS_SELECTOR, value=nextCSS)
#     time.sleep(1)  # headless 에서도 필요한가
#
#     print("하위노드 크기", len(lv2LiList))
#     print()
#
#     print("********************")
#     for i in lv2LiList:
#         atag = i.find_element(By.TAG_NAME, value='a')
#         print(atag.text)
#     print("********************")
#
#     cnt = cnt + 1
