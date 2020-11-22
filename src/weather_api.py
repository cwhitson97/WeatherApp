from configparser import ConfigParser
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}'
config_file = '../config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(zip, country):
    result = requests.get(url.format(zip, country, api_key))
    if result:
        json = result.json()
        # (zip, Country, temp_fahrenheit, icon, weather)
        zip = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
        weather = json['weather'][0]['main']
        final = (zip, country, temp_fahrenheit, weather)
        return final
    else:
        return None

