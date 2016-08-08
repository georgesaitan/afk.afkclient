__author__ = 'gxg'
import re
class Utils:


    @staticmethod
    def remLineDividers(initial_string):
        return initial_string.replace('\r','').replace('\n','')

    @staticmethod
    def extractHost(urlString):
        return re.search('(\w*?\.\w{2,3})',urlString).group(1)

    @staticmethod
    def getTestData(url):
        file = open(url, 'r')
        page_data = file.read().replace('\r', '').replace('\n', '')
        file.close()

        return page_data