#!/c/Users/User/Anaconda2/python

import pandas
import json
import requests
import pprint

API_KEY = ""
URL = "http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=" + API_KEY + "&format=json"
PRETTY_PRINTER = pprint.PrettyPrinter(indent=2)

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    # 
    # Once you've done this, return the name of the number 1 top artist in
    # Spain.
    
    raw_data = requests.get(url).text
    data = json.loads(raw_data)
    top_artists = data['topartists']
    artist_name = ''
    max_listeners = 0
    
    for entry in top_artists['artist']:
        if float(entry['listeners']) > max_listeners:
            #print "Changing artist from '{0}' ({1}) to '{2}' ({3})".format(artist_name, max_listeners, entry['name'], entry['listeners'])
            max_listeners = float(entry['listeners'])
            artist_name = entry['name']
            
    #print "Most popular artist was '{0}'".format(artist_name)

    return artist_name # return the top artist in Spain

if __name__ == "__main__":
    print api_get_request(URL)