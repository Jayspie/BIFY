import requests
import base64,json
from info import *
id='eb06631f371345be8eb9db8d9c7bbf98'
secret='db3274ecbe9b42d5b1eac7faa4744a5e'
authUrl="https://accounts.spotify.com/api/token"
authheader={}
authdata={}
cid="5vhMI6qUtzn8rDzJe7gSxv"

def get_access_token(id,secret):
    message = f"{id}:{secret}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    authheader['Authorization'] ="Basic "+ base64_message
    authdata['grant_type']= "client_credentials"

    res = requests.post(authUrl,headers=authheader,data=authdata)
    responseobj=res.json()
    #print(json.dumps(responseobj, indent=2))

    access_token=responseobj['access_token']

    return access_token

def get_Playlist(token,playlist_id):
    playlisturl= f"https://api.spotify.com/v1/playlists/{playlist_id}"

    getheader ={
        'authorization': f"Bearer {token}"
    }

    res= requests.get(playlisturl,headers=getheader)
    
    playlistobj=res.json()
    
    return playlistobj

token = get_access_token(id,secret)

playlist_id="0To8Dg8KqbWFOiKzzlv5Jo"

tracklist=get_Playlist(token,playlist_id)

#print(json.dumps(tracklist,indent=2))

for t in tracklist["tracks"]["items"]:
    #artist= t['track'],['artists'],['name']
    Names= t['track']['uri']

def put_songs(token):
    url=f"https://api.spotify.com/v1/playlists/{cid}/tracks"
    
    getheader ={
        'authorization': f"Bearer {token}"
    }

    res= requests.post(url,data=Names,headers=getheader)
    
    playlistobj=res.json()
