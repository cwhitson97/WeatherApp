from weather_api import get_today_weather, get_forecast_weather


zipcode = input("Enter a zipcode to get weather for ")
countrycode = input("Enter the country abreviation ")
print(get_today_weather(zipcode, countrycode))

# THIS IS SETTING THE LAT AND LONG FOR FORECAST. IT IS NEEDED TO BE ABLE TO RUN get_forecast_weather(lat, long)
city = get_today_weather(zipcode, countrycode)[0]
lon = get_today_weather(zipcode, countrycode)[4]
lat = get_today_weather(zipcode, countrycode)[5]

print(get_forecast_weather(lat, lon))
