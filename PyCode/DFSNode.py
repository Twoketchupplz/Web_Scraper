from selenium import webdriver
# 공식홈페이지 Documentation 에도 ChromeOptions()가 적혀있지만 안된다
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import time

mainPage = 'https://mitel.dimi.uniud.it/ichi/'

opt = Options()
opt.add_argument('headless')
opt.add_argument('--blink-settings=imagesEnabled=false')
s = Service('../BrowserDriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=opt)
driver.implicitly_wait(10)

print("Chrome Driver Ready")
print()
driver.get(mainPage)


def getNth(prntLiIndex: int):  # Get CSS Selector(Nth of Current List Item) after tag
    # index 는 1부터 시작
    return ':nth-of-type(' + str(prntLiIndex) + ')'


def getAriaLevel(ariaDepth: int):  # Get CSS Selector(Child Li List)
    return ' li[aria-level="' + str(ariaDepth) + '"]'


def DFS(prntList: list[WebElement], prntSelector: str, paramListDepth: int):
    li_nth = 1
    tab: str = '   ' * (paramListDepth - 1) + '+  '

    # print()
    print(tab + "* * * * * * * Lv." + str(paramListDepth) + " DFS Start * * * * * * *")
    print(tab + prntSelector)  # cur item List
    print(tab + "List size: " + str(len(prntList)))

    for li in prntList:
        # get anchor
        trg_anchor = li.find_element(By.TAG_NAME, value='a')
        webdriver.ActionChains(driver).double_click(trg_anchor).perform()

        # get nth List Item
        nth_li_elmt = driver.find_element(By.CSS_SELECTOR, value=prntSelector + getNth(li_nth))
        if 'jstree-leaf' in nth_li_elmt.get_attribute('class'):
            # Get Right Contents(leaf format)
            print(tab + '- ' + str(li_nth) + '. ' + trg_anchor.text)  # print a
            li_nth = li_nth + 1
            continue
        else:
            # print(tab + "aria-level: " + nth_li_elmt.get_attribute('aria-level'))

            # Get Right Contents
            print(tab + str(li_nth) + '. ' + trg_anchor.text)  # print a

            next_selector: str = prntSelector + getNth(li_nth) + getAriaLevel(paramListDepth + 1)
            childList = driver.find_elements(By.CSS_SELECTOR, value=next_selector)
            DFS(childList, next_selector, paramListDepth + 1)
            li_nth = li_nth + 1

        print("* * * * * * * LV." + str(paramListDepth) + " DFS End * * * * * * *")


# def ChooseDropDownMenu:  # ul.dropdown-menu
#     return

DFS(driver.find_elements(By.CSS_SELECTOR, value='#tree li[aria-level="1"]'), '#tree li[aria-level="1"]', 1)

# while(True):
#     pass
