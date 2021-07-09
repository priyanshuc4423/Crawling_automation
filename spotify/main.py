import requests
from bs4 import BeautifulSoup
import lxml
import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
SPOTIPY_CLIENT_ID = "0166c6468bdc41e281a74c2ee8652396"
SPOTIPY_CLIENT_ID_SECRET = "006c461355da43c1a270ceaa828d691f"
redirect_url = "http://example.com/"
scope = "playlist-modify-private"
ID = "ixj8ypwsn58ydio7v9f99k2cu"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_ID_SECRET,redirect_uri=redirect_url,scope=scope))
user_id = sp.current_user()["id"]


year = input("what year you would like to travel to in YYYY-MM-DD format")



URL = f"https://www.billboard.com/charts/hot-100/{year}"

response = requests.get(URL)
CONTENT = response.text

response.raise_for_status()

soup = BeautifulSoup(CONTENT,"lxml")

song_name = soup.find_all(name= "span", class_ = "chart-element__information__song text--truncate color--primary")
new_list = [ x.getText() for x in song_name]
song_uri=[]
for x in new_list:

    new_new_list = sp.search(q=f"track:{x}")
    try:
        uri = new_new_list["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except:
        pass




playlist = sp.user_playlist_create(user=ID,name=f"{year} billboard 100",public=False)






sp.playlist_add_items(playlist_id=playlist["id"],items=song_uri)
