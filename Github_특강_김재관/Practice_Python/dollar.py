import bs4
import requests

html = requests.get('https://finance.naver.com/marketindex/')

soup = bs4.BeautifulSoup(html.text,'html.parser')
dollar = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
print(dollar)


"""
import requests
import bs4

# 이 주소로 요청을 보내면, 응답으로 html 파일이 도착할 것.
html = requests.get('https://finance.naver.com/sise/sise_index.nhn?code=KOSPI')

# html 텍스트를 내가 보기 좋게 접근할 수 있도록 변경
soup = bs4.BeautifulSoup(html.text,'html.parser')
# CSS Selector로 내가 원하는 Tag를 가져오겠다.
kospi = soup.select_one('#now_value')

print(kospi.text)
"""