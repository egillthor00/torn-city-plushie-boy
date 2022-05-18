import numpy
import requests
import json

def get_point_market_data(API_KEY):
    point_market_request = requests.get("https://api.torn.com/market/?selections=pointsmarket&key=" + API_KEY)
    point_market_d = json.loads(point_market_request.text)
    return point_market_d

def get_lowest_point(data):
    for v in data["pointsmarket"].values():
        lowest_price = v.get("cost")
        return lowest_price

def get_set_value(data):
    data = data*10
    return data
        
