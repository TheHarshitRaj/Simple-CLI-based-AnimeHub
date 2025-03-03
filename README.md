# Simple-CLI-based-AnimeHub
A CLI based one stop destination for all needs, whether it'd be searching for an anime, creating and editing your watchlist, or even watching an anime.
---

## Features 🚀

✅ **Search Anime** – Instantly search for anime on MyAnimeList.  
✅ **Create a Watchlist** – Categorize anime into _Plan to Watch_, _Watching_, _Completed_, and _Dropped_.  
✅ **Edit Watchlist** – Update an existing watchlist anytime.  
✅ **Watch Anime** – Redirects users to anime streaming sites (HiAnime, Miruro, AnimeZ, AnimeKai).  
✅ **Persistent Storage** – Saves and loads watchlists using a JSON file (`Watchlist.txt`).  

---

## Installation & Setup 🛠️

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/anime-watchlist.git
   cd anime-watchlist
   ```

2. **Ensure you have Python installed (3.x recommended).**  

3. **Run the script:**
   ```bash
   python anime_watchlist.py
   ```

---

## Usage 📖

When you run the script, you’ll be asked to choose an action:

- **(a) Search for an Anime** – Opens MyAnimeList with search results.
- **(b) Watch some Anime** – Lets you select a streaming platform.
- **(c) Create your watchlist** – Adds anime under different categories.
- **(d) Edit your Watchlist** – Updates an existing watchlist.

### Example of Adding to Watchlist
```
Enter category (Plan to Watch, Watching, Completed, Dropped): Watching
Enter anime names to add. Type 'Exit' to stop.
: Attack on Titan
: One Piece
: Exit
```
This will save the watchlist under the `Watching` category.

---

## Dependencies 📦
This script uses Python’s built-in modules:
- `webbrowser` – Opens anime search and streaming websites.
- `time` – Adds delay effects for better user experience.
- `json` – Saves and loads the watchlist data.

_No external libraries are required!_

---

## Contributing 🤝
Feel free to fork this repository and submit a pull request if you have any improvements!  

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

---

## License 📜
This project is licensed under the MIT License. You are free to modify and distribute it.
