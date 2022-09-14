import tweepy #Twitter python api
import spotipy #Spotify python api
from spotipy.oauth2 import SpotifyOAuth #Spotifpy Client Authorization Code 
import random
import time
import requests
from info import * #Access for the keys, secret, and ids

#Twitter api authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

#Spotify api authorization
scope="playlist-modify-public"
username=user_id
token=SpotifyOAuth(scope=scope, username=username)
spotifyobj=spotipy.Spotify(auth_manager=token)

#Repsons for the bot
#Resone_list=[' Bify loves this', ' Bify will add this to the playlist',' Sorry but Bify dont like', ' Never suggest this again', "We've been trying to reach you concerning your vehicle's extended warranty.", '@Spotify delete this person account', '@Spotify give this person 1 year free spotify premium', 'Wanna break from the ads?', 'excuse me excuse me mommy sorry mommy sorry mommy sorry mommy sorry mommy', 'Not going to lie this slaps', 'Bify loves you <3', 'Give BIfy your spotify account']
#random.shuffle(Resone_list)

#Reads and stores the twitter post id 
FILE_NAME= 'BIFYSEEN.txt'
def read_BIFYSEEN(FILE_NAME):
    file_read= open(FILE_NAME,'r')
    BIFYSEEN_id=int(file_read.read().strip())
    file_read.close()
    return BIFYSEEN_id
def store_BIFYSEEN(FILE_NAME, BIFYSEEN_id):
    file_write=open(FILE_NAME, 'w')
    file_write.write(str(BIFYSEEN_id))
    file_write.close()
    return

#Bify reply and add songs to playlist
def reply():
    #Bify replying, liking, and retweet the mention post it was sent
    tweets=api.mentions_timeline(read_BIFYSEEN(FILE_NAME), tweet_mode='extended')
    Resone_list=[' Bify loves this', ' Bify will add this to the playlist',' Sorry but Bify dont like', 
                    ' Never suggest this again', "We've been trying to reach you concerning your vehicle's extended warranty.", 
                    '@Spotify delete this person account', '@Spotify give this person 1 year free spotify premium',
                    'Wanna break from the ads?', 'excuse me excuse me mommy sorry mommy sorry mommy sorry mommy sorry mommy',
                    'Not going to lie this slaps', 'Bify loves you <3', 'Give BIfy your spotify account']
    random.shuffle(Resone_list)
    for tweet in reversed(tweets):
        if 'https://t.co/' in tweet.full_text.lower():
            print(str(tweet.id)+' - '+tweet.full_text)
            api.update_status(Resone_list[0]+" @"+ tweet.user.screen_name,tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_BIFYSEEN(FILE_NAME,tweet.id)
            twaets=str(tweet.full_text)#storing the tweet 
        
        text=twaets.split()
        list_count=len(text)
        stop=list_count-1
        if len(text)==list_count:
            del text[0:stop]
            resp = requests.head(text[0])
            resp.status_code
            uri_id=resp.headers["Location"]
            uri_id=uri_id.replace("https://open.spotify.com/track/"," ")
            uri_id=uri_id.lstrip()
            uri_id=uri_id.split("?")
            print(uri_id[0])
        elif len(text)==2:
            resp = requests.head(text[1])
            resp.status_code
            uri_id=resp.headers["Location"]
            uri_id=uri_id.replace("https://open.spotify.com/track/"," ")
            uri_id=uri_id.lstrip()
            uri_id=uri_id.split("?")
            print(uri_id[0])
        uri_id.remove(uri_id[1])
        spotifyobj.user_playlist_add_tracks(user_id,wowo_id,tracks=uri_id,position=None)
       

while True:
    reply()
    time.sleep(15)