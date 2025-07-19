import requests
from bs4 import BeautifulSoup

def get_news():
  # url 주소
  url = "https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EA%B5%B0%EB%8C%80"
  # url 접근해 정보 가져오기(requests)
  res = requests.get(url)
  # 정보 내 필요한 데이터 파싱(BeautifulSoup)
  soup = BeautifulSoup(res.content, 'html.parser')
  data = soup.find_all('span',class_="sds-comps-text-type-headline1")
  data_list = []
  for i in data:
    data_list.append(i.text)
  return data_list

for i in get_news():
  print("******************")
  print(i)