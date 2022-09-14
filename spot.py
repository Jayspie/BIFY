import spotipy
from spotipy.oauth2 import SpotifyOAuth
from info import *
#from BIFY import *


scope="playlist-modify-public"
username=user_id
wowo_id='5vhMI6qUtzn8rDzJe7gSxv'
feels_id=""
weekly="37i9dQZEVXcNoaSgR2ccmo"

token=SpotifyOAuth(scope=scope, username=username)
spotifyobj=spotipy.Spotify(auth_manager=token)

#spotifyobj.user_playlist_create(user=username,name="wowo",public=True,description="um hi")
#kevin=spotifyobj.playlist_items(playlist_id,fields='items,track,uri')
#print(json.dumps(kevin,sort_keys=4,indent=4))
a=spotifyobj.playlist_items(weekly,fields='items(track.uri)')
a=str(a)
a=a.split()
valueToBeRemoved = "{'track':"
valueToBeRemoved2 = "{'uri':"

try:
    while True:
        a.remove(valueToBeRemoved)
except ValueError:
    pass

try:
    while True:
        a.remove(valueToBeRemoved2)
except ValueError:
    pass

a.remove("{'items':")
a.remove("[{'track':")
#a.remove("{'uri':")
#a.remove("{'track':")
a=str(a)
a=a.replace("}"," ")
a=a.replace("["," ")
a=a.replace("'"," ")
a=a.replace(", "," ")
a=a.replace("]"," ")
a=a.replace('"',"")
a=a.replace("spotify:track:"," ")
a=a.replace(","," ")
a=a.split()

#print(a)
#print("apple")
#def add_track(link):
    #spotifyobj.user_playlist_add_tracks(user_id,wowo_id,link,position=None)

