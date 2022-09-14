import tweepy
import os

consumer_key='BDlljmdRfeE5mtcF0zuEeUmUa'
consumer_secret='opQgVceGhiNbpusnDiTVYFloMqzXq2eyumT8gHCwv45eGhyc52'

key='1455096088407384069-jMMNFUkPwyX2VjZiCViOsBz4ucYZm6'    
secret='VgKQrHqP1dKgzEh0a7h6y5BBE1TjhkuUj0m8OYl9m4aDV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

img_obj = api.media_upload("D:\BIFY CODE\stop3.mp4")
hey="butt"
dir(img_obj)
new_status = api.update_status(hey,media_ids=[img_obj.media_id_string])