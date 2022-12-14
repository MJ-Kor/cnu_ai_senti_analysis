###################################################
# Collector 비즈니스 로직을 모아둔 파이썬 파일
###################################################
# - 2022.10.18, 파일 생성, 김민주
###################################################

# 함수 생성
# - 함수 : 반복적으로 사용하는 기능을 코드로 묶어서 만듦
# - 사용 : 함수 이름으로 호출
# - Python 에서 ()가 붙어있으면 대부분 함수
# - 예: print(), pprint(), get(), get_text()
# - 내장 함수 : 파이썬 설치하면 기본적으로 제공
# - 외부 함수: 다른 개발자가 만들어 놓음
#           requests.get(), BeautifulSoup()
# - 사용자 정의 함수: 직접 만들어서 사용
# Python naming rule
# 1) 파스칼 (Pascal) : GetDaumNews
# 2) 카멜 (Camel) : getDaumNews
# 3) 스네이크 (Sneak) get_daum_news(최신 언어)

import requests
from bs4 import BeautifulSoup

def get_daum_news_(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.tit_view')[0].get_text()
    contents = doc.select('section p')

    print(f'뉴스제목 : {title}')

    # if 문 -> 제어문(조건이 True인 경우에만 실행)
    # != -> 같지 않다
    if len(contents) != 0:  # 본문이 있는 경우에만
        content = ''
        for line in contents:
            content += line.get_text()
        print(f'뉴스본문 : {content}')