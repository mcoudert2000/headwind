import requests


weather_key = {'x-api-key':'4FdQRIr7sIZm6pvSzrBIY0hl4ln0qzRf'}

def get_weather(lat,lon,date,hour): # Input: Latitude, Longitude, YY-MM-DD, Hour
    station = get_nearby_station(lat,lon)
    return get_wind(get_weather_by_day(station,date)['data'][hour])

def get_weather_by_day(station,date): # Input: Latitude, Longitude, YYYY-MM-DD
    weather_params = {'station' : station, 'start' : date, 'end' :date, 'model': 1}
    out = requests.get("https://api.meteostat.net/v2/stations/hourly",
                    params = weather_params,                   
                    headers = weather_key)
    return(out.json())

def get_wind(weather):
    wind_dict = {'time':weather['time'],'wind_speed':weather['wspd'],'wind_direction':weather['wdir'],'temp':weather['temp']}
    return wind_dict

def get_nearby_station(lat,lon):
    params = {'lat':lat, 'lon':lon}
    out = requests.get('https://api.meteostat.net/v2/stations/nearby',
                       params = params,
                       headers = weather_key).json()['data'][0]['id']
    return out
