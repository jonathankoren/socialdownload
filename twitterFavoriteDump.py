#!/usr/bin/env python

import secrets

import twitter

api = twitter.Api(
  consumer_key=secrets.app_keys['twitter']['consumer_key'],
  consumer_secret=secrets.app_keys['twitter']['consumer_secret'],
  access_token_key=secrets.access_keys['jonathankoren']['twitter']['access_token'],
  access_token_secret=secrets.access_keys['jonathankoren']['twitter']['access_secret']
)

self_user = api.VerifyCredentials()
num_favorites = self_user.favourites_count
screen_name = self_user.screen_name
user_id = self_user.id
pseudonymous_name = self_user.name

# max count is 200, Which means to get all favorites, we're going to have to
# unfavorite as we go
to_refavorite_id = []
favorites = api.GetFavorites(count=200)
while len(favorites) > 0:
  for fav in favorites
    created_timestamp = fav.created_at  # Sat Jan 02 04:00:04 +0000 2016
    text = fav.text
    status_id = fav.id
    for url in fav.urls:
      u = urls.expanded_url
    for m in fav.media:
      expanded_url = m['expanded_url']
      media_url = m['media_url']
      media_url_https = m['media_url_https']
      id_str = m['id_str']
      large_media_url_https = m['media_url_https'] + ':large'

    to_refavorite_id.append(status_id)
    api.DestroyFavorite(status=fav)
  favorites = api.GetFavorites(count=200)


# refavorite everything
for id in to_refavorite_id:
  api.CreateFavorite(id=id)
