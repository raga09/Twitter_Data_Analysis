import tweepy  # this will give an error if tweepy is not installed properly
from tweepy import OAuthHandler
import json
from geopy.geocoders import Nominatim


# provide your access details below
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


geolocator = Nominatim()
location = geolocator.geocode("hyderabad")

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

geocode_ = str(location.latitude) + ',' + str(location.longitude) + ',' + '200mi'
print(geocode_)
print(location.address)

api = tweepy.API(auth)
tweets_list = api.search("%23ipl", rpp=10, lang="en", geocode=geocode_)

with open('D:\\GitRepos\\Twitter_Data_Analysis\\data\\twitter_data.txt', 'w', encoding='utf-8') as txt_file:
    for status in tweets_list:
        json_str = json.dumps(status._json)
        tweet_json = json.loads(json_str)
        tweet_text = tweet_json['text']
        tweet_user = tweet_json['user']
        print(tweet_text,tweet_user)
        txt_file.write(tweet_text)

