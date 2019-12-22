#! /usr/bin/python3

# a small script to check the length of music files and compare it. To check the conversion process from FLAC to mp3 went well. 

import os
import tinytag as ttag

FLAC-PATH = "~/SOMETHING"
MP3-PATH = "~/SOMETHINGELSE"

results = {}

def get_length(musicpath, flac_path = FLAC-PATH, mp3_path = MP3_PATH):
    rm_len = len(flac_path)
    musicname = musicpath[rm_len:]
    flac_length = ttag.TinyTag.get(os.path.join(flac_path, musicname)).duration
    mp3_length = ttag.TinyTag.get(os.path.join(mp3_path, musicname)).duration
    return {musicname : (flac_length, mp3_length, flac_length - mp3 length)}

for root, dirs, files in os.walk(FLAC_PATH):
    for name in files:
        print(get_length(os.path.join(root, name)))


# go through the filesystem for FLAC and MP3 structure
# for each file in each side, populate a table row with:
# path as key, one column for MP3 length one column for FLAC
