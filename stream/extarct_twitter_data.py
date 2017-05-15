import tweepy  # this will give an error if tweepy is not installed properly
from tweepy import OAuthHandler
import json

# provide your access details below
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweetslist = api.search("%23haiku",rpp=10,since_id='863974490291802112')

for status in tweetslist:
    json_str = json.dumps(status._json)
    print(json.loads(json_str)['text'])

from tweepy import Stream
from tweepy.streaming import StreamListener

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)


class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('D:\\python_data_set\\data_extract.json', 'a') as f:  # change location here
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


#twitter_stream = Stream(auth, MyListener())

# change the keyword here
#twitter_stream.filter(track=['#cricket'])