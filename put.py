import requests


def get_upload_link():
    with open('token.txt', 'r') as opened_file:
        token = opened_file.read()
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': 'disk:/Загрузки/govno.txt',
              'limit': '10',
              'overwrite': 'false'}
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    r = requests.get(url=url, headers=headers, params=params)
    k = r.json()
    print(k)
    link = k['href']
    print(link)
    return link


def upload_file(file, link):
    with open('token.txt', 'r') as opened_file:
        token = opened_file.read()
    headers = {'Authorization': f'OAuth {token}'}
    params = {'overwrite': 'false'}
    with open(file, mode='r') as opened_file:
        t = requests.put(url=link, headers=headers, params=params, data='Gbsdfasdfasdfasdfasdfasdfasdf')
        print(t)

upload_file('test.txt', get_upload_link())

# with open('test.txt', mode='r') as opened_file:
#     r = requests.put('https://uploader20o.disk.yandex.net:443/upload-target/20221004T144743.459.utd.2i01vbtdzwknsppxyreuxkbnr-k20o.572205', opened_file)
#     print(r)