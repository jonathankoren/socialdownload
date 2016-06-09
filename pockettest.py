#!/usr/bin/env python
import pocket

pocket_consumer_key = '49691-5a15a50769b4c079d1cddd5d'
pocket_access_token = '6658e190-fc79-c244-ef49-306802'


# When you need to authorize
#pocket_request_token = pocket.Pocket.get_request_token(consumer_key=pocket_consumer_key)
#auth_url = pocket.Pocket.get_auth_url(code=pocket_request_token, redirect_uri='http://localhost')
# visit auth_url and click 'authorize'

#pocket_user_credentials = pocket.Pocket.get_credentials(consumer_key=pocket_consumer_key, code=pocket_request_token)
#pocket_access_token = pocket_user_credentials['access_token']


p = pocket.Pocket(pocket_consumer_key, pocket_access_token)
favs = p.get(sort='newest', favorite=1, offset=0, count=10)
# FIXME: sort favs by the 'sort_key' field
for k in favs[0]['list'].keys():
  fav = favs[0]['list'][k]
  item_id = fav['item_id']
  is_index = fav['is_index'] # 0 = not index, 1 = index
  is_article = fav['is_article'] # 0 = not article, 1 = article
  status = fav['status']  # 0 = unarchived, 1 = archived, 2 = deleted
  has_image = fav['has_image'] #  0, 1, or 2 - 1 if the item has images in it - 2 if the item is an image
  has_video = fav['has_video'] # 0, 1, or 2 - 1 if the item has videos in it - 2 if the item is a video
  excerpt = fav['excerpt']
  favorite = fav['favorite'] # 0 = unfavorited, 1 = favorited
  given_title = fav['given_title']
  given_url = fav['given_url']
  resolved_title = fav['resolved_title']
  resolved_url = fav['resolved_url']
  print resolved_title
  #tags = fav['tags']
  #authors = fav['authors']
  #images = fav['images']
  #videos = fav['videos']


