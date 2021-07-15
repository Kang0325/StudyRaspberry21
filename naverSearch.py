import urllib.request as urq
import urllib.parse as uparse
import datetime
import json

class naverSearch(object):
    def __init__(self):
        print('NAVER Search API 생성')

    def getRequestUrl(self, url):
        req = urq.Request(url)
        req.add_header('X-Naver-Client-Id', '9anYbYmNmLR8WB9OFwtO')
        req.add_header('X-Naver-Client-Secret', 'eKTI4enOus')

        try:
            res = urq.urlopen(req)
            if res.getcode() == 200: #ok
                print('[{0}] URL Request succeed'.format(datetime.datetime.now()))
                return res.read().decode('utf-8')
        except Exception as e:
            print(e)
            return None

    # 네이버 검색API 사용 함수
    def getNaverSearchResult(self, sNode, search_word, page_start, display):
        base = 'https://openapi.naver.com/v1/search/'
        node = '{0}.json'.format(sNode)
        param = '?start={0}&display={1}&query={2}'.format(page_start, display, uparse.quote(search_word))
        url = base + node + param

        retData = self.getRequestUrl(url)
        if retData == None:
            return None
        else:
            return json.loads(retData)

    # 데이터 처리
    def getPostData(self, post, jsonResult):
        pass