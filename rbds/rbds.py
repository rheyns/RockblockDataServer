#!/usr/bin/python

from flask import Flask
import requests

app = Flask(__name__, static_url_path='')

@app.route('/messages', methods=['POST'])
def messages():
  """Process messages from RockBlock"""
  # Do stuff here
  # Now send confirmation back
  r = requests.get('http://some-server/path')
  if r.status_code != 200:
    # Handle some sort of failure, since we didn't get the 200 OK code
    pass

@app.route('/', methods=['GET'])
def homepage():
  """Serve up a default homepage"""
  return 'Hello World, and Alex says hi too'

def main():
  app.run(host='0.0.0.0', port=5050)

if __name__ == '__main__':
  main()
