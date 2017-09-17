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


## Variables
subreddit_name="worldnews"
sort_by="rising"

account_sid = "AC5fb440c5a197baf2a967ea6d1f5b8e3b"
auth_token = "14bf9cfbd24b992a0dc411ac2cae0ade"
upvotes_per_min_trigger=1
refresh_every=360           # Seconds

content_buffer = list()
cl = config_load()
config_dict = cl._parse()

while True:
        client = Client(account_sid, auth_token)
        page = requests.get("https://www.reddit.com/r/" +subreddit_name + "/" + sort_by + ".json?sort=new")
        print("Response Status: " + str(page.status_code))
        print "Last refresh: " + time.strftime('%X')
        if page.status_code != 200:
                print("Error parsing page!  Skipping this time.")
                time.sleep(refresh_every)
                continue

        soup = unicode(str(BeautifulSoup(page.content, 'html.parser')), 'latin-1')
        children = json.loads(soup).get('data').get('children')
        for item in children:
                d = item.get('data')
                mins_since_creation, seconds_since_creation = divmod((mktime(time.gmtime()) - d.get('created_utc')), 60)
                upvotes_per_min = d.get('score') / mins_since_creation
                if upvotes_per_min > upvotes_per_min_trigger:
                        if d.get('url') in content_buffer:
                                print "Skipping : " + d.get('title')
                        else:
                                print "Sending text for " + d.get('url')
                                message = client.api.account.messages.create(to=phone_number_target,
                                                                         from_=phone_number_source,
                                                                         body=(d.get('title') + " ( " + str(d.get('score')) + " | " + str(upvotes_per_min) + " | " + str(d.get('num_comments')) + ")\n\n" +  d.get('url')))
                                content_buffer.append(str(d.get('url')))
                                time.sleep(refresh_every)
