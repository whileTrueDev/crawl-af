
# coding: utf-8

# In[213]:


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pandas import DataFrame
import time
import warnings
from datetime import datetime
import pandas as pd
from selenium.webdriver.common.keys import Keys
global rank #rank를 전역변수로 설정
global i #i를 전역변수로 설정
i = 0 # 검색 하고자 넣은 인자 리스트의 순서를 파악하기 위한 변수
rank = 2 #아프리카 홈페이지에 있는 bj들은 시청자수 순위로 나열되기 때문에 그 순위를 나타내기 위한 변수 rank

warnings.filterwarnings("ignore", category=DeprecationWarning) #경고 메세지 무시

stime = time.time() #현재 시각을 stime으로 받기

# Headless
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")

now = datetime.now() #크롤링 시작시간을 간단하게 보기위한 함수 now
print("크롤링 시작시간은",now)


title_i = [] #방송제목
name_i = [] #bj이름
viewer_i = [] #현재 시청자수
start_time_i = [] #방송 시작시간
category_i = [] #방송 카테고리
current_time_i = [] #현재 시각
bj_id_i = [] #bj의id

driver = webdriver.Chrome('C:/chromedriver.exe', options=options) #크롬 드라이버 실행하기
driver.get('http://www.afreecatv.com')


# In[214]:


def open_driver(): # 아프리카 홈페이지에서 100명까지 방송 들어가기위한 셀레니움 이용한 클릭
    driver.find_element_by_css_selector("""#broadlist_area > div > ul > li:nth-child({}) > div > a.box_link""".format(rank-1)).click()
    driver.switch_to_window(driver.window_handles[1])
    driver.get(driver.current_url)


# In[215]:


def save_bj_name(): # 방송 안에서 bj의 닉네임을 가져오기
    bj_name = driver.find_element_by_css_selector("""#player_area > div.broadcast_information > div.text_information > div.nickname""")
    name_i.append(bj_name.text)


# In[216]:


def save_title(): #live화면에서 방송제목 가져오기
    title = driver.find_element_by_css_selector("""#player_area > div.broadcast_information > div.text_information > div.broadcast_title > span""")
    title_i.append(title.text)


# In[217]:


def current_viewer(): #live화면에서 현재 시청자수 가져오기
    driver.find_element_by_xpath("""//*[@id="stop_screen"]/dl/dd[2]/a""").click()
    time.sleep(4)
    viewer = driver.find_element_by_xpath("""//*[@id="nAllViewer"]""")
    if str(0) == viewer.text: #크롤링중 방송이 종료되었을때 데이터 수집 안함
        viewer_i.append("방송이 종료되었습니다")
    else:
        viewer_i.append(viewer.text) #방송이 종료되지 않을 경우 현재 시청자수 수집


# In[218]:


def save_start_time():#방송 시작시간 live화면에서 가져오기
    start_time = driver.find_element_by_css_selector("""#player_area > div.broadcast_information > div.text_information > ul > li:nth-child(1) > span""")
    start_time_i.append(start_time.text)


# In[219]:


def save_category(): #live화면에서 카테고리 가져오기
    category =  driver.find_element_by_css_selector("""#player_area > div.broadcast_information > div.text_information > ul > li:nth-child(4) > span""")
    category_i.append(category.text)


# In[220]:


def screenshot(): #각 라이브 화면을 스크린샷으로 찍음
    driver.save_screenshot("bj_{}.png".format(rank-1))


# In[221]:


def bj_id(): #bj id B행에 등록
    info_id = driver.current_url.split('/') #bj의 id를 방송국에 가서 가져오면 시간이 더걸릴거같아 url에서 id 추출
    bj_id_i.append(info_id[3])


# In[222]:


def current_time(): # 수집한 현재시간 
    now = datetime.now()
    current_time_i.append(now)


# In[223]:


while rank<4: #100번 실행하도록 하는 반복문
    open_driver()
    save_bj_name()
    bj_id()
    save_title()
    current_viewer()
    save_start_time()
    save_category()
    screenshot()
    driver.close()
    current_time()
    driver.switch_to_window(driver.window_handles[0])
    rank += 1
    if not rank % 61: #live 방송수가 60번째가되면 더보기를 클릭해야 100번까지 볼수있으므로 더보기 클릭
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_css_selector("""#broadlist_area > div > div > a""").click()
        time.sleep(3)
    if rank == 102: #102번째가되면 드라이버 종료
        driver.quit()


now = datetime.now()
print("크롤링 끝난시간", now ) #크롤링이 끝난 시간을 반환
print("\n진행시간 {}초".format(time.time() - stime))


# In[229]:


bj_list = ['wnnw','khm11903','qweqwe','123qd']  #인자로 넣을 리스트의 예시


# In[230]:


len_search_bj = len(bj_list) #반복문에 리스트에 id 수만큼 반복할수 있도록 id수 세기


# In[231]:


while i < len_search_bj: #인자로 넣은 갯수만큼 반복하기 위한 반복문
    int(i)
    if bj_list[i] in bj_id_i: #bj_list속 id가 bj_id_i에 있는지 비교하기
        indexno = bj_id_i.index(bj_list[i]) #있다면 인덱스 번호 반환
        p_title = title_i[indexno] #인덱스 번호에 맞는 bj의 방송 제목 출력
        p_name = name_i[indexno] #인덱스 번호에 맞는 bj 닉네임 출력
        p_viewer = viewer_i[indexno] #인덱스 번호에 맞는 bj의 현재 시청자수 출력
        p_start_time = start_time_i[indexno] #인덱스 번호에 맞는 bj의 방송 시작 시간 출력
        p_category = category_i[indexno]#인덱스 번호에 맞는 bj의 카테고리 출력
        p_currenttime = current_time_i[indexno] #인덱스 번호에 맞는 bj의 현재 방송 시작시간 출력
        p_bj_id = bj_id_i[indexno] #인덱스 번호에 맞는 bj의 id 출력
        print("방송 제목: ", p_title)
        print("bj 닉네임: ",p_name)
        print("현재 시청자수: ", p_viewer)
        print("방송 시작 시간: ",p_start_time)
        print("방송 카테고리: ",p_category)
        print("데이터 수집 시간: ",p_currenttime)
        print("bj id: ",p_bj_id)
        
    else:
        print("해당 bj가 방송중이지 않습니다")
    i = i + 1


# In[227]:


data = [title_i,name_i, viewer_i,start_time_i,category_i,current_time_i,bj_id_i ]

