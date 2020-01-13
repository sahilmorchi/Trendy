import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

"""client_credentials_manager = SpotifyClientCredentials(client_id='fd0f694eb3df41f1ae48bc7d0d8d5a3a',client_secret='f06d7ba6bc094ea5944622f77c77462d' )
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
        """

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print ("usage: python user_playlists.py [username]")
        sys.exit()

    token = util.prompt_for_user_token(username,client_id='fd0f694eb3df41f1ae48bc7d0d8d5a3a',client_secret='f06d7ba6bc094ea5944622f77c77462d', redirect_uri='http://localhost:8888')

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print()
                print (playlist['name'])
                print('  total tracks', playlist['tracks']['total'])
                results = sp.user_playlist(username, playlist['id'],
                    fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print ("Can't get token for", username)