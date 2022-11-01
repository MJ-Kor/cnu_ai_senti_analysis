import requests
from bs4 import BeautifulSoup

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
    # 리뷰를 수집하는 코드 작성
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=190694&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={num}'
    return title
# 리뷰 수집(리뷰, 평점, 작성자, 작성일자)

def movie_review_crawler(movie_code):
    title = movie_title_crawler(movie_code)  #  제목 수집
    print(f'제목: {title}')

    # set {제목, 리뷰, 평점, 작성자, 작성 일자}
