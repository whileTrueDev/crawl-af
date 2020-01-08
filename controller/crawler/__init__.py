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

        self.__driver = webdriver.Chrome('C:/chromedriver.exe', options=self.__options) #크롬 드라이버 실행하기
        self.__driver.get('http://www.afreecatv.com')
    

    # 크롤링 메소드 구현
