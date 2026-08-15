# Ideas & Future Features

Not committed to the roadmap yet — just tracking ideas for later.
(Folder-scan, database, and UI are already tracked in the main Roadmap in README.md)

## Matching quality improvements
- Fuzzy matching for artist/track names (e.g. rapidfuzz) to handle typos
  (e.g. "Ed Sheeren" -> "Ed Sheeran")
- Better ranking when multiple valid matches survive filtering
  (currently just takes results[0])

## CLI improvements
- Batch mode: process a list of "Artist - Track" from a text file,
  instead of one search at a time
- Dry-run flag: preview matches without saving files to disk

## Code quality / portfolio
- Unit tests (pytest) for matching.py and files.py
- GitHub Actions CI to run tests automatically on every push

## Long-term
- Plain lyrics fallback when syncedLyrics is missing but plainLyrics exists