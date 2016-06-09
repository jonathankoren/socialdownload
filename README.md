Requires a file called secrets.py which is not included.

It should contain your API and access tokens. It's format is:

...
app_keys = {
  'pocket': {
     'consumer_key': '',    # some key
   },
   'tumblr' : {
     'consumer_key': '',    # some key
     'consumer_secret': '', # some key
   },
   'twitter' : {
     'consumer_key': '',    # some key
     'consumer_secret': '', # some key
   },
}

access_keys = {
  'jonathankoren' : {	    # a specific account. You can change this, but 
                            # you'd have to modifiy the code as well.
    'pocket': {
       'access_token': '',  # some key
    },
    'tumblr' : {
      'access_token': '',   # some key
      'access_secret': '',  # some key
    },
    'twitter' : {
      'access_token': '',   # some key
      'access_secret': '',  # some key
    },
  },
}
...