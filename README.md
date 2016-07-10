# Requirements

We're stuck using python 2.7 because of pytumblr .

## Packages

* pocket
* python-twitter
* pytumblr

# Install
Requires a file called secrets.py which is not included.

It should contain your API and access tokens. It's format is:

```python
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
  'account_login' : {	      # a specific account login
    'pocket': {             # providers associated with the account
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
```
