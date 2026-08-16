# LyricSync

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-in%20development-yellow?style=flat-square)
![Requests](https://img.shields.io/badge/Requests-000000?style=flat-square&logo=python&logoColor=white)
![dotenv](https://img.shields.io/badge/python--dotenv-ECD53F?style=flat-square&logo=dotenv&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
# Add Mutagen here
A CLI tool that searches for song lyrics online through the [lrclib.net](https://lrclib.net/api/search) API and saves them as `.lrc` (synced lyrics) files.

## Features

- Search lrclib.net by track and artist name
- Filters out instrumental tracks and results missing synced lyrics
- Saves results as clean `.lrc` files, ready to use with any lyrics-aware music player

## Project Structure

```
lyricSync/
├── src/
│   └── __init__.py
│   ├── api.py          # search and fetch lyrics from lrclib.net
│   ├── cli.py # orchestrates the single-song interactive workflow
│   └── constants.py    # Shared Variables and Functions
│   └── files.py        # file/folder handling
│   └── matching.py     # filter and match the desired song
│   └── pipeline.py     # orchestrates the folder-scan workflow (scan -> search -> match -> save)
│   └── validators.py   # validation Functions
├── Tests/              # output .lrc files land here
├── main.py             # entry point
├── requirements.txt
├── .env
└── .gitignore
```

## How to Run

### Linux

Set up the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

### Windows

Set up the virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

> If `activate` is blocked by PowerShell's execution policy, run PowerShell as Administrator and use:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> then retry activation.

### Example: single-song lookup

```
Welcome to the Lyric Sync Tool!
Type 'exit' to exit the program
Enter '1' for a specific song or '2' for a folder scan: 1
Enter track name: Lose Yourself
Enter artist name: Eminem
Song saved in {path}/Eminem - Lose Yourself.lrc
 ```
> **Note:** `{path}` is replaced with the path set in your local `.env` file.

### Example: folder scan
```
Enter '1' for a specific song or '2' for a folder scan: 2
Do you want to scan the default testing folder or specify a folder? (default/specific): specific
Enter the folder path: /home/youssef/Music
Scanned File: Eminem - Lose Yourself.mp3
Best Match: Lose Yourself by Eminem from album 8 Mile
Scanned File: Untagged Track.mp3
Skipping Untagged Track.mp3: no ID3 tag found.
```
## Roadmap

- [x] Minimal structure (initial)
- [X] Validate user input
- [X] Search for songs in a local folder, then download matching `.lrc` files
- [ ] Connect with a database
- [ ] Build a UI (after database integration)

## Contact Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/theyoussefmoussa)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/theyosefmusa)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/theyoussefmoussa)