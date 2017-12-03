import io
import os
import json
import requests
import urllib.request as urllib
import zipfile
import subprocess


class Atlas(object):

    @staticmethod
    def build(content):
        # Get URL for zip
        # Check if file is a ZIP [NOT DONE]

        name = content[0]['filename'].replace('.zip', '')
        print(name)
        data = content[0]['url']

        # Download Zip to memory (extracted)
        request = requests.get(data)
        extracted_files = zipfile.ZipFile(io.BytesIO(request.content))
        print(extracted_files.namelist())
        if not os.path.exists('{0}\{1}'.format(os.getcwd(), 'temp')):
            os.makedirs('{0}\{1}'.format(os.getcwd(), 'temp'))

        extracted_files.extractall('{0}\{1}'.format(os.getcwd(), 'temp'))

        os.system('{0}/atlas.py -i "{1}" -n "{2}"'.format("S:\GameTextures\GT-Web-View",
                                                          r'{0}\{1}\atlas'.format(os.getcwd(), 'temp', name),
                                                          name))
        return r'{0}\{1}\atlas\{2}.jpg'.format(os.getcwd(), 'temp', name)


