from pyfiglet import Figlet
import urllib2
import json
import calcs

forms = calcs.calcs()
f = Figlet(font='slant')
print f.renderText('Python Weather')

openWeatherUrl = "http://api.openweathermap.org/data/2.5/weather?"
apiKey="" ##YOUR API KEY HERE
def takeData():
	try:
	    #########IP_TRACKING############
	    #Get data from the client via IP and store data via JSON into variables
	    #We suppose that both of webpages are still working, for IP tracking
	    pageOne = True
	    pageTwo = True
	    try:
    	        response_client = json.loads(urllib2.urlopen('https://freegeoip.net/json', None, 2.5).read())#Store data in JSON
		pageTwo = False
		pageOne = True
		#print "Page one"
	    except urllib2.HTTPError, e:#Another option if freegeoip fails
		response_client = json.loads(urllib2.urlopen('http://ip-api.com/json').read())
		pageOne = False
		pageTwo = True
		#print "PageTwo"
	    except urllib2.URLError, e:
	        response_client = json.loads(urllib2.urlopen('http://ip-api.com/json').read())
		pageOne = False
		PageTwo = True	
	    if pageOne == True:
		    cityCli = response_client['city']
                    print "Localization: " + cityCli
		    cityZip = response_client['zip_code']
		    cityLatitude = response_client['latitude']
		    cityLongitude = response_client['longitude']
		    #print cityLatitude, cityLongitude
		    countryCode = (response_client['country_code']).lower()
	    if pageTwo == True:
		    cityCli = response_client['city'] 
		    cityLatitude = response_client['lat']
		    cityLongitude = response_client['lon']
	    ##########WEATHER###############
            #Making the url for call to openweather page
	    tail = "lat=" + str(cityLatitude) + "&lon=" + str(cityLongitude) +"&appid=" + apiKey
	    urlFinal = openWeatherUrl + tail
	    response_weather = json.loads(urllib2.urlopen(urlFinal).read())
    	    tempData = response_weather['main']['temp']#Y de dicha parte del array selecciono el objeto main y especifico que quiero temp de dicho objeto
	    humiData = response_weather['main']['humidity']
	    windData = response_weather['wind']['speed']
	    weatherData = response_weather['weather'][0]
	    weatherDescOne = weatherData['main']
	    weatherDescTwo = weatherData['description']

	    temp = int(tempData)
	    temp_in_cel = forms.kelvin_to_celsius(temp)
	    return temp_in_cel, weatherDescOne, weatherDescTwo, humiData, windData
    
	except urllib2.HTTPError, e: 
	        if e.code == 503:
		    print "Error 503"
		else:
		    print "Unknown error"

tmp, weaDescOne, weaDescTwo, humiData, windData = takeData()
print "Temperaure: "+ str(tmp)
print "Weather description one: "+  weaDescOne
print "Weather description two: "+  weaDescTwo
print "Humidity: "+ str(humiData)
print "Wind speed: "+ str(windData)
