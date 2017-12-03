import json
import requests
import urllib.request as urllib


class Util(object):

    @staticmethod
    def url_shorten(url):
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
    @staticmethod
    def leet_speak(in_string):
        replacement_characters = (('l', '1'), ('e', '3'), ('a', '4'), ('s', '5'), ('t', '7'), ('o', '0'))
        in_string = in_string.replace("!leet ", "")
        out_string = in_string.lower()
        for old, new in replacement_characters:
            out_string = out_string.replace(old, new)
        print('1337 5p34k...')

        return out_string

    # Retrieves a random dad joke.
    @staticmethod
    def get_dad_joke():
        http = urllib.build_opener()
        http.addheaders = [('User-Agent', 'Mozilla/5.0'), ('Accept', 'text/plain')]
        joke_text = http.open('https://icanhazdadjoke.com/').read().decode()
        print('Telling a joke...')

        return joke_text
