import sys
import requests
import json 
 
city_id = ''
city = "Rivne"
cities = requests.get('http://bulk.openweathermap.org/sample/weather_16.json.gz')
with open('cities.json', encoding='utf-8', newline='') as f:
    # try:
        data = json.load(f)
        for item in data:
            if item['city']['name'] == city:
                print(item['city']['id'])
    # except Exception:
        # pass
    # finally:
        f.close()