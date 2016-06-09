#!/usr/bin/env python

import twitter

consumer_key='V1tFhqK4eB4wFgzxMmurEnP79'
consumer_secret='oeWQaenPxFySwIr7kTxezLdZz9vCFTkwOaddnvEOv9mLQgx65u'
access_token_key='23558652-JQNkPptepJHtFALj7dpI2ps28kHQ2VoJWY7U2rUt8'
access_token_secret='iZ4iRUbCGOwqPdIDmzwNapd4ogS6SQBluklxWzhIpBHoH'

api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret)
#status = api.GetStatus(683135646706364417)
status = api.GetStatus(684876859515916288)
text = status.text
pseudonymous_name = status.user.name
screen_name = status.user.screen_name
#created_time = status.created_time # Sat Jan 02 04:00:04 +0000 2016
for m in status.media:
  expanded_url = m['expanded_url']
  media_url = m['media_url']
  media_url_https = m['media_url_https']
  id_str = m['id_str']
  large_media_url_https = m['media_url_https'] + ':large'
  
  print m
  print
