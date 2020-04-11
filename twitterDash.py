import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sqlite3
import requests
class listener(StreamListener):

    def dataOn(self,data):
        print(data)
        return True
    def errorOn(self,error):
        print(error)

APIkey = 'pviFW6JiIcROhlyhfMx4k5tKy'
APIsecret = 'H65QIE5HlSwRSmdIqgEuGi8E7FXhomHI4wwo3wz8kx4jqy8O1B'

Atoken = '1655514888-TRrtq6J8sIH63hwxSQTs7RNuUKcK1d8nBfJNyUC'
Atokensecret = 'WkjRpggySfqdv1NZKPg0ZY0eby68Si6Gu4kWBmjxBMTha'

auth = OAuthHandler(APIkey,APIsecret)
auth.set_access_token(Atoken, Atokensecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])


