# https://github.com/netology-code/py-homeworks-basic/tree/master/9.http.requests - задание 1
import requests

her_list = None
# her_list = ['Hulk', 'Captain America', 'Thanos']
r = requests.get(f'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
tmp = {'None': 0}

for i in r.json():
    if her_list is not None:
        if i['name'] in her_list:
            if int(i['powerstats']['intelligence']) > int(list(tmp.values())[0]):
                tmp = {i['name']: i['powerstats']['intelligence']}
    else:
        if int(i['powerstats']['intelligence']) > int(list(tmp.values())[0]):
            tmp = {i['name']: i['powerstats']['intelligence']}
        elif int(i['powerstats']['intelligence']) == int(list(tmp.values())[0]):
            tmp.update({i['name']: i['powerstats']['intelligence']})

if len(tmp) == 1:
    print(f'Max intellect have {list(tmp.keys())[0]} with {list(tmp.values())[0]}')
else:
    print('Max intellect have:')
    for i in tmp:
        print(f'{i} with {tmp[i]}')
