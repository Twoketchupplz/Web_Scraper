from selenium import webdriver
# 공식홈페이지 Documentation 에도 ChromeOptions()가 적혀있지만 안된다
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = 'https://mitel.dimi.uniud.it/ichi/'
cnt = 0

opt = Options()
opt.add_argument('headless') # 브라우저가 뜨지 않고 실행됨
opt.add_argument('--blink-settings=imagesEnabled=false')
s = Service('./BrowserDriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=opt)
print("driver ready")
driver.get(url)
driver.implicitly_wait(1)
time.sleep(1)

# treeUl = driver.find_element(By.CSS_SELECTOR, value='#tree > ul')  # "/ul[contains(@role='group')]"
time.sleep(0.5)

# rootLiList = treeUl.find_elements(By.CSS_SELECTOR, value='li.jstree-node')
rootLiList = driver.find_elements(By.CSS_SELECTOR, value='#tree > ul > li.jstree-node')
time.sleep(0.5)

print("length:", len(rootLiList))
print()

for li in rootLiList:
    treeAnchor = li.find_element(By.TAG_NAME, 'a')
    print("treeAnchor class: "+treeAnchor.get_attribute("class"))
    # print(treeAnchor.text)
    print("text: " + treeAnchor.text)
    print()
    time.sleep(1)  # headless 에서도 필요한가

    webdriver.ActionChains(driver).double_click(treeAnchor).perform()
    time.sleep(1)  # headless 에서도 필요한가

    lv2LiList = li.find_elements(By.CSS_SELECTOR, value='ul > li')
    time.sleep(1)

    print("    child length:", len(lv2LiList))
    for childLi in lv2LiList:
        childAnchor = childLi.find_element(By.TAG_NAME, 'a')
        time.sleep(1)

        # print("   child name:")
        print("        child item text:" + childLi.text)

# driver.close()
