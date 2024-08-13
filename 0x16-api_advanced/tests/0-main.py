#!/usr/bin/python3
import sys


if __name__ == '__main__':
    number_of_subscribers = __import__('subs_0').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

