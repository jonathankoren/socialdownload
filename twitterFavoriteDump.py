#!/usr/bin/env python

import secrets

import twitter

for login, serviceData in secrets.access_keys.items():
  if 'twitter' in serviceData:
    api = twitter.Api(
      consumer_key=secrets.app_keys['twitter']['consumer_key'],
      consumer_secret=secrets.app_keys['twitter']['consumer_secret'],
      access_token_key=serviceData['twitter']['access_token'],
      access_token_secret=serviceData['twitter']['access_secret']
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
      for fav in favorites:
        created_timestamp = fav.created_at  # Sat Jan 02 04:00:04 +0000 2016
        text = fav.text
        status_id = fav.id
        #for url in fav.urls:
        #  u = url.expanded_url
        if fav.media is not None:
          for m in fav.media:
            print m
            expanded_url = m.expanded_url
            media_url = m.media_url
            media_url_https = m.media_url_https
            id_str = str(m.id)
            large_media_url_https = m.media_url_https + ':large'

        to_refavorite_id.append(status_id)
        api.DestroyFavorite(status=fav)
      favorites = api.GetFavorites(count=200)


    # refavorite everything
    for id in to_refavorite_id:
      api.CreateFavorite(id=id)
