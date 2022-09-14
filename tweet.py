from spot import*
import random
import tweepy
import time
from info import*

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
def uh():
    random.shuffle(a)
    tweets=["Hey check out this song that Bify found","Have you heard this song","Let Bify put you on to somthing","AHHHHHHH","Honestly and personally this is better than Kendrick","This song makes Bify want to slap his own mom","Bro that one part hits differnt","Don't listen to Bri this song is better","Bri is this the song you listen to when your boyfriend cheated on you","They don't miss"]
    random.shuffle(tweets)

    api.update_status(tweets[0]+" https://open.spotify.com/track/"+a[0])

while True:
    uh()
    time.sleep(21600)