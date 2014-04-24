__author__ = 'gxg'
from data_parser.DataMixer import Mixer
from data_parser.ParserUtils import Utils
from httpclient.HttpClient import HttpClient
from data_parser.NetworkConfigParser import IfConfigParser
from data_parser.WhoAmIParser import Whatismyipaddress
class WinLocationConstructor:

    def createWinLocation(self,here):

        #get external view
        ext_parser = Whatismyipaddress()
        ext_parser.getWebPage()
        external = ext_parser.locationInfo()

        #get internal view
        if_parser = IfConfigParser()
        internal = if_parser.parseWinInterface()
        # mix data
        mixer = Mixer()
        final_location = mixer.mixData(internal,external)

        # construct final location object
        final_location.address = here

        return final_location

    def createLinuxLocation(self,here):

        #get external view
        ext_parser = Whatismyipaddress()
        ext_parser.getWebPage()
        external = ext_parser.locationInfo()

        #get internal view
        if_parser = IfConfigParser()
        internal = if_parser.parseEthData('eth0')
        # mix data
        mixer = Mixer()
        final_location = mixer.mixData(internal,external)

        # construct final location object
        final_location.address = here

        return final_location

