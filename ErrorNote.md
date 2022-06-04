# Error

## 현상
- urlopen()이 수행되지 않음
- *[SSL: CERITIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired*

## 원인

## 해결
- [StackOverflow](https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error)
- import certifi, ssl
    - use attr context=ssl.create_default
    
## 현상
- *DeprecationWarning: executable_path has been deprecated, please pass in a Service object*

## 원인
- selenium 4에서는 Service Object에 경로를 넣어야함

## 해결
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
s = Service('path')
opt = Options()
driver = webdriver.Chorme(service=s, option=opt)
```


## 현상
- 같은 코드임에도 매번 Run 결과가 랜덤함
- 정상 동작, 에러 발생(실행x, 실행 되나 잘못된 Interaction)

## 이유(추측)
- 브라우저가 조작될 충분한 시간을 주어야함

## 해결?
- `time.sleep(1)`
- url, element 가져오거나, 브라우저 조작 전후로 충분한 시간을 확보 
