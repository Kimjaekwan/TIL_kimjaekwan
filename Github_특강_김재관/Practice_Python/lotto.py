# 로또 번호를 랜덤으로 뽑아주는 프로그램

import random

numbers = range(1,46)
# range(1,46) > [1,2,3,4,5,,,,,,,45]와 비슷하게 동작함.

# 6개의 숫자를 뽑아 출력해주는 프로그램
lotto = random.sample(numbers,6)
print(sorted(lotto))
# alt + shift + 위 or 아래 방향키 = 선택한 라인이 복사됨
# alt + 위 or 아래 방향키 = 라인이 위아래로 움직임
# sorted() = () 안의 텍스트를 정렬해 주는 함수
# random.sample(범위,개수) = 겹치지 않도록 범위 내의 숫자를 개수만큼 뽑아줌

