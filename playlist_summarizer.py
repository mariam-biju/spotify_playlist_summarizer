import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import matplotlib.pyplot as plt

# --- Spotify API credentials ---
CLIENT_ID = "your client id "
CLIENT_SECRET = "your client secret"
REDIRECT_URI = "http://localhost:8501/callback"
SCOPE = "playlist-read-private user-library-read"

# --- Spotify Auth ---
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

# --- Streamlit UI ---
st.title("🎧 Spotify Playlist Summarizer")
playlist_url = st.text_input("Enter a Spotify Playlist URL:")

if playlist_url:
    try:
        playlist_id = playlist_url.split("/")[-1].split("?")[0]
        playlist = sp.playlist(playlist_id)
        tracks = playlist["tracks"]["items"]

        track_data = []
        for item in tracks:
            track = item["track"]
            if track is None: continue
            features = sp.audio_features(track["id"])[0]
            if features is None: continue
            track_data.append({
                "Track": track["name"],
                "Artist": track["artists"][0]["name"],
                "Danceability": features["danceability"],
                "Energy": features["energy"],
                "Valence": features["valence"]
            })

        df = pd.DataFrame(track_data)

        st.subheader("🎵 Playlist Summary")
        st.dataframe(df)

        st.subheader("📊 Audio Feature Averages")
        avg_features = df[["Danceability", "Energy", "Valence"]].mean()
        st.bar_chart(avg_features)

        st.subheader("📈 Feature Trend by Track")
        st.line_chart(df[["Danceability", "Energy", "Valence"]])

    except Exception as e:
        st.error(f"Something went wrong: {e}")
