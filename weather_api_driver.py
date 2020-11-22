from weather_api import get_weather


zipcode = input("Enter a zipcode to get weather for ")
countrycode = input("Enter the country abreviation ")
print(get_weather(zipcode, countrycode))
