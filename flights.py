import sys
import json
import operator
from geopy import distance

airports_lookup=str(sys.argv[1])

with open('airports.json') as f:
    airports_info = json.load(f)
    
destinations=[]
destinations_distance={}
for airport in airports_info:
    if airport['IATA/FAA'] == airports_lookup:
        selected_airport_id = airport['Airport ID']
        selected_airport_latitude= airport['Latitude']
        selected_airport_longitude= airport['Longitude']
        destinations=airport['destinations']
        for destination in destinations:        
            for airport in airports_info:
                if destination in airport['Airport ID']:
                    destination_iata=airport['IATA/FAA']
                    destination_name=airport['Name']
                    destination_latitude=airport['Latitude']
                    destination_longitude=airport['Longitude']
                    distance_between=round(distance.distance([selected_airport_latitude,selected_airport_longitude],[destination_latitude,destination_longitude]).km)
                    name_summary=str(destination_iata +' '+ destination_name +' ')
                    distance_summary=str(str(distance_between)+'km')
                    destinations_distance.update({name_summary : distance_summary})

destinations_distance=sorted(destinations_distance.items(), key=operator.itemgetter(1))

for dest in destinations_distance:
    print (dest[0]+dest[1])                    
