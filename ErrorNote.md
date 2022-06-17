# Error

## SSL: CERITIFICATE_VERIFY_FAILED

### 현상

- *[SSL: CERITIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired*
- urlopen()이 수행되지 않음

### 원인

### 해결

- [StackOverflow](https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error)
- import certifi, ssl
    - use attr context=ssl.create_default

## DeprecationWarning

### 현상

- *DeprecationWarning: executable_path has been deprecated, please pass in a Service object*

### 원인

- selenium 4에서는 Service Object에 경로를 넣어야함

### 해결

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

s = Service('path')
opt = Options()
driver = webdriver.Chorme(service=s, option=opt)
```

## StaleElementReferenceException

### 현상

- *selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference*
- 같은 코드임에도 매번 Run 결과가 랜덤함
- 정상 동작, 에러 발생(실행x, 실행 되나 잘못된 Interaction)

### 원인

- 웹 엘리먼트 로딩이 길어져(네트워크 지연, 액션 시간 등) 미쳐 로딩하지 못한 엘리먼트를 찾으려 했음

### 해결

- 대기시간을 부여
    - 묵시적 대기시간(Implicit wait time)
        - 전체 웹 엘리먼트에 동일한 타임아웃 시간을 설정
    - 명시적 대기시간(Explicit wait time)
        - 특정 엘리먼트에 대해서만 타임아웃 시간 설정
        - 특수하게 긴 시간이 필요한 경우 사용
    - `time.sleep(sec)`
        - 고정적인 타임아웃 시간(강제)

## UnexpectedAlertPresentException

### 현상
- Target, Action, Means에서 작업 수행 중 아래 예외 발생
- *UnexpectedAlertPresentException Alert Text Error: Generic error*

### 원인
- 3개 항목에서 leaf node에 데이터가 없는 경우가 존재함
- alert() 발생

### 해결방안
- 예외처리