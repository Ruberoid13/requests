import requests


def get_upload_link(file):
    with open('token.txt', 'r') as opened_file:
        token = opened_file.read()
    headers = {'Authorization': f'OAuth {token}'}
    path = f'disk:/Загрузки/{file}'
    params = {'path': path,
              'overwrite': 'false'}
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    req = requests.get(url=url, headers=headers, params=params)
    if req.status_code == 200:
        jsoned_req = req.json()
        upload_link = jsoned_req['href']
        return upload_link
    elif req.status_code == 409:
        print('Error: file already exists!')
        return None
    else:
        print('Error! Something goes wrong!')
        return None


def upload_file(file, upload_link):
    if upload_link is not None:
        with open('token.txt', 'r') as opened_file:
            token = opened_file.read()
        headers = {'Authorization': f'OAuth {token}'}
        params = {'overwrite': 'false'}
        with open(file, mode='r') as opened_file:
            req = requests.put(url=upload_link, headers=headers, params=params, data=opened_file.read())
        if req.status_code == 201:
            print('File uploaded successfully!')
        else:
            print('Something goes wrong!')


upload_file('test.txt', get_upload_link('test.txt'))
