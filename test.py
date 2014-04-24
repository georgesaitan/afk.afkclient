__author__ = 'gxg'

# from data_parser.WhoAmIParser import Whatismyipaddress
#
# parser = Whatismyipaddress()
# print parser.page_data
#
# external = parser.locationInfo()
# print external.__dict__
#
# from data_parser.NetworkConfigParser import IfConfigParser
#
# net_parser = IfConfigParser()
# net_parser.testConfig()
#
# internal = net_parser.parseWinInterface()
#
# print internal.__dict__;
#
# # net_parser1 = IfConfigParser()
#
# from data_parser.DataMixer import Mixer
#
# dataMixer = Mixer()
# print dataMixer.mixData(internal,external).__dict__
#
#
# from httpclient.HttpClient import HttpClient
# client = HttpClient()
# print client.getUrlData('http://whatismyipaddress.com/')


from data_parser.DataConstructor import  WinLocationConstructor
winConstructor = WinLocationConstructor()
print winConstructor.createWinLocation('here').__dict__

test = 'http://whatismyipaddress.com/'
import re
print re.search('(\w*?\.\w{2,3})',test).group(1)