import requests
from datetime import datetime
import json

current_datetime = datetime.now()

key = "38185f434c3df6799b22a707a008ff02"
url = 'https://currate.ru/api/?get=rates&pairs=USDRUB&key=38185f434c3df6799b22a707a008ff02'
response = requests.get(url)

data = response.json()
usd_rub = data['data']['USDRUB']

rub = float(input("Введите сумму в рублях для пересчета на доллары США"))
result = float(rub) / float(usd_rub)
print("Получилось ", result, " долларов США намомент расчета", current_datetime)
