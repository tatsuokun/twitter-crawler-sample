import json
from twitter.api import Twitter
from twitter.oauth2 import OAuth2
from twitter.oauth_dance import oauth2_dance


def get_keys(path_to_keys_json):
    with open(path_to_keys_json, mode="r") as f:
        keys = json.load(f)
    return keys


def oauth2(keys):
    BEARER_TOKEN = oauth2_dance(keys['ConsumerKey'], keys['ConsumerSecret'])
    return Twitter(auth=OAuth2(keys['AccessToken'], 
                               keys['AccessTokenSecret'],
                               BEARER_TOKEN))


def authenticate(path_to_keys_json):
    keys = get_keys(path_to_keys_json)
    return oauth2(keys)
