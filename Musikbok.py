from gtts import gTTS
import os

# define variables
s = "escape with plane"
file = "file.mp3"

# initialize tts, create mp3 and play
tts = gTTS(s, 'en')
tts.save(file)
os.system("mpg123 " + file)