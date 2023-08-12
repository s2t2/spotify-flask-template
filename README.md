# spotify-flask-template

## Setup

```sh
conda create -n spotify-flask python=3.10
conda activate spotify-flask
```

```sh
pip install -r requirements.txt
```

### Credentials

Login to the Spotify Developer console, create a new app, set redirect url of "http://localhost:5000/auth/spotify/callback". Note the app's client id and client secret. Provide these credentials via ".env" file approach (see below).

### Environment Variables

Create ".env" and input your own credentials as environment variables:

```sh
# this is the ".env" file

SPOTIPY_CLIENT_ID="_________"
SPOTIPY_CLIENT_SECRET="_________"

```


## Usage


```sh
FLASK_APP="web_app" flask run
```
