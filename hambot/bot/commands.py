import requests
import json


class Command:
    @classmethod
    def url_shorten(cls, url):
        url = url.replace("!shorten", "").replace("<", "").replace(">", "").split(r'|')
        key = 'AIzaSyD4yFhUY4rH2vWdj_5DpnXHbHBcPcGNU6U'
        post_url = 'https://www.googleapis.com/urlshortener/v1/url?key={0}'.format(key)
        payload = {'longUrl': url}
        header = {'content-type': 'application/json'}
        response = requests.post(post_url, data=json.dumps(payload), headers=header)
        data = json.loads(response.text)
        print('Shortening a URL...')

        return data['id']

    # Converts user-input to 1337 5p34k.
    @classmethod
    def leet_speak(cls, in_string):
        replacement_characters = (('l', '1'), ('e', '3'), ('a', '4'), ('s', '5'), ('t', '7'), ('o', '0'))
        in_string = in_string.replace("!leet ", "")
        out_string = in_string.lower()
        for old, new in replacement_characters:
            out_string = out_string.replace(old, new)
        print('1337 5p34k...')

        return out_string

    # Retrieves a random dad joke.
    @classmethod
    def get_dad_joke(cls):
        header = {'User-Agent': 'Mozilla/5.0', 'Accept': 'text/plain'}
        response = requests.get('https://icanhazdadjoke.com', headers=header)
        if response.status_code == 200:
            return response.text.encode('utf-8').decode()
        else:
            return 'Too angry to tell a joke.'
