
import urllib
import urllib.request
import http.client
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

import re

class MySpider(object):
    "getting page and items from website 'url' rule by regular expression 'pattern'."
    def __init__(self,url,headers,pattern):
        self.__url = url
        self.__headers= headers
        self.__pattern = pattern


    # return the website source code formatted by unicode
    def getPage(self):
        try:
            # print("getting website content......" + "from " + self.url)
            request = urllib.request.Request(url=self.__url)#, headers=self.headers)
            response = urllib.request.urlopen(request)
            page = response.read().decode('utf-8')  # get source code
        except Exception as errStr:
            print(errStr,'Wrong:Error occured when read from website!')
            return ''
        else:
            # print("getting website content finished successfully")
            return page

    # return a tuple containing the entries.  msgs=((......),(......),...)
    def getMsgs(self):
        page = self.getPage()
        # print("get entries ......")
        msgs = re.findall(self.__pattern, page)
        # print("get entries finished")
        return msgs

