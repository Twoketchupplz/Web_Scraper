from selenium import webdriver
# 공식홈페이지 Documentation 에도 ChromeOptions()가 적혀있지만 안된다
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

mainPage = 'https://mitel.dimi.uniud.it/ichi/'
cnt = 0
urlStack = []

opt = Options()
# opt.add_argument('headless')
opt.add_argument('--blink-settings=imagesEnabled=false')
s = Service('../BrowserDriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=opt)
print("driver ready")
driver.get(mainPage)
driver.implicitly_wait(1)
time.sleep(1)

parentNode = '#tree li[aria-level="1"]'

rootLiList = driver.find_elements(By.CSS_SELECTOR, value=parentNode)
time.sleep(0.5)

print("length:", len(rootLiList))
print()
for i in range(4):
    li = driver.find_element(By.CSS_SELECTOR, value='li[aria-level="1"]:nth-of-type('+str(i+1)+')')
    nextCSS = 'li[aria-level="1"]:nth-of-type(' + str(cnt + 1) + ') li[aria-level="' + str(2) + '"]'

    anchor = li.find_element(By.TAG_NAME, value='a')
    print("href: " + anchor.get_attribute('href'))
    print("text: " + anchor.text)
    print()
    time.sleep(1)  # headless 에서도 필요한가

    webdriver.ActionChains(driver).double_click(anchor).perform()
    time.sleep(1.1)  # data-delay = 1000

    print('li[aria-level="1"]:nth-of-type(' + str(cnt + 1) + ') li[aria-level="' + str(2) + '"]')
    lv2LiList = driver.find_elements(By.CSS_SELECTOR, value=nextCSS)
    time.sleep(1)  # headless 에서도 필요한가

    print("하위노드 크기", len(lv2LiList))
    print()

    print("********************")
    for i in lv2LiList:
        atag = i.find_element(By.TAG_NAME, value='a')
        print(atag.text)
    print("********************")

    cnt = cnt + 1

    # lv2LiList = li.find_elements(By.CSS_SELECTOR, value='ul > li')
    # time.sleep(1)
    #
    # print("    child length:", len(lv2LiList))
    # for childLi in lv2LiList:
    #     childAnchor = childLi.find_element(By.TAG_NAME, 'a')
    #     time.sleep(1)
    #
    #     # print("   child name:")
    #     print("        child item text:" + childLi.text)
