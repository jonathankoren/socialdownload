#!/usr/bin/env python

import secrets

import json
import os
import pytumblr
import sys
import urllib2

PATH = '/Users/jonathan/Dropbox/social_clone'

# site: Tumblr, Twitter, Pocket, Flickr, etc.
# post_id: some site specific id string
# post_timestamp: epoch seconds when the post was made
# permalink_post_url: permalink to the original post
# post_html: string
# caption_html: string
# tags: array of strings
# photos:
#    caption:
#    permalink_url


tumblr = pytumblr.TumblrRestClient(
  secrets.app_keys['tumblr']['consumer_key'],
  secrets.app_keys['tumblr']['consumer_secret'],
  secrets.access_keys['jonathankoren']['tumblr']['access_token'],
  secrets.access_keys['jonathankoren']['tumblr']['access_secret']
)


# Grab the likes
offset = 0
if len(sys.argv) > 1:
  offset = int(sys.argv[1])
limit = 20 # maximum limit
i = offset
num_likes = -1
while True:
  likes = tumblr.likes(limit=limit, offset=offset)
  if num_likes < 0:
    num_likes = likes['liked_count']
  print "THERE ARE " + str(num_likes) + " LIKED POSTS"
  print "RECEIVED " + str(len(likes['liked_posts']))
  if len(likes['liked_posts']) == 0:
    break
  for cur_post in likes['liked_posts']:
    print "PROCESSING POST " + str(i) + ' ' + str(cur_post['id']) + ' ' + cur_post['post_url']
    i = i + 1
    os_path = PATH + '/tumblr/' + str(cur_post['id'])
    #try:
    #  os.makedirs(os_path)
    #  os.rmdir(os_path)
    #  print "OOPS! " + cur_post['post_url'] + " is new! Skipping."
    #except:
    # we want a fail
    print "reblogging " + str(cur_post['id']) + " // " + str(cur_post['reblog_key'])
    tumblr.reblog('robotmonkeys-net.tumblr.com', id=cur_post['id'], reblog_key=cur_post['reblog_key'])
    tumblr.unlike(cur_post['id'], cur_post['reblog_key'])

  offset = offset + len(likes['liked_posts']) - 1
  print "advancing to offset " + str(offset)
