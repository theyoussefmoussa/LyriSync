# LyricSync

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-in%20development-yellow?style=flat-square)
![Requests](https://img.shields.io/badge/Requests-000000?style=flat-square&logo=python&logoColor=white)
![dotenv](https://img.shields.io/badge/python--dotenv-ECD53F?style=flat-square&logo=dotenv&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

A CLI tool that searches for song lyrics online through the [lrclib.net](https://lrclib.net/api/search) API and saves them as `.lrc` (synced lyrics) files.

## Features

- Search lrclib.net by track and artist name
- Filters out instrumental tracks and results missing synced lyrics
- Saves results as clean `.lrc` files, ready to use with any lyrics-aware music player

## Project Structure

```
lyricSync/
├── src/
│   ├── __init__.py
│   ├── api.py         # search and fetch lyrics from lrclib.net
│   ├── matching.py    # filter and match the desired song
│   └── files.py       # file/folder handling
├── Tests/                # output .lrc files land here
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

### Example

```
Enter track name: lose yourself
Enter artist name: eminem
Song Saved: Tests/Eminem - Lose Yourself.lrc
```

## Roadmap

- [x] Minimal structure (initial)
- [X] Validate user input
- [ ] Search for songs in a local folder, then download matching `.lrc` files
- [ ] Connect with a database
- [ ] Build a UI (after database integration)

## Contact Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/theyoussefmoussa)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/theyosefmusa)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/theyoussefmoussa)