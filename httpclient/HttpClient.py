__author__ = 'gxg'

import urllib2

class AfkClient:
    def __init__(self):
        self.headers = {}
        self.headers[Headers.AUTH] = HeaderKeys.AUTH
        self.headers[Headers.CONTENT_TYPE] = HeaderKeys.CONTENT_TYPE
        self.headers[Headers.ACCEPT] = HeaderKeys.ACCEPT
        self.headers[Headers.HOST] = HeaderKeys.HOST
        self.headers[Headers.ACCEPT_LANGUAGE] = HeaderKeys.ACCEPT


#get all ips
#GET request on /ip
    def getAll(self):

        url = WsUrl.BASEdev+WsUrl.WS+ WsUrl.ALL+WsUrl.DEVparam # request url
        req = urllib2.Request( url ,None, self.headers)

        resp = urllib2.urlopen(req)

        return resp.read()

#sample {"address":"addressdsdsdads","externalView":"111","geoLocation":"1111","ip":"111111"}
    #get single ip
    #put request on /ip
    def getIp(self, location):
        url = WsUrl.BASEdev+WsUrl.WS + WsUrl.IP + WsUrl.DEVparam
        payload = str(location.__dict__) #'{"address":"'+location.address+'"}'


        #thanks a lot python ... just  one char away from the response
        payload = payload.replace('\'','"')
        # print payload
        req = urllib2.Request( url,payload,self.headers )
        req.get_method = lambda :'POST'
        resp = urllib2.urlopen(req)

        return resp.read()


    #delete ip
    #make delete request on /delete
    def delete(self, location):
        url = WsUrl.BASEdev + WsUrl.WS + WsUrl.DELETE + WsUrl.DEVparam

        payload = str(location.__dict__)
        payload = payload.replace('\'','"')
        req = urllib2.Request(url,payload,self.headers)

        req.get_method = lambda : 'POST'
        resp = urllib2.urlopen(req)

        return resp.read()

    #update ip
    #make post request on /update
    def update(self, location):

        url = WsUrl.BASEdev+WsUrl.WS + WsUrl.UPDATE + WsUrl.DEVparam

        payload = str(location.__dict__)
        payload = payload.replace('\'','"')
        #'{"address":"addressdsdsdads","externalView":"211112","geoLocation":"1122","ip":"222"}'
        req = urllib2.Request(url,payload,self.headers)

        req.get_method = lambda : 'POST'
        resp = urllib2.urlopen(req)

        return resp.read()

    #save ip
    #make post request to /ip
    def save(self, location):

        url = WsUrl.BASEdev+WsUrl.WS + WsUrl.SAVE + WsUrl.DEVparam
        payload = str(location.__dict__)
        payload = payload.replace('\'','"')
        req = urllib2.Request(url,payload,self.headers)

        req.get_method = lambda : 'POST'
        resp = urllib2.urlopen(req)

        return resp.read()

class Headers:

    AUTH = 'auth'
    CONTENT_TYPE = 'Content-type'
    ACCEPT = 'Accept'
    HOST = 'Host'
    ACCEPT_LANGUAGE = 'Accept-Language'
    ACCEPT_ENCODING = 'Accept-Encoding'
    AGENT = 'User-Agent'

class HeaderKeys:
    AUTH = 'test'
    CONTENT_TYPE = 'application/json'
    ACCEPT = 'application/json'
    HOST = 'afknotes.appspot.com'
    ACCEPT_LANGUAGE = 'en-US,en;q=0.8'
    ACCEPT_ENCODING = 'gzip,deflate,shch'

class WsUrl:
    BASE = 'http://afknotes.appspot.com/'
    WS = 'ws/location/'
    IP = 'ip/'
    UPDATE = 'update/'
    DELETE = 'delete/'
    SAVE = 'save/'
    ALL = 'all/'
    BASEdev = 'http://127.0.0.1:8888/'
    DEVparam = '?gwt.codesvr=127.0.0.1:9997'

class BrowserVal:
    AUTH = 'test'
    CONTENT_TYPE = 'application/json'
    ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    ACCEPT_LANGUAGE = 'en-US,en;q=0.8,ro;q=0.6'
    ACCEPT_ENCODING = 'gzip,deflate,sdch'
    HOST = 'whatismyipaddress.com'
    AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36'

class HttpClient:
    def __init__(self):
        self.headers = {}
        self.headers[Headers.AGENT] = BrowserVal.AGENT
        self.headers[Headers.ACCEPT] = BrowserVal.ACCEPT
        self.headers[Headers.ACCEPT_ENCODING] = BrowserVal.ACCEPT_ENCODING
        #self.headers[Headers.HOST] = BrowserVal.HOST
        self.headers[Headers.ACCEPT_LANGUAGE] = BrowserVal.ACCEPT_LANGUAGE

    def getUrlData(self,url):
        from data_parser.ParserUtils import Utils
        self.headers[Headers.HOST] = Utils.extractHost(url)#BrowserVal.HOST

        req = urllib2.Request(url,None,self.headers)

        resp = urllib2.urlopen(req)

        from cStringIO import StringIO
        from gzip import GzipFile
        data2 = GzipFile('', 'r', 0, StringIO(resp.read())).read()
        return data2