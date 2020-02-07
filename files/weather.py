#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, json, datetime

url = "https://johanbove.info/weather.php?key=eDaC9W"
response = urllib.urlopen(url)
data = json.loads(response.read())

# Expects this json object:
# `{u'temp': 16.5, u'rain': {u'intensity': 0.1166, u'probability': 0.11}, u'humidity': 0.89, u'pressure': 1010.76, u'location': {u'lat': 51.23, u'lon': 6.78}, u'wind': {u'speedKPH': 4.89, u'windSpeed': 4.89, u'windGust': 4.89, u'dir': u'SSW', u'windBearing': 203}, u'desc': u'Overcast'}`

now = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
location = str(data["location"]["lat"]) + ", " + str(data["location"]["lon"])

# Checks for Düsseldorf's lat and long
if data["location"]["lat"] == 51.23 and data["location"]["lon"] == 6.78:
    locationName = "Düsseldorf"
else:
    locationName = location

temp = str(data["temp"]) + "°C"
desc = str(data["desc"]).lower()

if desc == 'clear':
    desc = desc + ' skies'


rainIntensity = str(data["rain"]["intensity"])
rainProbability = str(data["rain"]["probability"] * 100)
windSpeed = str(data["wind"]["windSpeed"])
windGust = str(data["wind"]["windGust"])
windDirection = str(data["wind"]["dir"])

windDirection = windDirection.replace("N", "North")
windDirection = windDirection.replace("E", "East")
windDirection = windDirection.replace("W", "West")
windDirection = windDirection.replace("S", "South")

# debug
# print data

# Generating a humanized phrase
outStd = (
    "Look for " + desc + " in " + locationName + " with a temperature of " + temp + "."
)

# Rain
if data["rain"]["probability"] > 0.05:
    outRain = (
        "There is a "
        + rainProbability
        + "% chance of rain and you can expect about "
        + rainIntensity
        + "mm."
    )
else:
    outRain = "No rain is expected at this time."

# Wind
if data["wind"]["windSpeed"] > 5:
    outWind = (
        "The wind is blowing from the " + windDirection + " at " + windSpeed + "Kph"
    )
    if data["wind"]["windGust"] != data["wind"]["windSpeed"]:
        outWind = outWind + " with gusts up to " + windGust + "Kph."
    else:
        outWind = outWind + "."
else:
    outWind = "Expect a gently breeze from the " + windDirection + "."
if data["wind"]["windSpeed"] < 0.05:
    outWind = "It is currently wind still."

# Combining the response
out = outStd + " " + outRain + " " + outWind

print(out)
