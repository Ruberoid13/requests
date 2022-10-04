# https://github.com/netology-code/py-homeworks-basic/tree/master/9.http.requests - задание 2
import requests
import json


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        # https://yandex.ru/dev/disk/poligon/


def print_list_old(list):
    for i in list:
        if type(i) is dict:
            print_dict(i)
        else:
            print(i)


def print_list(list):
    for i in list:
        if type(i) is dict:
            print('    {')
            print_dict(i)
            print('    }')
        else:
            print(i)


def print_dict(in_dict):
    for i in in_dict:
        if type(in_dict[i]) is list:
            print_list(in_dict[i])
        else:
            if i == 'name' or i == 'type' or i == 'path' or i == 'file':
                print(f'{i}: {in_dict[i]}')


def print_list_l(list, in_list):
    for i in list:
        if type(i) is dict:
            # print('    {')
            print_dict_l(i, in_list)
            # print('    }')
        else:
            # print(i)
            pass


def print_dict_l(in_dict, in_list):
    out_list = in_list
    for i in in_dict:
        if type(in_dict[i]) is list:
            print_list_l(in_dict[i], in_list)
        else:
            if i == 'name':
                out_list.append(in_dict[i])
                # print(f'{i}: {in_dict[i]}')
    return out_list

def get_files_list(text):
    files_list = []
    d = json.loads(text)
    for k in d:
        if type(d[k]) is list:
            print_list_l(k, files_list)
            pass
        if type(d[k]) is dict:
            print_dict_l(d[k], files_list)
            pass
        else:
            # print(k)
            pass
    # print(files_list)
    return files_list

def get_resources():
    with open('token.txt', 'r') as opened_file:
        token = opened_file.read()
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': 'disk:/Загрузки'}
    url_disk = 'https://cloud-api.yandex.net/v1/disk'
    url = 'https://cloud-api.yandex.net/v1/disk/resources'

    r = requests.get(url=url, headers=headers, params=params)
    print(r.url)
    print('\nСодержимое папки "Загрзки":')
    for i in get_files_list(r.text):
        print(f'{i}')

def print_files_list():
    with open('token.txt', 'r') as opened_file:
        token = opened_file.read()
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': 'disk:/Загрузки',
              'limit': '10'}
    url = 'https://cloud-api.yandex.net/v1/disk/resources/files'

    r = requests.get(url=url, headers=headers, params=params)
    print(r.url)
    jtext = json.loads(r.text)
    print(json.dumps(jtext, indent=2))



print_files_list()
# text = r.text
# d = json.loads(text)
# print(d)
# print(json.dumps(d, indent=2))

# for k in d:
#     if type(d[k]) is list:
#         print_list(k)
#     if type(d[k]) is dict:
#         print_dict(d[k])
#     else:
#         print(k)

# if __name__ == '__main__':
#     # Получить путь к загружаемому файлу и токен от пользователя
#     path_to_file = ...
#     token = 'y0_AgAAAAAWNWbmAADLWwAAAADQEBgkRZOGOrA2TPmuvGoi4lP1bkBHVX8'
#     uploader = YaUploader(token)
#     result = uploader.upload(path_to_file)