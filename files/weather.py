#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import urllib, json, datetime
url = "{YOUR_URL_TO_JSON}"
response = urllib.urlopen(url)
data = json.loads(response.read())

# Expects this json object:
# `{u'temp': 16.5, u'rain': {u'intensity': 0.1166, u'probability': 0.11}, u'humidity': 0.89, u'pressure': 1010.76, u'location': {u'lat': 51.23, u'lon': 6.78}, u'wind': {u'speedKPH': 4.89, u'windSpeed': 4.89, u'windGust': 4.89, u'dir': u'SSW', u'windBearing': 203}, u'desc': u'Overcast'}`

now = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
location = str(data['location']['lat']) + ', ' + str(data['location']['lon'])

# Checks for Düsseldorf's lat and long
if data['location']['lat'] == 51.23 and data['location']['lon'] == 6.78:
    locationName = 'Düsseldorf'
else:
    locationName = location

temp = str(data['temp']) + '° C'
desc = str(data['desc'])
rainIntensity = str(data['rain']['intensity'])
rainProbability = str(data['rain']['probability'] * 100)
windSpeed = str(data['wind']['windSpeed'])
windGust = str(data['wind']['windGust'])
windDirection = str(data['wind']['dir'])
windDirections = {
    "N": "North",
    "NE": "North-East",
    "NW": "North-West",
    "S": "South",
    "SE": "South-East",
    "SW": "South-West",
    "E": "East",
    "W": "West",
    "NNE": "North-North-East",
    "NNW": "North-North-West",
    "SSW": "South-South-West",
    "SSE": "South-South-East"
}

# debug
# print data

# Generating a humanized phrase
outStd = 'It is currently ' + desc + ' in ' + locationName + ' with a temperature of ' + temp + '.'

# Rain
if data['rain']['probability'] > 0.05:
    outRain = 'There is a ' + rainProbability + '% change of rain and you can expect about ' + rainIntensity + ' mm.'
else:
    outRain = 'No rain is expected at this time.'

# Wind
if data['wind']['windSpeed'] > 5:
    outWind = 'The wind is blowing from the ' + windDirections[windDirection] + ' at ' + windSpeed + 'Kph with gusts up to ' + windGust + 'Kph.'
else:
    outWind = 'Expect a gently breeze from the ' + windDirections[windDirection] + '.'
if data['wind']['windSpeed'] < 0.05:
    outWind = 'It is currently wind still.'

# Combining the response
out = outStd + ' ' + outRain + ' ' + outWind

print(out)
