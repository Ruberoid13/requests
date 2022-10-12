from datetime import datetime, date
import requests

dt_now = datetime.now()
time = int(datetime.timestamp(dt_now)) - int(datetime.timestamp(dt_now)) % 86400 - 10800
url = 'https://api.stackexchange.com//2.3/questions'
page = 1
headers = {}
counter = 1
print('====================')
print(f'List of posts created in last two days from: '
      f'{date.fromtimestamp(time - 86400 * 2)} to {date.fromtimestamp(time)}:')
while True:
    params = {
              'site': 'stackoverflow',
              'tagged': 'python',
              'fromdate': time - 86400 * 2,
              'todate': time,
              'pagesize': 100,
              'page': page
            }
    r = requests.get(url=url, params=params, headers=headers)
    if r.status_code == 200:
        jsoned = r.json()
        print(f'====================\nPAGE: {page}\n====================')
        for i in jsoned['items']:
            print(f"{counter}: {i['title']}:")
            print(f"    {datetime.fromtimestamp(i['creation_date'])}")
            print(f"    {i['link']}")
            counter += 1
        if jsoned['has_more'] == True:
            page += 1
        else:
            print(f'====================\nEnd of list\n====================')
            break
    else:
        print('Something goes wrong!')
        print(r.status_code)
        print(r.text)
        break
