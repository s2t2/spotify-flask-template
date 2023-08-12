

from dotenv import load_dotenv
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv() # load environment variables

# env vars used implicitly by the spotipy package:
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")


client_credentials = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
#oauth_credentials = SpotifyOAuth(client_id="", client_secret="", redirect_uri="")
#oauth_credentials.get_access_token(code="")

client = spotipy.Spotify(client_credentials_manager=client_credentials)
print(client)

search_term = "Taylor Swift"
response = client.search(q=search_term, limit=20)
print(type(response))

tracks = response['tracks']['items']
print(len(tracks))

for i, track in enumerate(tracks):
    print(' ', i, track['name'])
