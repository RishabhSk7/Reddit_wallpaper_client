def network(sub_r, name, password):
    import requests
    import pprint
    import random

    base_url = 'https://www.reddit.com/'

    #{'access_token': '575944266236-dzjszIrXLkly4Le0o8pFkcmeskKlNw', 'token_type': 'bearer', 'expires_in': 3600, 'scope': '*'}

    data = {'grant_type': 'password',
            'username': name, 'password': password}

    auth = requests.auth.HTTPBasicAuth(
        "yhW-ZAAS3eBeDnW0H5SsmQ", "ysgzjodtzeb4YDXhXdH7H5ymI8GsQw")

    r = requests.post(base_url + 'api/v1/access_token',
                    data=data,
                    headers={'user-agent': 'Wallpaper-App by Rishabh_0507'},
                    auth=auth)
    d = r.json()
    base_url = 'https://oauth.reddit.com'

    token = 'bearer ' + d['access_token']

    headers = {'Authorization': token,
            'User-Agent': 'Wallpaper-App by Rishabh_0507'}
    response = requests.get(
        base_url + f'/r/{sub_r}/top.json?limit=50', headers=headers)


    list1 = []

    #pprint.pprint(response.json()["data"]["children"]["data"]["url"])

    if response.status_code == 200:
        for i in response.json()["data"]["children"]:
            if i["data"]["url"][-3::1] == "jpg" or i["data"]["url"][-3::1] == "png":
                list1.append(i["data"]["url"])

    return list1

if(__name__=="__main__"):
    print(network("wallpaper", "Rishabh_0507", "Aowu282n@££@2927Ka"))
