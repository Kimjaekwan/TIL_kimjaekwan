# Server&Chatbot



img를 포함한 실습 내용

(https://kjk3210.tistory.com/manage/posts/)

## [Python을 이용한 간이 서버 구성]

**[Flask?](https://www.palletsprojects.com/p/flask/)**

**- Python을 이용한 서버 구축에 필요한 모듈**

## [서버 구축을 바탕으로한 chatbot 만들기]



**※ ngrok** **으로 전달받은 세션은 8시간 후에 만료. 영구 등록할 필요가 있음.**

**> Pythonanywhere(**https://www.pythonanywhere.com/) : 추출한 세션을 영구 등록하는 서비스(일부 유료)

\- web > 쭉 진행 > Flask > Python 3.8선택

\- 코드 등록 : file > my site > flask_app.py > 작성한 코드 등록.

\- 사용한 모듈 등록 : console > Bash > pip3 install (모듈) --user

\- 보안파일 등록 : file > my site > .env 입력 > new file > 자신의 env 파일에 있는 내용을 복사 후 붙여넣기.

\- pythonanywhere에서 받은 주소를 telegram bot에 재 입력

\- 모든 작업 끝난 후 web > Reroad 시 변경된 주소로 bot이 실행됨.

 

**[금일 교육 내용 간단 정리]**

**1. Flask를 이용한 간이 서버 구축**

**2. Telegram, Flask 등을 이용한 Chatbot 구성(랜덤 점심메뉴 노출, 로또, 번역기능 탑재)**

**- 지금 현재 Pythonanywhere에서 서버 공유가 제대로 적용되지 않아, 차후 추가 공부가 필요함.**

**- 작일, 금일 진행한 Python 제작 기록은 github에 풀버전이 공유되어 있음.**

금일은 교육 시간 부족으로 Image 첨부는 블로그 업로드 된 것으로 대체함.