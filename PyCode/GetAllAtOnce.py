from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = 'https://mitel.dimi.uniud.it/ichi/'
cnt = 0

opt = Options()
opt.add_argument('headless') # 브라우저가 뜨지 않고 실행됨
opt.add_argument('--blink-settings=imagesEnabled=false')
s = Service('../BrowserDriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=opt)
print("driver ready")
driver.get(url)
driver.implicitly_wait(1)
time.sleep(1)

AnchorList = driver.find_elements(By.CSS_SELECTOR, value='#tree > ul a[href]')

print(len(AnchorList))

for i in range(len(AnchorList)):
    print(AnchorList[i].get_attribute("href"))
