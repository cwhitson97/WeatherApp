"""
Current issues: Needing to fix the library dependency issues.

Description: Found a decent program that pulls information from
yahoo weather and creates a string with the pertinent information.
Am currently in the process of manipulating the data to produce
an output that will be beneficial to our application.
"""
import sys
import urllib
from argparse import ArgumentParser
from xml.dom.minidom import parse

# Yahoo!'s limit on the number of days they will forecast
DAYS_LIMIT = 2
WEATHER_URL = 'http://xml.weather.yahoo.com/forecastrss?p=%s'
METRIC_PARAMETER = '&u=c'
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def get_weather(location_code, options):
    """
    Fetches weather report from Yahoo!
    :Parameters:
    -`location_code`: A five digit US zip code.
    -`days`: number of days to obtain forecasts
    :Returns:
    -`weather_data`: a dictionary of weather data
    """

    # Get the correct weather url.
    url = WEATHER_URL % location_code

    if options.metric:
        url = url + METRIC_PARAMETER

    # Parse the XML feed.
    try:
        dom = parse(urllib.urlopen(url))
    except Exception:
        return None

    # Get the units of the current feed.
    yunits = dom.getElementsByTagNameNS(WEATHER_NS, 'units')[0]

    # Get the location of the specified location code.
    ylocation = dom.getElementsByTagNameNS(WEATHER_NS, 'location')[0]

    # Get the current conditions.
    ycondition = dom.getElementsByTagNameNS(WEATHER_NS, 'condition')[0]

    # Hold the forecast in a hash.
    forecasts = []

    # Walk the DOM in order to find the forecast nodes.
    for i, node in enumerate(dom.getElementsByTagNameNS(WEATHER_NS, 'forecast')):

        # Stop if the number of obtained forecasts equals the number of requested days
        if i >= options.forecast:
            break
        else:
            # Insert the forecast into the forcast dictionary.
            forecasts.append({
                'date': node.getAttribute('date'),
                'low': node.getAttribute('low'),
                'high': node.getAttribute('high'),
                'condition': node.getAttribute('text')
            })

    # Return a dictionary of the weather that we just parsed.
    weather_data = {
        'current_condition': ycondition.getAttribute('text'),
        'current_temp': ycondition.getAttribute('temp'),
        'forecasts': forecasts,
        'units': yunits.getAttribute('temperature'),
        'city': ylocation.getAttribute('city'),
        'region': ylocation.getAttribute('region'),
    }

    return weather_data

def create_report(weather_data, options):
    """
    Constructs a weather report as a string.
    :Parameters:
    -`weather_data`: a dictionary of weather data
    -`options`: options to determine output selections
    :Returns:
    -`report_str`: a formatted string reporting weather
    """

    if weather_data is None:
        return None

    report = []

    if options.location:
        if options.verbose:
            # Add the location header.
            report.append("Location:")

        # Add the location.
        location_str = "%(city)s %(region)s\n" % weather_data
        report.append(location_str)

    if not options.nocurr:
        if options.verbose:
            # Add current conditions header.
            report.append("Current conditions:")

        # Add the current weather.
        curr_str = ""
        # degree = u"\xb0"
        degree = ""
        if not options.conditions:
            curr_str = curr_str + "%(current_temp)s" % weather_data + degree + \
                       "%(units)s" % weather_data

        if not options.conditions and not options.temperature:
            curr_str = curr_str + options.delim.decode('string_escape')

        if not options.temperature:
            curr_str = curr_str + "%(current_condition)s\n" % weather_data

        report.append(curr_str)

    if options.forecast > 0:
        if options.verbose:
            # Add the forecast header.
            report.append("Forecast:")

        # Add the forecasts.
        for forecast in weather_data['forecasts']:

            forecast['units'] = weather_data['units']

            forecast_str = """\
  %(date)s
    High: %(high)s%(units)s
    Low: %(low)s%(units)s
    Conditions: %(condition)s""" % forecast

            report.append(forecast_str)

    report_str = "\n".join(report)

    return report_str
