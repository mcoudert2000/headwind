#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 11:43:20 2021

@author: matthewcoudert
"""

import requests
import pandas as pd

keys = {'client_id':54363,'client_secret':'554b01c327e3ae0917b2a65207f0beeda39a47a5',
        'refresh_token':'41bfd5abd9488d49e65b523bdee74d68b72e7079','grant_type':'refresh_token'}

def refresh_access_token():
    access = requests.post('http://www.strava.com/oauth/token',
                           params = keys).json()['access_token']
    return(access)

token = 'ed9efe89c301eb8feae1553414dff60235118f7b'

def get_activities():
    col_names = ['id','type']
    all_activities = pd.DataFrame(columns=col_names)
    page = 1
    while(True):
        
        params = {'access_token':token,'per_page':200,'page':page}
        activities = requests.get('https://www.strava.com/api/v3/athlete/activities',
                              params = params).json()
        if(not activities):
            break
        
        for x in range(len(activities)):
            all_activities.loc[x+(page-1)*200,'id'] = activities[x]['id']
            all_activities.loc[x+(page-1)*200,'type'] = activities[x]['type']
        page = page + 1
        print(page)
    return(all_activities)

def get_40_activities():
    col_names = ['id','type']
    all_activities = pd.DataFrame(columns=col_names)
    page = 1
    params = {'access_token':token,'per_page':40,'page':page}
    activities = requests.get('https://www.strava.com/api/v3/athlete/activities',
                              params = params).json()
    for x in range(len(activities)):
        all_activities.loc[x+(page-1)*40,'id'] = activities[x]['id']
        all_activities.loc[x+(page-1)*40,'type'] = activities[x]['type']
    return(all_activities)
            
    
def get_rides():
    activities = get_40_activities()
    rides = activities[activities.type == 'Ride']
    col_names = ['id','name','distance','start_date','start_latitude','start_longitude',
                 'polyline','summary_polyline']
    ride_data = pd.DataFrame(columns = col_names)
    i = 0 
    for ride_id in rides['id']:
        r = requests.get('https://www.strava.com/api/v3/activities/' + str(ride_id),
                         params = {'access_token':token}).json()
        ride = dict.fromkeys(col_names, None)
        ride['id'] = ride_id
        ride['name'] = r['name']
        ride['distance'] = r['distance']
        ride['start_date'] = r['start_date']
        ride['start_latitude'] = r['start_latitude']
        ride['start_longitude'] = r['start_longitude']
        ride['polyline'] = r['map']['polyline']
        ride_data = ride_data.append(ride,ignore_index = True)
        i += 1
    return(ride_data)

rides = get_rides()

        
        
        
        
        