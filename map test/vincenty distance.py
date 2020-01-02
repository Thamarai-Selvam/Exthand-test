import geopy.distance
from math import sin, cos, sqrt, atan2, radians

c1 = (52.2290756,21.0122287)
c2 = (52.406374,16.9251681)

print('geopy method',geopy.distance.geodesic(c1,c2).km) # geopy.distance.distance() will also work.

print('\n')


#But somehow the below one works more accurately.
#This method reproduces the exact result as shown in Websites.

R = 6373.0 # The approx. radius of Spherical Earth in km. 

#The same latitude and longitude shown in above example to differntiate them.
lat1 = radians(52.2296756)
lon1 = radians(21.0122287)
lat2 = radians(52.406374)
lon2 = radians(16.9251681)

#dlat and dlong are lat. and long. differences.

dlon = lon2 - lon1
dlat = lat2 - lat1

#Harvesine formula 
a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", distance)

#Another Method to use the Harvesine formula(using mpu module)


import mpu

lat1 = 52.2296756
lon1 = 21.0122287

lat2 = 52.406374
lon2 = 16.9251681


dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
print('distance = ', dist)
