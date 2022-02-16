import urllib.request
import re
from bs4 import *
from googlesearch import search


def main():
    # to search
    query = "london weather"
    url_list = []
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(j)
        url_list.append(j)
    print("-" * 20)

    """
	https://www.weather.com/wx/today/?lat=51.51&lon=-0.13&locale=en_US&par=google
	https://weather.com/weather/today/l/f31a113995a7af63e126d831556babe68b6e22feecd029c3c33a55b1d31cfda1
	https://weather.com/weather/today/l/London+England+United+Kingdom?canonicalCityId=a4cb96aeab4c5bbc8f739c9195747c0abd46dbe68a101384f78303da71c0f417
	https://www.wunderground.com/forecast/gb/london
	https://www.runnersworld.com/uk/news/a37830992/london-marathon-weather-forecast/
	https://www.bbc.com/weather/2643743
	https://www.accuweather.com/en/gb/london/ec4a-2/weather-forecast/328328
	https://www.accuweather.com/en/gb/london/ec4a-2/hourly-weather-forecast/328328
	https://www.metoffice.gov.uk/weather/forecast/gcpvj0v07
	https://www.theweathernetwork.com/ca/weather/ontario/london
	"""

    # url = 'https://weather.com/weather/today/l/f31a113995a7af63e126d831556babe68b6e22feecd029c3c33a55b1d31cfda1'
    # 有时候无法访问，被拒绝，因为没付费
    url = url_list[0]
    html = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(html, "html.parser")
    sum = []
    # Retrieve all of the anchor tags
    tags = soup("span")
    for tag in tags:
        # Look at the parts of a tag
        y = str(tag)
        x = re.findall("[0-9]+", y)
        for i in x:

            sum.append(i)
    print(sum)


####
"""
59° Partly Cloudy
"""
wheather_R = "59° Partly Cloudy"
###
