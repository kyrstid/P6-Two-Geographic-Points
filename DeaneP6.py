# KDeaneP6
#Programmer: Kyrsti Deane
#Email: kdeane1@cnm.edu
#Purpose: distance between two points given longitaude & latitude in decimal degrees

# Import Statements
import math
from math import radians, cos, sin, atan, sqrt

#Functions
def header():
    print(" Welcome to my Geo Calculator.")

def get_location():
    lat = float(input('Please enter a latitude in decimal degrees: '))
    lon = float(input('Please enter a longitude in decimal degrees: '))
    return (lat, lon)

def distance(origin, destination):
    '''Code obtained from https://gist.github.com/rochacbruno/2883505'''
    lat1, lon1 = map(math.radians, origin)
    lat2, lon2 = map(math.radians, destination)
    r = 3956  #radius in miles

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan(sqrt(a))
    d = c * r
    return d

#Main program
header()
doanother = 'y'
while doanother == 'y':
    origin = get_location()
    destination = get_location()
    distance(origin, destination)
    print('The distance between', origin, 'and' ,\
           destination, 'is', round(distance(origin, destination),2), 'miles.')
    doanother = input('Do another (y/n) ?') 
    if doanother == 'n':
        print("Thanks for trying my GEO Calculator. Goodbye!")
        break
