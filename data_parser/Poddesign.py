__author__ = 'gxg'
from httpclient.HttpClient import HttpClient
from data_parser.ParserUtils import Utils


import re


class PodDesignParser:

    def __init__(self):
        self.page_data = None

    def getWebPage(self):
        urlClient = HttpClient()
        urlData = urlClient.getUrlData('http://www.pogdesign.co.uk/cat/')
        self.page_data = Utils.remLineDividers(urlData);

    def