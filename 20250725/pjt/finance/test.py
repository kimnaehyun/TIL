import requests
from dotenv import load_dotenv
import os
from pprint import pprint 

# load .env
load_dotenv()

API_KEY = os.environ.get('API_KEY')

url = f'https://api.openweathermap.org/data/2.5/weather?lat={35.09361644524314}&lon={128.85621638681846}&appid={API_KEY}' 
response = requests.get(url).json() 
pprint(response)

arr = []
dictionary = {'main' : response['main'], 'weather' : response['weather']}
for r in response :
    arr += [r]
pprint(dictionary)


url1 = f'https://api.openweathermap.org/data/2.5/weather?lat={35.09361644524314}&lon={128.85621638681846}&appid={API_KEY}&lang=kr' 
response1 = requests.get(url1).json() 
dictionary1 = {'main' : response1['main'], 'weather' : response1['weather']}

def to_celsius(kelvin):
    return round(kelvin - 273.15, 1)

translated_dict = {
    '주요정보': {
        '체감온도': dictionary1['main']['feels_like'],
        '지면기압': dictionary1['main']['grnd_level'],
        '습도': dictionary1['main']['humidity'],
        '기압': dictionary1['main']['pressure'],
        '해수면기압': dictionary1['main']['sea_level'],
        '현재온도': dictionary1['main']['temp'],
        '현재온도(섭씨)': to_celsius(dictionary1['main']['temp']),
        '최고온도': dictionary1['main']['temp_max'],
        '최고온도(섭씨)': to_celsius(dictionary1['main']['temp_max']),
        '최저온도': dictionary1['main']['temp_min'],
        '최저온도(섭씨)': to_celsius(dictionary1['main']['temp_min']),
    },
    '날씨': [
        {
            '설명': dictionary1['weather'][0]['description'],
            '아이콘': dictionary1['weather'][0]['icon'],
            '날씨코드': dictionary1['weather'][0]['id'],
            '날씨주제': dictionary1['weather'][0]['main'],
        }
    ]
}

pprint(translated_dict)