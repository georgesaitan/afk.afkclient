__author__ = 'gxg'

from httpclient.LocationInfo import  Location

class Mixer:

    def mixData(self,internalLocation,externalLocation):
        location = Location()
        location.ip = internalLocation.ip
        location.externalView = externalLocation.externalView
        location.geoLocation = externalLocation.geoLocation

        return location
