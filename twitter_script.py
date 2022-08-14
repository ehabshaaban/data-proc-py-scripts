"""
twitter_script is fetching all tweets for a twitter user
"""

import tweepy
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener

#API key
consumer_key=""

#API secret key
consumer_secret=""
access_token=""
access_token_secret=""

class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)

twitterstream = Stream(auth, StdOutListener())
#tweets = twitterstream.filter(track=["car"])
#print(tweets)
# user = api.get_user(901277118654500869)
# print(user.screen_name)
alltweets = api.user_timeline(screen_name = "ehabfeki",count=10)

print(alltweets)
