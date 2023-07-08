import os
import glob
import re
from moviepy.editor import *

filepaths = sorted(glob.glob("*.mp3"))

def extract_timestamp(filepath):
    match = re.search(r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}", filepath)
    if match:
        return match.group()
    return filepath

filepaths.sort(key=lambda filepath: extract_timestamp(filepath))
clips = [AudioFileClip(filepath) for filepath in filepaths]

concatenated = concatenate_audioclips(clips)

filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "merged.mp3")
concatenated.write_audiofile(filepath)
