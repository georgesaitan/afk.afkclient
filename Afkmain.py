from httpclient.HttpClient import AfkClient
from httpclient.LocationInfo import Location

client = AfkClient()


# get all elements
print client.getAll()



# get ip
# location = Location()
# location.address = 'addressdsdsdads'
# print client.getIp(location)

# update location
# location = Location()
# location.ip = '2222'
# location.address =  'addressdsdsdads'
# location.externalView = 'wasup'
# location.geoLocation = '323232323'
# print client.update(location)

# delete location
# location = Location()
# location.address = 'dssds'
# print client.delete(location)

# save new location
location = Location()
location.ip = 'ip address'
location.address = 'addresee'
location.externalView = 'externall'
location.geoLocation = 'georloc'

client.save(location)



print client.getAll()