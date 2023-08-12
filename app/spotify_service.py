

from dotenv import load_dotenv
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

load_dotenv() # load environment variables

# env vars used implicitly by the spotipy package:
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URL", default="http://localhost:5000/auth/spotify/callback")

def spotify_oauth():
    # Create a SpotifyOAuth instance
    return SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="user-library-read user-read-playback-state",
        cache_path=".spotifycache",
    )

if __name__ == "__main__":


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
