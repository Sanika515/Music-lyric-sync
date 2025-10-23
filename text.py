import syncedlyrics
import json
import re

def get_lyrics(song_name):
    lrc = syncedlyrics.search(song_name)
    if not lrc:
        return None
    
    pattern = r"\[(\d+):(\d+\.\d+)\](.*)"
    lyrics = []
    for line in lrc.splitlines():
        match = re.match(pattern, line)
        if match:
            minutes, seconds, text = match.groups()
            total_seconds = int(minutes) * 60 + float(seconds)
            lyrics.append({"time": total_seconds, "text": text.strip()})
    
    with open("lyrics.json", "w", encoding="utf-8") as f:
        json.dump(lyrics, f, indent=4)
    
    return lyrics

# Example test:
# get_lyrics("Champion")
