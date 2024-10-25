import requests
import reverse_geocoder as rg
import geocoder as g
import haversine as hs
from dataclasses import dataclass
from math import *


@dataclass
class Point:
    x: float
    y: float

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9e5ec70ed6b491f5f8b6d1fc06fad08c'
accesstoken = "'pk.eyJ1IjoidmluYXlhazEyMDAiLCJhIjoiY2xhOXo3YXVnMDJ2azNybzh3ODBpanF3ayJ9.3wPa3e8CFCAuj0lU3ZJv9A'"


start=[76.41346,30.33212]
end = [77.02252,28.45900]
locations = []

dist = hs.haversine([start[1], start[0]], [end[1], end[0]])


pointA = Point(start[0], start[1])
pointB = Point(end[0], end[1])

if dist<=500:
    numberofPoints=10

    for i in range(0, numberofPoints):
        locations.append(Point((abs(pointA.x-pointB.x)/10)*i+pointB.y,(abs(pointA.y - pointB.y)/numberofPoints)*i+pointB.y))


print(locations)


# cities = ['Patiala', 'Chandigarh', 'Ambala']
# 
# TempSum=0
# 
# for city in cities:
    # Response = requests.get(url.format(city))
    # data = eval(Response.text)
    # print(data['weather'][0]['main'])

