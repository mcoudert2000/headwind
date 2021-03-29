#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:35:13 2020

@author: matthewcoudert
"""

import requests

weather_key = {'x-api-key':'5ojBayWjBWReRKVaecaN1Rtz92nEHYOD'}

def get_weather_by_day(lat,lon,date): # Input: Latitude, Longitude, YYYY-MM-DD
    weather_params = {'lat':lat,'lon':lon,'start':date,'end':date}
    out = requests.get("https://api.meteostat.net/v2/point/hourly",
                    params = weather_params,                   
                    headers = weather_key)
    return(out.json())

def get_weather(lat,lon,date,hour): # Input: Latitude, Longitude, YY-MM-DD, Hour
    return get_weather_by_day(lat,lon,date)['data'][hour]

def get_wind(weather):
    wind_dict = {'time':weather['time'],'wind_speed':weather['wspd'],'wind_direction':weather['wdir']}
    return wind_dict

test_weather = get_weather(52.4118,1.7776,'1999-11-03',9)