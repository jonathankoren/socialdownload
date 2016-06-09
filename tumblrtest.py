#!/usr/bin/env python

import pytumblr

client = pytumblr.TumblrRestClient(
  'BEFiKFHs3OQRUIVvVE4cSM7OF3Yn7sxxhC6BVZf7gezmSIquUN', # consumer key
  'zKCHlEAyhto2lois9nZHtnZ57doue40jvIg6iYWzRzgSr1wvqZ', # consumer secret
  'jbtPIN5Si6N1nAr836cMvTDim3sbCfV7vpYxHNHeclhNuWG8Am', # oauth token
  'w9moJaPEO4TGDc9f4I3pgXtUkMdXeqBnlAzQprArDmdymCdjec'  # oauth secret
)

#client.info()

#Creates a photo post using a source URL
#client.create_photo('codingjester', state="published", tags=["testing", "ok"], source="https://36.media.tumblr.com/b965fbb2e501610a29d80ffb6fb3e1ad/tumblr_n55vdeTse11rn1906o1_500.jpg")

#Creates a photo post using a local filepath
#client.create_photo('codingjester', state="queue", tags=["testing", "ok"], tweet="Woah this is an incredible sweet post [URL]", data="/Users/johnb/path/to/my/image.jpg")

#Creates a photoset post using several local filepaths
#client.create_photo('codingjester', state="draft", tags=["jb is cool"], format="markdown", data=["/Users/johnb/path/to/my/image.jpg", "/Users/johnb/Pictures/kittens.jpg"], caption="## Mega sweet kittens")

# Make the request
offset = 0
limit = 20
posts = client.posts('robotmonkeys-net.tumblr.com', limit=limit, offset=offset)
total_posts = posts['total_posts']

for cur_post in posts['posts']:
  tags = cur_post['tags']
  via_tumblr_url = cur_post['source_url']
  summary = cur_post['summary']
  caption = cur_post['caption'] # this is html

  if photos in cur_post:
    for photo in cur_posts['photos']:
      summary = photo['summary']
      caption = photo['caption']  # this is html
      original_url = photo['original_size']['url']
      original_width = photo['original_size']['width']
      original_height = photo['original_size']['height']
      
blogname = 'robotmonkeys-net'
client.create_photo(blogname, state='published', tags=['b24', 'factory', 'wwii'], data=['/Users/jonathan/Desktop/IbY2svI.jpg'], format='markdown', caption='B-24 Factory')


# ~/Dropbox/IFTTT/Tumblr/May\ 23\ 2013\ at\ 1241AM/
# Photo -- September 28, 2012 at 01:01AM -- 1930s, illustrations, card, china, shanghai.jpg
# {{Caption}} -- {{Time}} -- {{Tags}}

