def pick_best_match(results: list, artist_name: str):
    """
    Filter candidates down to a usable match.
    Returns the chosen result dict, or None if nothing qualifies.
    """
    if not results: 
        print("No Songs Found, Check Your Internet Connection")
        return 
    # 1. Drop instrumental results
    results = [song for song in results if not song.get("instrumental")]

    # 2. Drop results without synced lyrics
    results = [song for song in results if song.get("syncedLyrics") is not None]

    # 3. among what's left, keep only results whose artistName case-insensitively matches artist_name
    results = [song for song in results if song.get("artistName").lower() == artist_name.lower()]

    # 4. return the first survivor, or None if the list is empty
    if results: 
        return results[0]
    return None