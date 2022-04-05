from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def spotify():

    playlistId = "1bqfMWQo9tEvKZJg4oKL0R"
    endpoint =	"https://api.spotify.com/v1/playlists/{playlistId}?fields=name%2Cfollowers(total)%2Cowner(id)%2Ctracks(items(track(name)))".format(playlistId=playlistId)
    token = "BQCGoFMgvM3gr5CnqdfwXByZstCxGZuhcG612rW_SKufByeuJ74u9r6H23UxT4i0rg25TYWZLl3l23mK4wuwwFDo1mn6jzhD6Z6eudGGSSSiF-YySMGg05bcysceGpCotRhbAoQXkA-MOVyHmHbjjSs26XLN9EW2yQdg"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=token)
    }
    
    resultado = requests.get(endpoint, headers=headers)
    datos = resultado.json()

    return '<pre>{}</pre>'.format(json.dumps(datos, indent=4))

app.run()