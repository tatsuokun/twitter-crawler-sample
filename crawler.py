import json
import argparse
from util import authenticate
from twitter.follow import follow


def crawl_follower_ids(twitter, screen_name):
    # get the entire list of followers user_ids for the user corresponding given screen_name
    return follow(twitter, screen_name, followers=True)


def crawl_friends_ids(twitter, screen_name):
    # get the entire list of user_ids
    return follow(twitter, screen_name, followers=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--screen_name',
                        type=str,
                        default='screen_names.txt')
    args = parser.parse_args()

    with open(args.screen_name, mode='r') as f:
        screen_names = [_.strip() for _ in f]

    twitter = authenticate('auth.json')

    for screen_name in screen_names:
        following_list = crawl_friends_ids(twitter, screen_name)
        print(following_list)

if __name__ == '__main__':
    main()
