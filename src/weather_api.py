from configparser import ConfigParser
import requests
from datetime import datetime
import calendar


"""

WRITEUP FOR USE
---------------------



get_today_weather(ZIP, COUNTRY)
	-for this function, you have to pass in a zipcode and country abbreviation.
	-It returns "final" which is the city, country, temp_fahrenheit, weather, longitude, and latitude.
	-WARNING: this function has to be called before you can call get_forecast_weather(). This is due to get_forecast_weather() requiring the latitude and longitude gathered from get_today_weather(). This is bad programming practice but I am tired and want to sleep.
	-To get one individual item from final, like the temp_fahrenheit, you have to treat final like an array. To get the temp, you would type final[2] since the temp_fahrenheit variable is the 3rd variable in final.
	
dayofweek(DAY, MONTH, YEAR)
	-this is a simple function that will return the day of the week that is passed in from "DAY, MONTH, YEAR"
	-it is invoked in get_forecast_weather().
	
get_forecast_weather(LATITUDE, LONGITUDE)
	-This function requires a latitude and longitude variable be passed in. You obtain this from invoking get_today_weather() and assigning lat to final[5] and lon to final[4]. Again, this is bad practice but I am tired.
	-The api calls for a lat and long, that is why I am using it this way.
	-to get the weather for a certain day, it is similar to the array of get_today_weather() except it is a 2d array. Sunday through Saturday are 0-6 for the first part of the array and the weather is the second part of the array, 0-1.
	EXAMPLE: To get the weather and temp for monday, you type "get_forecast_weather(lat, lon)[1]" and if you just want the temperature for monday you would type "get_forecast_weather(lat, lon)[1][0]"

---------------------

"""

url = 'http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}'
url2 = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}'
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_today_weather(zip, country):
    result = requests.get(url.format(zip, country, api_key))
    if result:
        json = result.json()
        # (city, Country, temp_fahrenheit, weather)
        lon = json['coord']['lon']
        lat = json['coord']['lat']
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
        weather = json['weather'][0]['main']
        final = (city, country, temp_fahrenheit, weather, lon, lat)
        return final
    else:
        return None

def dayofweek(d, m, y):
	t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
	y -= m < 3
	dow = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	omega = ((y + int(y / 4) - int(y / 100) + int(y / 400) + t[m - 1] + d) % 7)
	
	return str(dow[omega])

def get_forecast_weather(lat, lon):
	result = requests.get(url2.format(lat, lon, api_key))
	if result:
		json = result.json()
		for x in range(0, 7):
			unixdate = int(json['daily'][x]['dt'])
			real_date = datetime.utcfromtimestamp(unixdate).strftime('%Y-%m-%d %H:%M:%S')
			real_date = real_date.split(" ", maxsplit=1)[0]
			year, month, day = (int(z) for z in real_date.split('-'))
			if dayofweek(day, month, year) == 'Sunday':
				temp_kelvin = json['daily'][x]['temp']['day']
				temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
				weather = json['daily'][x]['weather'][0]['main']
				sunday_weather = (temp_fahrenheit, weather)
			elif dayofweek(day, month, year) == 'Monday':
				temp_kelvin = json['daily'][x]['temp']['day']
				temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
				weather = json['daily'][x]['weather'][0]['main']
				monday_weather = (temp_fahrenheit, weather)
			elif dayofweek(day, month, year) == 'Tuesday':
				temp_kelvin = json['daily'][x]['temp']['day']
				temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
				weather = json['daily'][x]['weather'][0]['main']
				tuesday_weather = (temp_fahrenheit, weather)
			elif dayofweek(day, month, year) == 'Wednesday':
				temp_kelvin = json['daily'][x]['temp']['day']
				temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
				weather = json['daily'][x]['weather'][0]['main']
				wednesday_weather = (temp_fahrenheit, weather)
			elif dayofweek(day, month, year) == 'Thursday':
				temp_kelvin = json['daily'][x]['temp']['day']
				temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
				weather = json['daily'][x]['weather'][0]['main']
				thursday_weather = (temp_fahrenheit, weather)
			elif dayofweek(day, month, year) == 'Friday':
				temp_kelvin = json['daily'][x]['temp']['day']
				temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
				weather = json['daily'][x]['weather'][0]['main']
				friday_weather = (temp_fahrenheit, weather)
			elif dayofweek(day, month, year) == 'Saturday':
				temp_kelvin = json['daily'][x]['temp']['day']
				temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
				weather = json['daily'][x]['weather'][0]['main']
				saturday_weather = (temp_fahrenheit, weather)
				
		week_outlook = [sunday_weather, monday_weather, tuesday_weather, wednesday_weather, thursday_weather, friday_weather, saturday_weather]
		return week_outlook;
	else:
		return None;
