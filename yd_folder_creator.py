import requests

def create_folder(folder_name):
    yd_token = 'token'
    url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
    headers = {'Authorization': 'OAuth ' + yd_token}
    params = {'path': folder_name}

    r = requests.put(url, headers=headers, params=params)
    print(r.status_code)
    return r.status_code
if __name__ == '__main__':
    create_folder('test_folder')