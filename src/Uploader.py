#!/usr/bin/python
#
# Install python requests library: 
# pip install requests

import requests

class Uploader:
    """A class for uploading the image files"""
    def __init__(self):
        self.url = 'http://192.168.1.105:3000/upload'
    
    def upload(self, filename):
        files = {'file': open(filename, 'rb')}
        r = requests.post(self.url, files=files)
        print filename,vars(r)

