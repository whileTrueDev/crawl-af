from sqlalchemy import Column, String, Integer, TIMESTAMP, Text
from sqlalchemy.sql.expression import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AfreecaStreamDetail(Base):
    """
    아프리카 스트리밍의 세부정보를 담기 위한 테이블

    :bjId: bj의 아프리카tv 아이디
    :bjNickName: bj의 닉네임
    :broadcastId: 방송의 고유 id
    :startedAt: 방송의 시작 시간
    :displayQuality: 방송의 화질 정보
    :title: 방송의 제목
    :viewer: 현재 시청자 수
    :mobileViewer: 현재 모바일 시청자 수
    :pcViewer: 현재 PC 시청자 수
    :time: 현재시간
    """
    __tablename__ = 'afreecaStreamDetail'
    code = Column(Integer, primary_key=True, autoincrement=True)
    bjId = Column(String(50), unique=False)
    bjNickName = Column(String(50), unique=False)
    broadcastId = Column(String(50), unique=False)
    startedAt = Column(TIMESTAMP)
    displayQuality = Column(String(50), unique=False)
    title = Column(String(200), unique=False)
    viewer = Column(Integer, unique=False)
    mobileViewer = Column(Integer, unique=False)
    pcViewer = Column(Integer, unique=False)
    time = Column(TIMESTAMP, default=func.now())

    def __init__(self, bjId, bjNickName,
                 broadcastId, startedAt, displayQuality,
                 title, viewer, mobileViewer, pcViewer):
        self.bjId = bjId
        self.bjNickName = bjNickName
        self.broadcastId = broadcastId
        self.startedAt = startedAt
        self.displayQuality = displayQuality
        self.title = title
        self.viewer = viewer
        self.mobileViewer = mobileViewer
        self.pcViewer = pcViewer

    def __repr__(self,):
        return """%s, %s, %s, %s, %s, %s, %s, %s, %s""" % (
            self.bjId,
            self.bjNickName,
            self.broadcastId,
            self.startedAt,
            self.displayQuality,
            self.title,
            self.viewer,
            self.mobileViewer,
            self.pcViewer)
