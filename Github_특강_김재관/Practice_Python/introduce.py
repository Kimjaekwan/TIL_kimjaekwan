# 명단에서 이름을 뽑아서 영어 소개와 한글 소개 만들기.
import random

name = ['홍길동','김막례','이희동','이덕팔']
eng_name = {
    '홍길동':'hong',
    '김막례':'mark',
    '이희동':'dong',
    '이덕팔':'par'

}

지목된사람 = random.choice(name)
지목된영어이름 = eng_name[지목된사람]

# 예) 저는 홍길동입니다. my name is hong 문자열을 만들고 싶다
# 띄어쓰기는 문자열('') 안에 입력
intro1 = '저는 ' + 지목된사람 +'입니다. ' + 'My name is ' + 지목된영어이름
intro2 = '저는 {}입니다. My name is {}'.format(지목된사람,지목된영어이름)
intro3 = f'저는 {지목된사람}입니다. My name is {지목된영어이름}'
# format(첫번째 중괄호, 두번째 중괄호)
print(intro1)
print(intro2)
print(intro3)