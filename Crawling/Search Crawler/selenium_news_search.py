# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import math
from selenium import webdriver

# 각 크롤링 결과 저장하기 위한 리스트 선언
title_text = []
link_text = []
source_text = []
date_text = []
contents_text = []
result = {}

#selenium 사용 설정
path = r"/Users/jungyulyang/programming/chromedriver"
driver = webdriver.Chrome(path)

# 날짜 정제화 함수
def date_cleansing(test):
    try:
        # 지난 뉴스
        # 머니투데이  10면1단  2018.11.05.  네이버뉴스   보내기
        pattern = '\d+.(\d+).(\d+).'  # 정규표현식

        r = re.compile(pattern)
        match = r.search(test).group(0)  # 2018.11.05.
        date_text.append(match)

    except AttributeError:
        # 최근 뉴스
        # 이데일리  1시간 전  네이버뉴스   보내기
        pattern = '\w* (\d\w*)'  # 정규표현식

        r = re.compile(pattern)
        match = r.search(test).group(1)
        # print(match)
        date_text.append(match)


# 내용 정제화 함수
def contents_cleansing(contents):
    first_cleansing_contents = re.sub('<dl>.*?</a> </div> </dd> <dd>', '',
                                      str(contents)).strip()  # 앞에 필요없는 부분 제거
    second_cleansing_contents = re.sub('<ul class="relation_lst">.*?</dd>', '',
                                       first_cleansing_contents).strip()  # 뒤에 필요없는 부분 제거 (새끼 기사)
    third_cleansing_contents = re.sub('<.+?>', '', second_cleansing_contents).strip()
    contents_text.append(third_cleansing_contents)
    # print(contents_text)


def crawler(query, sort, s_date, e_date):
    s_from = s_date.replace(".", "")
    e_to = e_date.replace(".", "")
    page = 1
    driver.get("https://search.naver.com/search.naver?where=news&query=" + query + "&sort=" + sort + "&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to)
    extracted = driver.find_element_by_xpath('//*[@id="main_pack"]/div[1]/div[1]/div[1]/span').text.split(" ")
    maxpage = (math.ceil(int(extracted[2].replace("건", "").replace(",","")) / 10)-1)*11 + 1

    while page <= maxpage:
        url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort=" + sort + "&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(
            page)

        response = requests.get(url)
        html = response.text

        # 뷰티풀소프의 인자값 지정
        soup = BeautifulSoup(html, 'html.parser')

        # <a>태그에서 제목과 링크주소 추출
        atags = soup.select('._sp_each_title')
        for atag in atags:
            title_text.append(atag.text)  # 제목
            link_text.append(atag['href'])  # 링크주소
        #
        # # 신문사 추출
        # source_lists = soup.select('._sp_each_source')
        # for source_list in source_lists:
        #     source_text.append(source_list.text)  # 신문사
        #
        # # 날짜 추출
        # date_lists = soup.select('.txt_inline')
        # for date_list in date_lists:
        #     test = date_list.text
        #     date_cleansing(test)  # 날짜 정제 함수사용

        # 본문요약본
        contents_lists = soup.select('ul.type01 dl')
        for contents_list in contents_lists:
            # print('==='*40)
            # print(contents_list)
            contents_cleansing(contents_list)  # 본문요약 정제화

        # 모든 리스트 딕셔너리형태로 저장
        result = {"title": title_text, "contents": contents_text}
        print(page)

        df = pd.DataFrame(result)  # df로 변환
        page += 10

    # 새로 만들 파일이름 지정\
    df.to_csv("./data/{start_period}-{end_period}-result.csv".format(start_period=s_date,end_period=e_date))


def main():
    info_main = input("=" * 50 + "\n" + "입력 형식에 맞게 입력해주세요." + "\n" + " 시작하시려면 Enter를 눌러주세요." + "\n" + "=" * 50)

    query = input("검색어 입력: ")
    sort = input("뉴스 검색 방식 입력(관련도순=0  최신순=1  오래된순=2): ")  # 관련도순=0  최신순=1  오래된순=2
    s_date = input("시작날짜 입력(2019.01.04):")  # 2019.01.04
    e_date = input("끝날짜 입력(2019.01.05):")  # 2019.01.05

    crawler(query, sort, s_date, e_date)


main()