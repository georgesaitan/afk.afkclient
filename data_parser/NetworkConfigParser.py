__author__ = 'gxg'
from httpclient.LocationInfo import Location
import re
class IfConfigParser:
    def testConfig(self):

        self.raw = None
        file = open('D:\proiecte\location\ifconfig.txt','r')

        self.raw = file.read()
        file.close()

    def parseWinInterface(self):
        import subprocess

        p = subprocess.Popen(['ipconfig','/all'],stdout=subprocess.PIPE)
        output, err = p.communicate()
        raw = output.replace('\n','').replace('\r','')
        location = Location()
        pattern = re.compile('Intel\(R\) Centrino\(R\) Advanced-N 6200 AGN.*?IPv4 Address. . . . . . . . . . . : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?Subnet Mask')
        location.ip = pattern.search(raw).group(1)

        return location

    # return a location object
    def parseEthData(self,eth_name):

        # get process output
        import subprocess
        p = subprocess.Popen(['ifconfig',str(eth_name)], stdout=subprocess.PIPE)
        output, err = p.communicate()

        location = Location()
        reg_ex_ip = 'inet addr:(.*?) '
        pattern = re.compile(reg_ex_ip)
        location.ip = pattern.search(output).group(1)

        return location