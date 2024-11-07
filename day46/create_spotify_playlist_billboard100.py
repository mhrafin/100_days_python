import os
from pprint import pp

import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

ID = os.getenv("SPOTIFY_CLIENT_ID")
SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

date = input("Which year do you want to travel to? Type in YYYY-MM-DD format: ")
year = date[:4]
print(year)

url = f"https://www.billboard.com/charts/hot-100/{date}/"

headers = {"User-Agent": "Mozilla/5.0", "Referer": "https://www.billboard.com/"}

session = requests.Session()
response = session.get(url=url, headers=headers)
response.raise_for_status()

html = response.text
# print(html)

soup = BeautifulSoup(html, "html.parser")
# x = soup.find_all("h3", id="title-of-a-story", class_="c-title")
# print(x)

song_names_spans = soup.select("li ul li h3")
# print(song_names_spans)
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names[7])

song_artists_tag = soup.select("li ul li span")
song_artists = [artist.getText().strip() for artist in song_artists_tag]
print(song_artists[7])


scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=ID,
        client_secret=SECRET,
        redirect_uri="http://example.com",
    )
)

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

profile_info = sp.current_user()
user_id = profile_info["id"]

song_ids = []
for n in range(len(song_names)):
    song = sp.search(
        q=f"track:{song_names[n]} artist:{song_artists[n]}",
        limit=1,
        offset=0,
        type="track",
        market=None,
    )
    print()
    print(n)
    try:
        print(song["tracks"]["items"][0]["id"])
        song_ids.append(song["tracks"]["items"][0]["id"])
    except IndexError:
        pp(song)


print(song_ids)
print(len(song_ids))

new_playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False, description=""
)

new_playlist_id = new_playlist["id"]

# current_playlists = sp.current_user_playlists(limit=50, offset=0)
# pp(current_playlists)

sp.user_playlist_add_tracks(
    user=user_id, playlist_id=new_playlist_id, tracks=song_ids, position=None
)
