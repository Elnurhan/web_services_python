import requests
import json
import datetime
from collections import Counter


ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'

YEAR = datetime.datetime.now().year

def user_data(uid):
    url = "https://api.vk.com/method/users.get"
    template = {'v': 5.71, 'access_token': ACCESS_TOKEN, 'user_ids': uid}
    r = requests.get(url, params=template)
    if r.status_code == requests.codes.ok:
        data = json.loads(r.text)
    else:
        r.raise_for_status()
    return data['response'][0]['id']

def friends_data(uid):
    url = "https://api.vk.com/method/friends.get"
    template = {'v': 5.71, 'access_token': ACCESS_TOKEN, 'user_id': uid, 'fields': 'bdate'}
    r = requests.get(url, params=template)
    counts = []
    if r.status_code == requests.codes.ok:
        data = json.loads(r.text)
    else:
        r.raise_for_status()
    #print(dict(data['response']['items']))
    for i in data['response']['items']:
        if 'bdate' in i:
            if len(i['bdate']) > 5:
                counts.append(YEAR - int(i['bdate'].split('.')[2]))
    res = Counter(counts)
    return dict(res)

def parser(counts):
    sorted_values = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_values
    

def calc_age(uid):
    uid = user_data(uid)
    res = friends_data(uid)
    return parser(res)



if __name__ == '__main__':
    res = calc_age('painharold')
    print(res)
