def insert_stream_data(dao, data):
    '''
    DB - afreecaStreamDetail 적재.
    bjId, bjNickName, broadcastId, startedAt, displayQuality, title, viewer, mobileViewer, pcViewer
    '''
    from model import AfreecaStreamDetail
    from datetime import datetime

    members = list(map(
        lambda data: AfreecaStreamDetail(
            bjId=data['bjId'], bjNickName=data['bjNickName'],
            broadcastId=data['broadcastId'],
            startedAt=datetime.strptime(
                data['startedAt'], '%Y-%m-%d %H:%M:%S'),
            displayQuality=data['displayQuality'], title=data['title'],
            viewer=data['viewer'], mobileViewer=data['mobileViewer'],
            pcViewer=data['pcViewer']
        ), data))

    dao.add_all(members)
