
class Crawler:
    def __init__(self, url):
        self._url = url

        # webdriver settings
        from selenium import webdriver
        self.__options = webdriver.ChromeOptions()
        self.__options.add_argument('headless')
        self.__options.add_argument('window-size=1920x1080')
        self.__options.add_argument("disable-gpu")
        self.__options.add_argument("lang=ko_KR")

        self.__driver = webdriver.Chrome(
            'C:/chromedriver.exe', options=self.__options)  # 크롬 드라이버 실행하기
        self.__driver.get('http://www.afreecatv.com')

    def run(self):
        '''
        crawl start method
        '''
        pass

    # Crawling Methods
    def init(self):
        '''
        크롤러 초기화 함수
        '''
        from datetime import datetime
        import time
        self.start_time = datetime.now()
        self.running_time = time.time()

        # Connect with Database and Get the BJ data contracted with OnAD
        # DB에서 가져왔다 가정.
        self.contracted_BJs = ['와꾸대장봉준', '감스트']

    def show_all_broad_list_area(self):
        # 끝까지 더보기 버튼
        self.__driver.find_element_by_css_selector('.more_list').click()

    def get_broad_data(self):
        # #broadlist_area 의 .listarea 의 ul 의 li들을 모두 가져옴.
        # 해당 엘리먼트 안에 방송에 관한 정보가 담겨있음.

        # 아프리카 방송 플레이어 url : bj 아이디
        # bj닉네임
        # 썸네일 이미지 url
        # 방송 화질정보
        # 방송 시작 시간
        # 방송 제목
        # 현재 시청자
        # 모바일 시청자 | pc 시청자
        pass

    def get_broad_detail_data(self):
        # 방송 카테고리 정보 가져오기.
        pass
