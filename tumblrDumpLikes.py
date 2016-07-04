#!/usr/bin/env python2.7

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

def download(url, outfile):
  attempts = 0
  while attempts < 3:
    try:
        response = urllib2.urlopen(url, timeout=5)
        content = response.read()
        f = open(outfile, 'w')
        f.write(content)
        f.close()
        break
    except urllib2.URLError as e:
        attempts += 1
        print type(e)

# Make the request
#posts = tumblr.posts('robotmonkeys-net.tumblr.com', limit=limit, offset=offset)
#total_posts = posts['total_posts']

# Grab the likes
offset = 0
if len(sys.argv) > 1:
  offset = int(sys.argv[1])
limit = 20 # maximum limit
i = offset
while True:
  likes = tumblr.likes(limit=limit, offset=offset)
  num_likes = likes['liked_count']
  print "THERE ARE " + str(num_likes) + " LIKED POSTS"
  print "RECEIVED " + str(len(likes['liked_posts']))
  for cur_post in likes['liked_posts']:
    print "PROCESSING POST " + str(i) + ' ' + str(cur_post['id']) + ' ' + cur_post['post_url']
    i = i + 1
    os_path = PATH + '/tumblr/' + str(cur_post['id'])
    try:
      os.makedirs(os_path)
      post_data = {}
      post_data[u'site'] = u'tumblr'
      post_data[u'post_id'] = unicode(cur_post['id'])
      post_data[u'post_timestamp'] = cur_post['timestamp']
      if 'source_url' in cur_post:
        post_data[u'permalink_post_url'] = unicode(cur_post['source_url'])
      else:
        post_data[u'permalink_post_url'] = unicode(cur_post['post_url'])
      post_data[u'tags'] = []
      for tag in cur_post['tags']:
        post_data[u'tags'].append(unicode(tag))
      if cur_post['type'] == 'link':
        post_data[u'post_html'] = cur_post['description']
      elif cur_post['type'] == 'photo':
        post_data[u'post_html'] = cur_post['caption'] # this is html
      post_data[u'photos'] = []
      if 'photos' in cur_post:
        for photo in cur_post['photos']:
          photo_data = {}
          photo_data[u'caption'] = photo['caption']
          photo_data[u'permalink_url'] = photo[u'original_size']['url']
          post_data[u'photos'].append(photo_data)
          print "\t" + 'downloading ' + str(photo_data[u'permalink_url'])
          download(photo_data[u'permalink_url'], os_path + '/' + os.path.basename(photo_data[u'permalink_url']))

      print "\t" + 'writing ' + os_path + '/data.json'
      f = open(os_path + '/data.json', 'w')
      f.write(json.dumps(post_data).encode('utf8'))
      f.close()
    except OSError as err:
      print("\tskipping because an OS error occurred: {0}".format(err))
    except:
      print("\tskipping because: ", sys.exc_info()[0])

  if (offset + len(likes['liked_posts'])) >= num_likes:
    print "stopping because " + str(offset + limit) + " >= " + str(num_likes)
    break
  offset = offset + len(likes['liked_posts'])
  print "advancing to offset " + str(offset)
