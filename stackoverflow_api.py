from datetime import datetime, date, time
import requests

dt_now = datetime.now()

# def print_list(list):
#     for i in list:
#         if type(i) is dict:
#             print('list_dict')
#             print_dict(i)
#         elif type(i) is str:
#             print('list_str')
#             print(list)
#             return
#         else:
#             print(i)
#
# def print_dict(dict):
#     for i in dict:
#         if type(dict[i]) is list:
#             print('dict_list')
#             print_list()
#         # elif type(dict[i]) is str:
#         #     print('dict_str')
#         #     print(dict)
#         else:
#             print(i, dict[i])
def pd(dict):
    for i in dict:
        if i == 'tags' and 'python' in dict[i]:
            print(dict[i])
        # print(f'{i}: {dict[i]}')

def pl(list):
    for i in list:
        if type(i) is dict:
            pd(i)
        else:
            print(i)

print(dt_now)
time = int(datetime.timestamp(dt_now)) - int(datetime.timestamp(dt_now)) % 86400
print(time)
url_time = time - 86400 * 2

url = 'https://api.stackexchange.com//2.3/questions'
headers = {}
params = {'order': 'desc',
          'min': url_time,
          'sort': 'activity',
          'site': 'stackoverflow'}
r = requests.get(url=url, params=params, headers=headers)
print(r)

# print(r.text)
jsoned = r.json()
print(jsoned)

for i in jsoned:
    if type(jsoned[i]) is list:
        pl(jsoned[i])
    print(f'{i}: {jsoned[i]}')

# for i in jsoned:
#     if type(jsoned[i]) is dict:
#         print('g')
#         print_dict(i)
#     if type(jsoned[i]) is list:
#         print('o')
#         print_list(i)
#     else:
#         print('v')
#         print(i)

    # print(i, jsoned[i])

# r = requests.get('https://api.stackexchange.com//2.3/questions?order=desc&min=1665014400&sort=activity&site=stackoverflow')

# dt = datetime.today()
# dt = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
# print(dt)
# tt = dt.timetuple()
# dt_ord = dt.toordinal()
# print(dt_ord)
# print(datetime.fromordinal(dt_ord))




# r = requests.get('https://api.stackexchange.com//2.3/questions?order=desc&min=1665014400&sort=activity&site=stackoverflow')
#

