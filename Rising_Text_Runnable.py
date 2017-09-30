import requests
import time
import json
import sys
import os
import datetime
import calendar
from time import mktime
from bs4 import BeautifulSoup
from ConfigLoad import config_load
from twilio.rest import Client

content_buffer = list()
cl = config_load()
config_dict = cl._parse()

while True:
        client = Client(config_dict['account_sid'], config_dict['auth_token'])
        page = requests.get("https://www.reddit.com/r/" + config_dict['subreddit_name'] + "/" + config_dict['sort_by'] + ".json?sort=new")
        print("Response Status: " + str(page.status_code))
        print "Last refresh: " + time.strftime('%X')
        if page.status_code != 200:
                print("Error parsing page!  Skipping this time.")
                time.sleep(float(config_dict['refresh_every']))
                continue

        soup = unicode(str(BeautifulSoup(page.content, 'html.parser')), 'latin-1')
        children = json.loads(soup).get('data').get('children')
        for item in children:
                d = item.get('data')
                mins_since_creation, seconds_since_creation = divmod((mktime(time.gmtime()) - d.get('created_utc')), 60)
                print " |||  " + str(mins_since_creation) 
		upvotes_per_min = d.get('score') / mins_since_creation
		print upvotes_per_min
                if upvotes_per_min > config_dict['upvotes_per_min_trigger']:
                        if d.get('url') in content_buffer:
                                print "Skipping : " + d.get('title')
                        else:
                                print "Sending text for " + d.get('url')
                                message = client.api.account.messages.create(to=config_dict['phone_number_target'],
                                                                         from_=config_dict['phone_number_source'],
                                                                         body=(d.get('title') + " ( " + str(d.get('score')) + " | " + str(upvotes_per_min) + " | " + str(d.get('num_comments')) + ")\n\n" +  d.get('url')))
                                content_buffer.append(str(d.get('url')))
	time.sleep(float(config_dict['refresh_every']))
