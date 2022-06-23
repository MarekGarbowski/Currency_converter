from urllib.request import urlopen
import json

url = "http://api.nbp.pl/api/exchangerates/tables/a/today/?format=json"

response = urlopen(url)
data_json = json.loads(response.read())

y = 0
for word in data_json:
    for x in word.values():
        y += 1
        if y == 4:
            for a in x:
                # print(a)
                print(f'Currency: {a["currency"]}, code {a["code"]}, mid price is: {a["mid"]} PLN')
