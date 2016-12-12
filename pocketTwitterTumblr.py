#!/usr/bin/env python

import sys;
reload(sys);
sys.setdefaultencoding("utf8")

import pocket
import pytumblr
import re
import secrets
import twitter
import urllib2


tumblr_blogname = 'robotmonkeys-net'
tumblr = pytumblr.TumblrRestClient(
  secrets.app_keys['tumblr']['consumer_key'],
  secrets.app_keys['tumblr']['consumer_secret'],
  secrets.access_keys['jonathankoren']['tumblr']['access_token'],
  secrets.access_keys['jonathankoren']['tumblr']['access_secret']
)

tapi = twitter.Api(
  consumer_key=secrets.app_keys['twitter']['consumer_key'],
  consumer_secret=secrets.app_keys['twitter']['consumer_secret'],
  access_token_key=secrets.access_keys['jonathankoren']['twitter']['access_token'],
  access_token_secret=secrets.access_keys['jonathankoren']['twitter']['access_secret']
)

p = pocket.Pocket(
  secrets.app_keys['pocket']['consumer_key'],
  secrets.access_keys['jonathankoren']['pocket']['access_token']
)

favs = p.get(sort='newest', offset=0, count=1000)
for k in favs[0]['list'].keys():
  fav = favs[0]['list'][k]
  if ('resolved_url' in fav) and ('twitter.com/' in fav['resolved_url']):
    toks = fav['resolved_url'].split('/')
    for i in xrange(len(toks)):
      if toks[i] == 'status':
        try:
          tweet = tapi.GetStatus(toks[i + 1])
          if tweet.media is not None:
            for m in tweet.media:
              url = m.media_url_https + ':large'
              print 'tumblr ' + str(fav['item_id']) + ' ' + url + ' ' + fav['resolved_title']
              tumblrCaption = unicode(fav['resolved_title']) + u"\n" + unicode(tweet.text) + u"\n" + unicode(fav['resolved_url'])
              tumblr.create_photo(tumblr_blogname, state='published', format='markdown', caption=str(tumblrCaption), source=url)
        except twitter.TwitterError as e:
          print unicode('failed to download ') + unicode(fav['resolved_url']) + unicode(' ') + unicode(e.message)
    p.unfavorite(fav['item_id'])
    p.archive(fav['item_id'])
    p.commit()
