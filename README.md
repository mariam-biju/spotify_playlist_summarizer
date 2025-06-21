# 🎧 Spotify Playlist Summarizer

A web app built with **Streamlit** and **Spotify's Web API (Spotipy)** that allows users to input a playlist URL and visualize track-level audio features such as **Danceability**, **Energy**, and **Valence**.

---

## 🚀 Features

- 🔍 Fetches Spotify playlist data via URL  
- 📊 Calculates average **danceability**, **energy**, and **valence**  
- 📈 Visualizes audio features across tracks  
- 🧾 Shows a summary table with track name, artist, and features  
- ✅ Built with Streamlit + Spotipy  

---

## 🔐 Spotify API Setup

To use this app, you must register your app at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and get:

- `CLIENT_ID`  
- `CLIENT_SECRET`  
- `REDIRECT_URI` (e.g., `http://localhost:8501/callback`)

Set `SCOPE` to:
```
playlist-read-private user-library-read
```

---

## 🧠 How It Works

1. Authenticate via **SpotifyOAuth**
2. Enter a playlist URL (public or your private playlist)
3. App fetches all tracks and their audio features
4. Displays:
   - 🧾 Summary DataFrame
   - 📊 Bar chart of feature averages
   - 📈 Line chart of feature trends by track

---

## 🖥️ Technologies Used

- `streamlit`  
- `spotipy`  
- `pandas`  
- `matplotlib` (optional, not required unless extended)

---

## ▶️ How to Run

1. Clone the repo and install dependencies:

```
pip install streamlit spotipy pandas
```

2. Replace placeholder API credentials in the script:

```python
CLIENT_ID = "your client id"
CLIENT_SECRET = "your client secret"
REDIRECT_URI = "http://localhost:8501/callback"
```

3. Launch the app:

```
streamlit run app.py
```

---

## 📎 Sample Output

- Playlist summary table (Track, Artist, Danceability, Energy, Valence)  
- Bar chart of average audio features  
- Line chart showing feature trends across the playlist

---

## ⚠️ Notes

- Works best with playlists of 5–100 tracks  
- Requires valid Spotify account with developer access  
- Only works with playlists you have access to (public or yours)

---
