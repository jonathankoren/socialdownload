#!/usr/bin/env python

from pprint import pprint
import pocket
import pytumblr
import re
import secrets
import sys
import twitter
import urllib2

for login, serviceData in secrets.access_keys.items():
  if 'pocket' in serviceData:
    p = pocket.Pocket(
      secrets.app_keys['pocket']['consumer_key'],
      serviceData['pocket']['access_token']
    )

    to_delete = []

    offset = 0
    favs = p.get(sort='newest', favorite=0, offset=0, count=100)
    while len(favs[0]['list']) > 0:
      for k in favs[0]['list'].keys():
        fav = favs[0]['list'][k]
        if u'resolved_title' in fav and fav[u'resolved_title'] == u'Missing Link':
          #print "deleting " + str(fav)
          to_delete.append(fav['item_id'])
      offset = offset + 1000
      favs = p.get(sort='newest', favorite=0, offset=offset, count=10)

    for iid in to_delete:
        p.delete(iid)
    p.commit()
