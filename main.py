#!/usr/bin/python

import sys
import time
from twython import Twython
import pyowm
from pyowm import OWM
from pyowm import timeutils

location = 'Vienna,AT'
owm = OWM('weather api from openweathermap here')
forecast = owm.daily_forecast(location)

früh = timeutils.tomorrow(8, 00)
mittag = timeutils.tomorrow(13, 00)
abend = timeutils.tomorrow(19, 00)


if forecast.will_be_sunny_at(früh):
        f_adj = "sonnig"
        f_nom = "Sonne"
elif forecast.will_be_rainy_at(früh):
        f_adj = "regnerisch"
        f_nom = "Regen"
elif forecast.will_be_foggy_at(früh):
        f_adj = "nebelich"
        f_nom = "Nebel"
elif forecast.will_be_cloudy_at(früh):
        f_adj = "bewölkt"
        f_nom = "Wolken"
elif forecast.will_be_snowy_at(früh):
        f_adj = "verschneit"
        f_nom = "Schnee"
else:
        print ("Konnte keine Wetterdaten für den Morgen finden!")
        sys.exit()

if forecast.will_be_sunny_at(mittag):
        m_adj = "sonnig"
        m_nom = "Sonne"
elif forecast.will_be_rainy_at(mittag):
        m_adj = "regnerisch"
        m_nom = "Regen"
elif forecast.will_be_foggy_at(mittag):
        m_adj = "nebelich"
        m_nom = "Nebel"
elif forecast.will_be_cloudy_at(mittag):
        m_adj = "bewölkt"
        m_nom = "Wolken"
elif forecast.will_be_snowy_at(mittag):
        m_adj = "verschneit"
        m_nom = "Schnee"
else:
        print ("Konnte keine Wetterdaten für Mittag finden!")
        sys.exit()

if forecast.will_be_sunny_at(abend):
        a_adj = "sonnig"
        a_nom = "Sonne"
elif forecast.will_be_rainy_at(abend):
        a_adj = "regnerisch"
        a_nom = "Regen"
elif forecast.will_be_foggy_at(abend):
        a_adj = "nebelich"
        a_nom = "Nebel"
elif forecast.will_be_cloudy_at(abend):
        a_adj = "bewölkt"
        a_nom = "Wolken"
elif forecast.will_be_snowy_at(abend):
        a_adj = "verschneit"
        a_nom = "Schnee"
else:
        print ("Konnte keine Wetterdaten für den Abend finden!")
        sys.exit()

if f_adj == m_adj == a_adj:
        wetter = ("Der morgige Tag wird ganztägig überwiegend " + f_adj + "."
elif f_adj == m_adj:
        wetter = "Der morgige Tag beginnt überwiegend " + f_adj + " mit " + a_nom + " in den Abendstunden."
elif m_adj == a_adj:
        wetter = "Der morgige Tag beginnt überwiegend " + f_adj + " mit " + m_nom + " ab der Mittagszeit."
else:
        wetter = "Der morgige Tag beginnt überwiegend " + f_adj + ", mit " + m_nom + " um die Mittagszeit und " + a_nom + " in den Abendstunden."

#Twitter API
apiKey = 'to be added later'
apiSecret = 'to be added later'
accessToken = 'to be added later'
accessTokenSecret = 'to be added later'
twitter = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

tweetStr = wetter

twitter.update_status(status=tweetStr)

