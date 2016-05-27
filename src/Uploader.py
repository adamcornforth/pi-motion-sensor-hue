#!/usr/bin/python
#
# Install python requests library: 
# pip install requests
# 
# Install libffi libraries needed by cryptography
# sudo apt-get install libffi-dev
import requests

class Uploader:
    """A class for uploading the image files"""
    def __init__(self):
        self.url = 'http://pi-meteor.herokuapp.com/upload'
    
    def upload(self, filename):
        files = {'file': open(filename, 'rb')}
        r = requests.post(self.url, files=files)
