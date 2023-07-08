import os
import datetime
from gtts import gTTS

filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_content.txt")

with open(filepath, "r") as file:
    text = file.read()

speech = gTTS(text=text, lang='en', slow=False)

now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"sample_{now}.mp3"
filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
speech.save(filepath)
