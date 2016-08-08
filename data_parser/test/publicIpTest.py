from data_parser.WhoAmIParser import Whatismyipaddress
from data_parser.test.test import Test
parser = Whatismyipaddress()
#parser.getWebPage()
parser.getTestData()
#print parser.page_data

testObj = Test()


print testObj.getData(parser)
