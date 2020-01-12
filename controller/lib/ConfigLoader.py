
class ConfigLoader:
    '''
    정적함수를 사용하여 각 configuration 을 로드하는 클래스.

    1. db_load
    2. ...
    '''
    __config = None

    def __init__(self):
        pass

    @staticmethod
    def db_load(config_path):
        __config = config_path

        import os
        import json

        env = os.environ.get('PYTHON_ENV')
        if (env == 'production'):
            # Get the configurations from  environment variables
            DB_USER = os.environ.get('DB_USER')
            DB_PASSWORD = os.environ.get('DB_PASSWORD')
            DB_URL = os.environ.get('DB_URL')
            DB_PORT = os.environ.get('DB_PORT')
            DB_DATABASE = os.environ.get('DB_DATABASE')
            DB_CHARSET = os.environ.get('DB_CHARSET')

            db_url = "mysql+pymysql://%s:%s@%s:%s/%s?charset=%s" % (
                DB_USER, DB_PASSWORD, DB_URL, DB_PORT, DB_DATABASE, DB_CHARSET
            )
            return db_url
        else:
            with open(config_path) as conf:
                config = json.load(conf)

            DB_USER = config['DATABASE']['DB_USER']
            DB_PASSWORD = config['DATABASE']['DB_PASSWORD']
            DB_URL = config['DATABASE']['DB_URL']
            DB_PORT = config['DATABASE']['DB_PORT']
            DB_DATABASE = config['DATABASE']['DB_DATABASE']
            DB_CHARSET = config['DATABASE']['DB_CHARSET']

            db_url = "mysql+pymysql://%s:%s@%s:%s/%s?charset=%s" % (
                DB_USER, DB_PASSWORD, DB_URL, DB_PORT, DB_DATABASE, DB_CHARSET
            )

            return db_url
