import requests
import datetime
import json
from pyproj import Transformer


def getWardBoundaries():
	wardCounter = 0
	wardBoundaries = []
	while wardCounter <= 14:
		print("Getting boundary points for Ward " + str(wardCounter) + " ! \n")
		wardCounter += 1
		ward = getWard(wardCounter)
		wardBoundaries.append(ward)
	writeWardBoundaries(wardBoundaries)


def getWard(wardNumber):
	wardCoords = {}
	wardCoords["Ward"] = wardNumber
	wardCoords["EPSG:3857"] = []
	wardCoords["EPSG:4326"] = []
	ward3857 = requests.get("https://spatialsolutions.hamilton.ca/webgis/rest/services/General/Political/MapServer/15/query?f=json&outSR={'wkid':3857}&objectIds="+str(wardNumber)).json()
	for l in ward3857["features"][0]["geometry"]["rings"][0]:
		coord3857 = {}
		coord3857["lng"] = l[0]
		coord3857["lat"] = l[1]
		wardCoords["EPSG:3857"].append(coord3857)
	ward4326 = requests.get("https://spatialsolutions.hamilton.ca/webgis/rest/services/General/Political/MapServer/15/query?f=json&outSR={'wkid':4326}&objectIds="+str(wardNumber)).json()
	for l in ward4326["features"][0]["geometry"]["rings"][0]:
		coord4326 = {}
		coord4326["lng"] = l[0]
		coord4326["lat"] = l[1]
		wardCoords["EPSG:4326"].append(coord4326)
	return wardCoords


def writeWardBoundaries(wardBoundaries):
	current_date = datetime.datetime.now()
	jsonfile = open('hamilton_ward_boundaries_'+str(current_date.month)+'-'+str(current_date.day)+'-'+str(current_date.year)+'.json', 'w', encoding='utf8', newline='')
	with jsonfile:
	    json.dump(wardBoundaries, jsonfile)
	jsonfile.close()


# def transformCoords(x, y):
# 	transformer = Transformer.from_crs(3857,4326)
# 	newCoords = transformer.transform(x, y)
# 	return (newCoords[0], newCoords[1])

getWardBoundaries()