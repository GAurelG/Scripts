#! /usr/bin/python3

# a small script to check the length of music files and compare it. To check the conversion process from FLAC to mp3 went well. 

import os
import tinytag as ttag
import pandas as pd

FLAC_PATH = '/home/aurelien/ParentsMusic_FLAC/'
MP3_PATH = '/home/aurelien/Musique_Convertie/ParentsMusic_FLAC/'

def get_length(musicpath, flac_path = FLAC_PATH, mp3_path = MP3_PATH):
    rm_len = len(flac_path)
    musicname = musicpath[rm_len:-4]
    musicname_FLAC = musicpath[rm_len:]
    musicname_MP3 = musicname + "mp3"
    flac_length = ttag.TinyTag.get(os.path.join(flac_path, musicname_FLAC)).duration
    mp3_length = ttag.TinyTag.get(os.path.join(mp3_path, musicname_MP3)).duration
    return {musicname : (flac_length, mp3_length, flac_length - mp3_length)}

for root, dirs, files in os.walk(FLAC_PATH):
    for name in files:
        fullname = os.path.join(root, name)
        try:
            results.update(get_length(fullname, FLAC_PATH, MP3_PATH))
        except:
            results = get_length(fullname, FLAC_PATH, MP3_PATH)
data = pd.DataFrame.from_dict(results, 
                              orient='index',
                              columns=['flac', 'mp3', 'diff'])
data.index.name = 'musicname'
filtered = data[data["diff"] >= 1]
print("length of the filtered dataframe: {0}\n".format(len(filtered.index)))
print(filtered.head())

zero_len = data[(data["flac"] < 5) | (data["mp3"] < 5)]
print("\nlength of the dataframe of the musics with no length in mp3 or flac: {}\n".format(len(zero_len.index)))

print(data.describe())
print("\n")

print(data.head())
