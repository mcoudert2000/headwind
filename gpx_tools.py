#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import branca.colormap as cm
import matplotlib
import polyline
import folium
import math
import gpxpy
import gpxpy.gpx
import numpy as np
from weather_tools import get_weather

def get_start_position(gpx):
    start_point = gpx.tracks[0].segments[0].points[0]
    return start_point.latitude, start_point.longitude, str(start_point.time.date()), int(start_point.time.time().hour)

# gpx_file = open('/Users/matthewcoudert/Downloads/activity_5852303688.gpx', 'r')

#gpx = gpxpy.parse(gpx_file)

#lat, lon, date, hour = get_start_position(gpx_file)

def get_ratio(lat_lon, wind_direc):
    if(len(lat_lon) <= 1):
        return []
    i = 1
    ratio = []
    while(True):
        first = lat_lon[i-1]
        second = lat_lon[i]
        y = math.sin(first[1]-second[1]) * math.cos(second[0])
        x = math.cos(first[0])*math.sin(second[0]) - math.sin(first[0])*math.cos(second[0])*math.cos(first[1]-second[1])
        r = math.atan2(y, x)
        deg = (r*180/math.pi + 360) % 360
        diff = wind_direc - deg
        ratio.append(abs(diff))
        i += 1
        if(i == len(lat_lon)):
            return ratio

# OPTION 2
def add_to_map(lat_lon, ratio, world_map): 
    minima = min(ratio)
    maxima = max(ratio)
    test = cm.LinearColormap(['red','green'], vmin=minima, vmax=maxima)
    colorline = folium.ColorLine(lat_lon, ratio, colormap = test, nb_steps=len(lat_lon), weight = 4, opacity=1)
    world_map.add_child(colorline)

def get_lat_lon(gpx):
    for track in gpx.tracks:
        for segment in track.segments:
            lat_lon = [(point.latitude, point.longitude) for point in segment.points]
    return lat_lon

def generate_map(gpx_file):  
    world_map = folium.Map()
    
    gpx = gpxpy.parse(gpx_file)
    lat_lon = get_lat_lon(gpx)
    lat, lon, date, hour = get_start_position(gpx)
    weather = get_weather(lat,lon,date,hour)
    wind_direction = weather['wind_direction']
    
    ratio = get_ratio(lat_lon, wind_direction) 
    add_to_map(lat_lon, ratio, world_map)
    world_map.fit_bounds(world_map.get_bounds())
    # world_map.save('/Users/matthewcoudert/Maths/#Headwind/#Headwind/maps/mymap.html')
    return world_map._repr_html_()
