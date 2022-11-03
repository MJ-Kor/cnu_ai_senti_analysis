import requests
import re
import math
from bs4 import BeautifulSoup

###################
# 1. 영화 제목 수집 #
###################

# 제목 수집
# 단지 함수 생성
# 함수
#   - 함수는 생성하면 아무 동작 x
#   - 반드시 생성 후 호출을 통해 사용
#   - 1. 생성, 2. 호출
# 기능의 단위들을 모듈화해서 따로 만듦

def movie_title_crawler(movie_code):
    url = f'https://movie.naver.com/movie/bi/mi/point.naver?code={movie_code}#tab'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.h_movie > a')[0].get_text()
    return title


# 리뷰 수집(리뷰, 평점, 작성자, 작성일자)
# 리뷰를 수집하는 코드 작성
def movie_review_crawler(movie_code):
    title = movie_title_crawler(movie_code)  #  제목 수집
    print(f'>> Start collecting movies for {title}')

    # set {제목, 리뷰, 평점, 작성자, 작성 일자}
    url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={movie_code}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    all_count = doc.select('strong.total > em')[0].get_text()  # 리뷰 전체 수

    # "2,480" : str type(문자열)
    #         : int type(정수형 숫자)
    # print(type(all_count))

    # A(문자) / 10 -> 불가능
    # "2480" -> 2480(O)
    # "2,480" -> 문자 포함은 변화가 안된다.

    # 1. 숫자만 추출 : 정규식
    numbers = re.sub(r'[^0-9]', '', all_count)
    pages = math.ceil(int(numbers)/10)
    print(f'The total number of pages to collect is {pages}')

    # 해당 페이지 리뷰 수집!
    count = 0  # 전체 리뷰 수를 count
    for page in range(1, pages+1):
        url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={movie_code}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={page}'
        result = requests.get(url)
        doc = BeautifulSoup(result.text, 'html.parser')
        review_list = doc.select('div.score_result > ul > li')  # 1page의 리뷰 10건

        for i , one in enumerate(review_list):  # 리뷰 1건씩 수집
            # 리뷰, 평점, 작성자, 작성일자
            review = one.select('div.score_reple > p > span')[-1].get_text().strip()
            score = one.select('div.star_score > em')[0].get_text()


            print(f' # Review: {review}')
            print(f' # Score: {score}')

        break