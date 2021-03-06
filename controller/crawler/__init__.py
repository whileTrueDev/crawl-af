from datetime import datetime
import time
from model.DBManager import DBManager
from controller.lib.ConfigLoader import ConfigLoader
from PIL import Image


class Crawler:
    def __init__(self, url, webdriver_path, config_file):
        self._url = url
        self._webdriver_path = webdriver_path
        self._config_path = config_file

        ##########################
        # DB Settings
        ##########################
        # Load config and make database access url
        db_url = ConfigLoader.db_load(self._config_path)

        # Access to DB and get session object
        self.data_access_object = DBManager.init(db_url)
        DBManager.init_db()  # initialize DB
        print('[%s] DataBase - connected..' % datetime.now())

    def init(self):
        '''
        크롤러 초기화 함수
        '''
        # Webdriver Settings
        from selenium import webdriver
        self.__options = webdriver.ChromeOptions()
        self.__options.add_argument('headless')
        self.__options.add_argument('window-size=1920x1080')
        self.__options.add_argument("disable-gpu")
        self.__options.add_argument("lang=ko_KR")

        self.__driver = webdriver.Chrome(
            self._webdriver_path, options=self.__options)  # 크롬 드라이버 실행
        self.__driver.get(self._url)

        # Time Settings
        self.start_time = datetime.now()
        self.running_time = time.time()

    def run(self):
        '''
        one-click Crawling start method
        '''
        self.init()
        self.show_all_broad_list_area()
        self.get_broad_data()
        print("[%s] Data getting job Done..." % datetime.now())
        self.insert()
        self.close()

    def run_screenshot(self):
        '''
        test 필요.
        '''
        self.init()
        self.show_all_broad_list_area()
        self.get_category_with_screenshot()

    # Crawling Methods
    def show_all_broad_list_area(self, time_sleep=1.0):
        '''
        끝까지 더보기 버튼 클릭 핸들러

        :time_sleep: 더보기 클릭 이후 sleep 시간
        '''

        start_time = time.time()
        while True:

            try:
                # 끝까지 더보기 버튼
                self.__driver.find_element_by_css_selector(
                    '.more_list').click()
                time.sleep(time_sleep)
            except Exception:
                complete_time = time.time()
                print('[%s] 더보기 클릭 완료: %s' %
                      (datetime.now(), str(complete_time - start_time)))
                break

        self.full_page_source = self.__driver.page_source

    def get_broad_data(self):
        '''
        broadlist_area 의 ul을 가져옴.
        해당 엘리먼트 안에 방송에 관한 정보가 담겨있음.
        '''

        from bs4 import BeautifulSoup
        import requests

        soup = BeautifulSoup(self.full_page_source, 'html.parser')

        # listarea: 생방송 카드 들의 모음
        broadlist_area = soup.find('div', {'id': 'broadlist_area'})
        self.broad_list = broadlist_area.find('ul').find_all('li')

        from controller.lib.get_element_with_error_check import get_element_with_error_check
        self.broad_data = []
        for broad in self.broad_list:
            data = get_element_with_error_check(broad)
            self.broad_data.append(data)

    def get_broad_detail_data(self):
        pass

    def get_category_with_screenshot(self):
        '''
        Get the data category and screenshot
        '''
        repeat = 1
        while repeat < 100:
            self.__driver.find_element_by_css_selector(
                """#broadlist_area > div > ul > li:nth-child({}) > div > a.box_link""".format(repeat)).click()
            self.__driver.find_element_by_css_selector(
                """#layer_high_quality > div > span > a > span""").click()  # 고화질 스트리머는 시간이 많이걸려 저화질로 캡처

            time.sleep(3)

            self.__driver.save_screenshot("bj_{}.png".format(
                repeat))  # 실행코드가 존재하는 파일안에 스크린샷 저장
            im = Image.open("bj_{}.png".format(repeat))
            cropimage = im.crop((0, 70, 1600, 1070))

            cropimage.save('bj_{}.png'.format(repeat))

            category = self.__driver.find_element_by_css_selector(
                """#player_area > div.broadcast_information > div.text_information > ul > li:nth-child(4) > span""").text

            self.__driver.close()

            # self.__driver.switch_to_window(self.__driver.window_handels[0])

            # self.broad_data.appendTo(category)

    def insert(self):
        '''
        크롤링된 데이터 insert
        '''
        from model.query import insert_stream_data

        # data insert
        insert_stream_data(self.data_access_object, self.broad_data)

        # commit changes
        self.data_access_object.commit()

    def close(self):
        self.data_access_object.remove()
        DBManager.dispose()
        self.end_time = datetime.now()
        self.running_time_end = time.time()

        print('[%s] JOB DOME' % self.end_time)
        print("Running time: %s" % (self.running_time_end - self.running_time))
        print("Number of Data: %s" % len(self.broad_data))
