#!/usr/bin/env python3
# bot.py

from generate_verses import get_verselist
import tweepy
import json
import time
from secrets import *

INTERVAL = 60 * 60 * 24 # tweets every 24 hours

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

verselist = get_verselist()
my_iter = iter(verselist)

while True:
    api.update_status(next(my_iter))
    time.sleep(INTERVAL)

api.update_status("Beep")