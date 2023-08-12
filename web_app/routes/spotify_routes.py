
# this is the "web_app/routes/spotify_routes.py" file...

from flask import Blueprint, render_template, redirect, request, session, current_app #, url_for
from spotipy import Spotify

spotify_routes = Blueprint("spotify_routes", __name__)

@spotify_routes.route("/auth/spotify/login")
def login():
    print("LOGIN...")
    sp_oauth = current_app.config["SPOTIFY_OAUTH"]
    auth_url = sp_oauth.get_authorize_url()
    print("REDIRECTING TO:", auth_url)
    return redirect(auth_url)

@spotify_routes.route("/auth/spotify/callback")
def callback():
    print("CALLBACK...")
    code = request.args["code"]

    sp_oauth = current_app.config["SPOTIFY_OAUTH"]
    token_info = sp_oauth.get_access_token(code)
    print(type(token_info))
    print(token_info)

    # store info in the session to keep track of logged-in user info:
    session["spotify_user"] = token_info

    return redirect("/user/playlists")

@spotify_routes.route("/auth/spotify/logout")
def logout():
    print("LOGOUT...")
    session.clear()
    #del session["spotify_user"]
    return redirect("/")



@spotify_routes.route("/user/playlists")
def user_playlists():
    # todo: move to a route decorator
    if not session.get("spotify_user"):
        return redirect("/")

    spotify_token = session.get("spotify_user")
    access_token = spotify_token["access_token"]
    client = Spotify(auth=access_token)
    print(type(client))

    print("GETTING PLAYLISTS...")
    playlists = client.current_user_playlists(limit=10)
    playlist_names = [playlist["name"] for playlist in playlists["items"]]

    return render_template("user_playlists.html", playlists=playlist_names)
