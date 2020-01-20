def get_element_with_error_check(broad):
    '''
    soup 객체에서 데이터 추출 함수

    # 아프리카 방송 플레이어 url : bj 아이디
    # bj닉네임
    # 썸네일 이미지 url
    # 방송 화질정보
    # 방송 시작 시간
    # 방송 제목
    # 현재 시청자
    # 모바일 시청자 | pc 시청자
    '''
    try:
        info_tag = broad.find('a', {'class': 'box_link'})
    except Exception as e:
        print(e)
        return None

    try:
        if (info_tag is not None):
            count = info_tag.find('span', {'class': 'count'})
            count_tag = str(count).split('</em>')[1:]

            bj_id = broad.find('a', {'class': 'nick'})['user_id']

            bj_nickname = broad.find('a', {'class': 'nick'}).get_text()

            broad_num = broad.find('a', {'id': 'laterview_push'})[
                'data-broad-no']

            started_at = info_tag.find(
                'span', {'class': 'time'}).get_text().replace(' 방송시작', '')

            viewer = info_tag.find(
                'span', {'class': 'viewer'}).get_text().replace(' 명 시청', '').replace(',', '')

            display_quality = info_tag.find(
                'em', {'class': 'grade'}).get_text()

            title = info_tag.find('span', {'class': 'subject'}).get_text()

            mobile_viewer = count_tag[0].replace(
                '<em class="mobile">', '').replace(',', '')

            pc_viewer = count_tag[1].replace('</span>', '').replace(',', '')

    except Exception as e:
        print('[Error] An error occurred while getting elements')
        print(e)

    return {
        'bjId': bj_id if bj_id is not None else None,
        'bjNickName': bj_nickname if bj_nickname is not None else None,
        'broadcastId': broad_num if broad_num is not None else None,
        'startedAt': started_at if started_at is not None else None,
        'displayQuality': display_quality if display_quality is not None else None,
        'title': title if title is not None else None,
        'viewer': viewer if viewer is not None else None,
        'mobileViewer': mobile_viewer if mobile_viewer is not None else None,
        'pcViewer': pc_viewer if pc_viewer is not None else None,
    }
