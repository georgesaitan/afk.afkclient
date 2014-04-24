__author__ = 'gxg'
import re
class Utils:


    @staticmethod
    def remLineDividers(initial_string):
        return initial_string.replace('\r','').replace('\n','')

    @staticmethod
    def extractHost(urlString):
        return re.search('(\w*?\.\w{2,3})',urlString).group(1)