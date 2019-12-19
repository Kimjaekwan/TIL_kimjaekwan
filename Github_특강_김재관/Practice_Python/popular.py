import requests
import bs4

html = requests.get('https://www.naver.com/')
soup = bs4.BeautifulSoup(html.text,'html.parser')

keywords = soup.select('span.ah_k')

# keywords = ['a','b','c'] > a, b, c를 각각 키워드로 이름짓겠다.
# for keyword in keywords:
#    print(keyword.text)



# 배열[0:n] 배열의 0번째 인덱스부터 n-1번쨰
# 인덱스들의 요소를 가져와 배열로 만든다.
real_keywords = keywords[0:20]
real_real_keywords = [keyword.text for keyword in real_keywords]
# 무엇이 1등인지 모르게 가나다 순 정렬.
problem = sorted(real_real_keywords)

print('아래의 보기 중에서 1위를 고르세요')
print(problem)
answer = input('당신이 입력한 답:')
# 배열[0] : 배열의 첫번째 요소.

if answer == real_real_keywords[0]:
    print('정답입니다.')
else:
    print('오답입니다')

# = : 우변을 좌변에 대입함.
# == : 양 변이 같은지 틀린지 비교 


"""
#[0 ~ 100]까지의 배열 표기.
numbers = [i for i in range(0,101)]
print(numbers)

numbers = []
for i in range(0,101):
    numbers.append(i)
    #append : 원하는 순서대로 넣겠다.
    print(numbers)
"""   