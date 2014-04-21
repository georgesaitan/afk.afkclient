__author__ = 'gxg'

from data_parser.WhoAmIParser import Whatismyipaddress

parser = Whatismyipaddress()
print parser.page_data
print parser.locationInfo().__dict__

from data_parser.NetworkConfigParser import IfConfigParser

net_parser = IfConfigParser()
net_parser.testConfig()
print net_parser.parseWinInterface().__dict__;

# net_parser1 = IfConfigParser()
# net_parser1.parseEthData('eth0')