import numpy
import requests
import json



def get_lowest_point(data):
    for v in data["pointsmarket"].values():
        lowest_price = v.get("cost")
        return lowest_price

def get_set_value(data):
    data = data*10
    return data
        
