from controller.crawler import Crawler

if __name__ == "__main__":
    import os

    AFREECA_TV_HOME = 'http://www.afreecatv.com'
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    DRIVER_PATH = os.path.join(ROOT_PATH, 'chromedriver.exe')
    CONFIG_FILE_PATH = os.path.join(ROOT_PATH, 'config', 'config.json')

    onad = Crawler(AFREECA_TV_HOME, DRIVER_PATH, CONFIG_FILE_PATH)
    onad.run()
