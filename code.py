# This code uses the help of google maps API for getting the location of specified address when entered with longitude and latitude
# This syntax and url format is decided by google and we will get a JSON file

#This code is not running as now we are required an API key from google to use it, But the method is same pretty well
import urllib.request, urllib.parse, urllib.error
import json                                               # importing the module and stuff       
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'       # We will concatinate this string with the address that we will enter

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break                      #on hitting "enter" the loop will stop

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)        #Concatinating the complete url by encoding it in the url format for the search

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)        # It will open the url but it will not read it
    data = uh.read().decode()                           #Now this will turn the UTF-8 format from the internet in the the unicode format fot the python
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)                       # this loads loads the data in to js as a python dictionary or list depending on the format recieved
    except:                                          # 4 and gives us to print the data that actually we get from the web in the same format
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':     #this will check for the errors by the status which is there in the data recieved
        print('==== Failure To Retrieve ====')                  #is 'OK' or not and do accordingly
        print(data)
        continue

    print(json.dumps(js, indent=4))                        #this dumps is opposite of loads which dictionary that includes arrays and pretty print with indent of
                                                           # 4 and gives us to print the data that actually we get from the web in the same format
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)