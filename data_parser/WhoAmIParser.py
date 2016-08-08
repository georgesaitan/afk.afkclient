__author__ = 'gxg'
import re
from httpclient.LocationInfo import Location
from httpclient.HttpClient import HttpClient
from data_parser.ParserUtils import Utils


class Whatismyipaddress(object):

    def __init__(self):
        self.page_data  = None

    def getTestData(self):

        self.page_data = None
        file = open('/home/gxg/devep/testdata/location.txt','r')
        self.page_data = file.read().replace('\r','').replace('\n','')
        file.close()

    def getWebPage(self):
        #get page data
        urlCient = HttpClient()
        urlData = urlCient.getUrlData('http://whatismyipaddress.com/')
        self.page_data = Utils.remLineDividers(urlData)

    def locationInfo(self):

        location = Location()
        geo_location = ''

        reg_ex_isp = 'style="font-weight:bold;color:#676769;">ISP:</th><td style="font-size:14px;">(.*?)</td></tr>'
        reg_ex_city = 'style="font-weight:bold;color:#676769;">City:</th><td style="font-size:14px;">(.*?)</td></tr>'
        reg_ex_region = 'style="font-weight:bold;color:#676769;">Region:</th><td style="font-size:14px;">(.*?)</td></tr>'
        reg_ex_country = 'style="font-weight:bold;color:#676769;">Country:</th><td style="font-size:14px;">(.*?)</td></tr>'

        reg_ex_ip = 'alt="Click for more about (.*?)"></a></div>'



        pattern = re.compile(reg_ex_isp)
        geo_location = pattern.search(self.page_data).group(1) + ', '

        pattern = re.compile(reg_ex_city)
        geo_location += pattern.search(self.page_data).group(1) + ', '

        pattern = re.compile(reg_ex_region)
        geo_location += pattern.search(self.page_data).group(1) + ', '

        pattern = re.compile(reg_ex_country)
        geo_location += pattern.search(self.page_data).group(1)

        pattern = re.compile(reg_ex_ip)
        location.externalView = pattern.search(self.page_data).group(1)
        location.geoLocation = geo_location
        return location

