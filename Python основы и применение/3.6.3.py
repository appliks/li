import requests
import json

with open('C:/Users/li/Downloads/dataset_24476_3.txt') as file:
    for number in file:
        number = number.strip()
        params = {'default': 'Boring number is boring', 'json': True}
        url = 'http://numbersapi.com/{}/math'.format(number)
        res = requests.get(url, params=params).text
        data = json.loads(res)
        if 'Boring' in data['text']:
            print('Boring')
        else:
            print('Interesting')