#!/usr/bin/python

import sys
import time
from twython import Twython
import pyowm
from pyowm import OWM
from pyowm import timeutils

location = 'Vienna,AT'
owm = OWM('weather api to be added later')
forecast = owm.daily_forecast(location)

früh = timeutils.tomorrow(8, 00)
mittag = timeutils.tomorrow(13, 00)
abend = timeutils.tomorrow(19, 00)


if forecast.will_be_sunny_at(früh):
        f = "sonnig"
elif forecast.will_be_rainy_at(früh):
        f = "regnerisch"
elif forecast.will_be_foggy_at(früh):
        f = "nebelich"
elif forecast.will_be_cloudy_at(früh):
        f = "bewölkt"
elif forecast.will_be_snowy_at(früh):
        f = "verschneit"
else:
        print ("Konnte keine Wetterdaten für den Morgen finden!")
        sys.exit()

if forecast.will_be_sunny_at(mittag):
        m = "sonnig"
elif forecast.will_be_rainy_at(mittag):
        m = "regnerisch"
elif forecast.will_be_foggy_at(mittag):
        m = "nebelich"
elif forecast.will_be_cloudy_at(mittag):
        m = "bewölkt"
elif forecast.will_be_snowy_at(mittag):
        m = "verschneit"
else:
        print ("Konnte keine Wetterdaten für Mittag finden!")
        sys.exit()

if forecast.will_be_sunny_at(abend):
        a = "sonnig"
elif forecast.will_be_rainy_at(abend):
        a = "regnerisch"
elif forecast.will_be_foggy_at(abend):
        a = "nebelich"
elif forecast.will_be_cloudy_at(abend):
        a = "bewölkt"
elif forecast.will_be_snowy_at(abend):
        a = "verschneit"
else:
        print ("Konnte keine Wetterdaten für den Abend finden!")
        sys.exit()

if f == m == a:
        wetter = ("Morgen wird es genztägig " + f + "."
elif f == m:
        wetter = "Morgen wird es vormittags " + f + " und zu späterer Stunde " + a + "."
elif m == a:
        wetter = "Morgen wird es in der früh " + f + " und ab der Mittagszeit " + m + "."
else:
        wetter = "Morgen wird es vormittags " + f + ", ab Mittag " + m + " und am Abend " + a + "."

#Twitter API
apiKey = 'to be added later'
apiSecret = 'to be added later'
accessToken = 'to be added later'
accessTokenSecret = 'to be added later'
twitter = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

tweetStr = wetter

twitter.update_status(status=tweetStr)

