import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

cid ="fd0f694eb3df41f1ae48bc7d0d8d5a3a" 
secret = "f06d7ba6bc094ea5944622f77c77462d"
username = ""

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-read playlist-read-private'
token = util.prompt_for_user_token(username, scope,cid,secret, redirect_uri='http://localhost:8888')
if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        print(playlist['name'], playlist['id'])
    
else:
    print("Can't get token for", username)