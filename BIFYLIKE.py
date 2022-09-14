import tweepy
import random
import time

from tweepy.error import TweepError

consumer_key='6MUyTlnvDNlrfjfNIKcq3jYJ0'
consumer_secret='pDqtenuvWjIS1GMMHr65AGDhD2FPAKGxdmCm74v38ljrAbZ7aT'

key='1375127912286810121-iIMyvsyD5oQ2uyqvX6wbLm06WGiD1u'    
secret='RLBG02fWgU2hjHhxs2UvZoZp26EEy9pqyJygOgCx9MRcN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

search_list=['spotify.link/','#SpotifyCharts', 'Spotify','Lil Nas X','#BTS', 'Kanye West', 'Drake', 'Doja Cat', 'Billboard Hot 100', 'Spotify streams', 'Megan Thee Stallion', 'Cardi B', 'Nicki Minaj', 'Beyoncé', 'Ariana Grande', 'Harry Styles', 'xxl freshman', 'Billboard Hot 10']
search=random.choice(search_list)
UNO=41

for tweet in tweepy.Cursor(api.search, search).items(UNO):
        try:
            print('Tweet Liked')
            tweet.favorite()
            time.sleep(60)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
         break
        
while True:
    time.sleep(1140)
    