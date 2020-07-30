import requests

with open('C:/Users/li/Downloads/dataset_3378_2.txt', 'r') as f:
    url = f.readline().strip()

r = requests.get(url)

l = r.text.splitlines()
print(len(l))