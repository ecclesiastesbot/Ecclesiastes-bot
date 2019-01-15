#!/usr/bin/env python3
# bot.py
from os import environ
from generate_verses import get_verselist
import tweepy
import json
import time

CONSUMER_KEY = environ["CONSUMER_KEY"]
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

INTERVAL = 60 * 60 * 24 # tweets every 24 hours

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

verselist = get_verselist()
my_iter = iter(verselist)

while True:
    api.update_status(next(my_iter))
    time.sleep(INTERVAL)