from datetime import datetime, date, time
import requests

dt_now = datetime.now()

print(f'Current date and time: {dt_now}')
time = int(datetime.timestamp(dt_now)) - int(datetime.timestamp(dt_now)) % 86400
print(f'Current date and time in seconds from 01.01.1970: {time}')
url_time = time - 86400 * 2

url = 'https://api.stackexchange.com//2.3/questions'
headers = {}
params = {'order': 'desc',
          'min': url_time,
          'sort': 'activity',
          'site': 'stackoverflow'}
r = requests.get(url=url, params=params, headers=headers)
print(f'Status code: {r.status_code}')
jsoned = r.json()
# print(jsoned)
for i in jsoned['items']:
    if 'python' in i['tags']:
        # print(i)
        print(f"{i['title']}:")
        print(f"    {i['creation_date']}")
        print(f"    {i['link']}")
