from selenium import webdriver
# 공식홈페이지 Documentation 에도 ChromeOptions()가 적혀있지만 안된다
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from openpyxl import Workbook

import time


def getNth(prnt_li_index: int):  # Get CSS Selector(Nth of Current List Item) after tag
    # index 는 1부터 시작
    return ':nth-of-type(' + str(prnt_li_index) + ')'


def getAriaLevel(aria_depth: int):  # Get CSS Selector(Child Li List)
    return ' li[aria-level="' + str(aria_depth) + '"]'


def getFullTitle(depth: int):
    # Excel; depth 와 맞는 col 에 full title 출력
    pass


def getFieldNum(key):
    print(key)
    num = {'ICHI code': 0, 'XCode': 1, 'Target': 2, 'Action': 3, 'Means': 4, 'Title': 5, 'ICHI descriptor': 6,
           'Definition': 7,
           'Index Terms': 8,
           'Includes Notes': 9,
           'Excludes': 10, 'Code also': 11, 'Excludes Notes': 12, 'Notes': 13, 'Original ICD uri': 14}.get(key)
    # print(num)
    return num


def getRecord(tr_tuple: tuple[WebElement], t: str):
    global wb, ws
    # Excel; 필드값을 비교해 같은 곳에 value 출력
    record = ['' for _ in range(15)]
    for tr in tr_tuple:
        field = tr.find_element(By.CSS_SELECTOR, value="td:nth-of-type(1)").text
        fieldNum = getFieldNum(field)

        data = tr.find_element(By.CSS_SELECTOR, value="td:nth-of-type(2)").text

        record[fieldNum] = data
    # for i in record:
    #     print(i, end=', ')
    # print()

    # result: list로 엑셀 데이터 삽입
    ws.append(record)
    wb.save("ICHI_Beta_3.xlsx")


def DFS(prnt_tuple: tuple[WebElement], prnt_selector: str, prnt_depth: int):
    li_nth = 1
    tab: str = '   ' * (prnt_depth - 1) + '+  '

    # print(tab + "* * * * * * * Lv." + str(prnt_depth) + " DFS Start * * * * * * *")
    # print(tab + prnt_selector)  # cur item List
    # print(tab + "List size: " + str(len(prnt_tuple)))

    for li in prnt_tuple:
        # get anchor
        trg_anchor = li.find_element(By.TAG_NAME, value='a')
        webdriver.ActionChains(driver).double_click(trg_anchor).perform()

        # get nth List Item
        nth_li_elmt = driver.find_element(By.CSS_SELECTOR, value=prnt_selector + getNth(li_nth))
        if 'jstree-leaf' in nth_li_elmt.get_attribute('class'):
            # Get Right Contents(leaf format)
            print(tab + '- ' + str(li_nth) + '. ' + trg_anchor.text)  # print a

            tr_tpl = tuple(driver.find_elements(By.CSS_SELECTOR, value="#content tbody > tr"))
            getRecord(tr_tpl, tab)

            li_nth = li_nth + 1
            continue
        else:
            # Get Right Contents
            print(tab + str(li_nth) + '. ' + trg_anchor.text)  # print a; step 2~6

            tr_tpl = tuple(driver.find_elements(By.CSS_SELECTOR, value="#content tbody > tr"))
            getRecord(tr_tpl, tab)

            next_selector: str = prnt_selector + getNth(li_nth) + getAriaLevel(prnt_depth + 1)
            child_tpl = tuple(driver.find_elements(By.CSS_SELECTOR, value=next_selector))
            DFS(child_tpl, next_selector, prnt_depth + 1)

            li_nth = li_nth + 1

        # print("* * * * * * * LV." + str(prnt_depth) + " DFS End * * * * * * *")


# def ChooseDropDownMenu:  # ul.dropdown-menu
#     return


# Workbook

wb = Workbook()

ws = wb.create_sheet('Means', 0)

fields_interventions = ['ICHI code', 'Target', 'Action', 'Means', 'ICHI descriptor', 'Definition',
                        'Index Terms', 'Includes Notes', 'Code also', 'Excludes Notes']

fields_target = ['ICHI code', 'Target', 'Action', 'Means', 'Title', 'ICHI descriptor', 'Definition',
                 'Index Terms', 'Excludes', 'Includes Notes', 'Code also', 'Excludes Notes', 'Mapping ICF']

fields_action = ['ICHI code', 'Target', 'Action', 'Means', 'Title', 'ICHI descriptor', 'Definition',
                 'Index Terms', 'Excludes', 'Includes Notes', 'Code also', 'Excludes Notes']

fields_means = ['ICHI code', 'Target', 'Action', 'Means', 'Title', 'ICHI descriptor', 'Definition', 'Index Terms',
                'Excludes', 'Includes Notes', 'Code also', 'Excludes Notes']

fields_extension_codes = ['XCode', 'Title', 'Definition', 'Index Terms', 'Excludes', 'Notes', 'Original ICD uri']

# ws.append()  # 알맞는 리스트를 집어넣는다

# 파일이 이미 있다면 다음 번호로..
wb.save("ICHI_Beta_3.xlsx")

# Web Crawling
mainPage = 'https://mitel.dimi.uniud.it/ichi/'

opt = Options()
# opt.add_argument('headless')
opt.add_argument('--blink-settings=imagesEnabled=false')
s = Service('../BrowserDriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=opt)
driver.implicitly_wait(20)

print("Chrome Driver Ready")
print()
driver.get(mainPage)

dropdown_menu = driver.find_element(By.CSS_SELECTOR, value='#dropdown-tsel')
if 'open' not in dropdown_menu.get_attribute('class'):  # 아직 열리지 않은 메뉴인 경우 클릭
    webdriver.ActionChains(driver).click(dropdown_menu).perform()

menu_interventions = dropdown_menu.find_element(By.CSS_SELECTOR, value='li[data-tsel="Interventions"]')
menu_target = dropdown_menu.find_element(By.CSS_SELECTOR, value='li[data-tsel="Target"]')
menu_action = dropdown_menu.find_element(By.CSS_SELECTOR, value='li[data-tsel="Action"]')
menu_means = dropdown_menu.find_element(By.CSS_SELECTOR, value='li[data-tsel="Means"]')
menu_extension_codes = dropdown_menu.find_element(By.CSS_SELECTOR, value='li[data-tsel="ExtensionCodes"]')

webdriver.ActionChains(driver).click(menu_means).perform()

DFS(tuple(driver.find_elements(By.CSS_SELECTOR, value='#tree li[aria-level="1"]')), '#tree li[aria-level="1"]', 1)
