from selenium import webdriver
# 공식홈페이지 Documentation 에도 ChromeOptions()가 적혀있지만 안된다
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = 'https://mitel.dimi.uniud.it/ichi/'
cnt = 0

opt = Options()
# opt.add_argument('headless') # 브라우저가 뜨지 않고 실행됨
opt.add_argument('--blink-settings=imagesEnabled=false')
s = Service('./BrowserDriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=opt)
print("driver ready")
driver.get(url)
time.sleep(3)
# sleep 이유
# https://www.selenium.dev/documentation/webdriver/getting_started/first_script/#4-establish-waiting-strategy
# time.sleep(3)
# driver.implicitly_wait(0.5)
# tab = driver.find_element(By.CLASS_NAME, "tab-content")
# driver.execute_script("return ('#tree').jstree('open_all');")

# def DFS(parent):
#
divTree = driver.find_element(By.XPATH, "//div[@id='tree']")  # "//*[@id='tree']"
time.sleep(0.5)
treeUl = divTree.find_element(By.TAG_NAME, "ul")  # "/ul[contains(@role='group')]"
time.sleep(0.5)
# driver.implicitly_wait(10)
# time.sleep(1)  # 타임슬립을 주면 왜 StaleElementReferenceException 에러가 발생할까?
# /html/body/div[1]/div/div[1]/div/div[1]/div[2]/ul/li[1]
# tagLi = treeUl.find_elements(By.XPATH, ".//li")
# tagLi = treeUl.find_elements(By.TAG_NAME, "li")  # 왜 하나의 li만 가져오는가?
# print(tagLi.get_attribute("role"))
tagLi = treeUl.find_elements(By.CLASS_NAME, "jstree-node")
time.sleep(0.5)
print("length:", len(tagLi))
for item in tagLi:
    cnt = cnt + 1
    print("cnt:", cnt)

    treeAnchor = item.find_element(By.TAG_NAME, 'a')
    print("treeAnchor class name: "+treeAnchor.get_attribute("class"))
    # print(treeAnchor.text)
    print("item text: "+item.text)
    webdriver.ActionChains(driver).double_click(treeAnchor).perform()
    time.sleep(0.8)  # headless 에서도 필요한가
    print()


# driver.close()
