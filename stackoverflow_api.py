from datetime import datetime, date, time
import requests

dt_now = datetime.now()

print(f'Current date and time: {dt_now}')
time = int(datetime.timestamp(dt_now))
time = time - time % 86400
print(time)
print(f'Current date and time in seconds from 01.01.1970: {time}')
time = time - 86400 * 2 - 10800
print('====================')
print(datetime.fromtimestamp(time))
print('====================')



url = 'https://api.stackexchange.com//2.3/questions'
page = 1
headers = {}
params = {'order': 'desc',
          # 'min': time,
          'sort': 'activity',
          'site': 'stackoverflow',
          'tagged': 'python',
          # 'creation_date': time,
          'fromdate': time,
          'todate': time + 86400,
          'pagesize': 100,
          'page': page}
# r = requests.get(url=url, params=params, headers=headers)
# print(f'Status code: {r.status_code}')
# print('====================')
# jsoned = r.json()
# print(jsoned)
# print('====================')
counter = 1
while True:
    params = {'order': 'desc',
              # 'min': time,
              'sort': 'activity',
              'site': 'stackoverflow',
              'tagged': 'python',
              # 'creation_date': time,
              'fromdate': time,
              'todate': time + 86400,
              'pagesize': 100,
              'page': page}
    r = requests.get(url=url, params=params, headers=headers)
    if r.status_code == 200:

        jsoned = r.json()
        print(jsoned)
        # counter = 1
        print(f'        PAGE: {page}')
        for i in jsoned['items']:
            # if 'python' in i['tags']:
                # print(i)
            print(f"{counter}: {i['title']}:")
            # print(f"    {datetime.fromtimestamp(i['creation_date'])}")
            # print(f"    {i['link']}")
            counter += 1
        if jsoned['has_more'] == True:
            page += 1

        else:
            print('No more pages')
            break
    else:
        print('BORODA!!!!!!')
        print(r.status_code)
        print(r.text)
        break
