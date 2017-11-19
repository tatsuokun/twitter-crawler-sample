import json
from util import authenticate
from twitter.follow import follow


def crawl_following_ids(twitter, screen_name):
    # get the entire list of user_ids that the user corresponding given screen_name follows
    return follow(twitter, screen_name)


if __name__ == '__main__':
    twitter = authenticate('auth.json')
    screen_name = 'tatsuokundayo'
    following_list = crawl_following_ids(twitter, screen_name)
    print(following_list[0])
