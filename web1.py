# web1.py
# 웹크롤링을 위한 선언
from bs4 import BeautifulSoup

# 페이지 로딩(메서드 체인)
page = open ("test01.html","rt",encoding="utf-8").read()
# 검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
# 전체 페이지 보기
print(soup.prettify())