import time
import requests
from bs4 import BeautifulSoup
import re
import telepot


send_lists = []
token = "6450289450:AAEZZXbQBJmFKIW7R_BOGubo5lEXs3qoFM0"
chat_id = 5907381682
bot = telepot.Bot(token)


def search_hotdeals(keyword):

    # 사이트 주소
    # 120자 넘으면 에러 뜸, 여러 줄로 나눠서 작성
    url = (
        "https://www.fmkorea.com/search.php?mid=hotdeal&category=&listStyle=webzine&"
        "search_keyword={}&search_target=title_content"
    ).format(keyword)

    # url에 요청해서 결과물(html)을 r로 받음
    r = requests.get(url)

    # r의 내용(html)을 lxml 이란 파서를 써서 BeautifulSoup 을 사용해 분석
    bs = BeautifulSoup(r.content, "lxml")

    # bs의 내용 중 li class = li를 가지고 있는 div class = li 요소를 선택
    # select는 리스트 타입으로 반환
    divs = bs.select("li.li > div.li")

    # divs의 결과물 중 필요한 요소를 가져옴
    for d in divs:
        # img 클래스 이름이 thumb entered loaded 일때 공백 사이를 .으로 연결해 3가지 요소를 모두 포함한 클래스를 선택한다
        # 근데 안됨. 그래서 걍 thumb 만 넣음
        # thumb = 이미지 + @, data-original = 썸넬만
        images = d.select("img.thumb")[0]
        image = images.get("data-original")

        # 펨코 핫딜에서 이미 지나간 핫딜은 글자 중앙에 취소선(-)이 달려 있음
        # 이런 경우 var8이 아닌 var8Y 클래스를 가지고 있으니 조건문을 사용해 에러 방지
        # href = 원글 링크
        if d.select(".hotdeal_var8"):
            alink = d.select(".hotdeal_var8")[0]
        elif d.select(".hotdeal_var8Y"):
            alink = d.select(".hotdeal_var8Y")[0]
        else:
            print("에러: 해당되는 클래스가 없습니다")
        href = "https://www.fmkorea.com" + alink.get("href")

        # re 모듈
        # 정규 표현식을 사용하여 연속된 공백을 1개로 치환하고 양쪽 공백을 제거
        # r: \(역슬래쉬)를 이스케이프 문자로 처리하지 않음. \n같은 줄바꿈에서 사용되는 \가 아닌 정규 표현식 용 \으로 사용을 하겠다~
        # \s: 공백 문자를 나타내는 이스케이프 시퀀스
        # +: 1회 이상 반복을 나타내는 메타 문자
        # alink에서 text를 뽑아 가공
        # <a> 태그 사이의 내용 = .text
        title = re.sub(r'\s+', ' ', alink.text).strip()

        # 핫딜의 정보를 가지고 있는 div 클래스 hotdeal_info를 가져옴
        # 쇼핑몰 / 가격 / 배송비를 가지고 있음
        total = d.select("div.hotdeal_info")[0]
        infodeal = re.sub(r'\s+', ' ', total.text).strip()

        # 중복 알림 체크
        if infodeal not in send_lists:
            send_info(href, infodeal)
        else:
            bot.sendMessage(chat_id, "중복")
            continue


def send_info(href, infodeal):

    bot.sendMessage(chat_id, href)
    bot.sendMessage(chat_id, infodeal)
    bot.sendMessage(chat_id, "ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    send_lists.append(infodeal)

def start_crawling():
    while True:
        search_hotdeals("사세")
        time.sleep(10) # 딜레이


# if __name__ == "__main__":

