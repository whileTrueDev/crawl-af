
# 데이터 베이스 관리자 설정파일
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBManager():
    __engine = None
    __session = None

    @staticmethod
    def init(db_url, db_log_flag=None):
        DBManager.__engine = create_engine(db_url, echo=db_log_flag)
        DBManager.__session = scoped_session(sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=DBManager.__engine
        ))
        dao = DBManager.__session

        return dao

    @staticmethod
    def init_db():
        from model import Base
        Base.metadata.create_all(bind=DBManager.__engine)

    @staticmethod
    def dispose():
        DBManager.__session.close()
        DBManager.__engine.dispose()
