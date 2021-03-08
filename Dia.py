#project Python Berbasis Speech Recognition
import os
import speech_recognition as sr
from playsound import playsound

recognizer = sr.Recognizer()

''' Rekam Suara '''

with sr.Microphone() as source:
    print("Penyesuaian..... ")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Rekam suara 10 detik...")
    recorded_audio = recognizer.listen(source, timeout=10)
    print("Berhasil Direkam..")

try:
    print("Text sedang diterjemahkan...")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="en-US"
        )
    print("Text yang diterjemahkan : {}".format(text))

    if text == 'I love you':
        print('you too')

    if text == "open":
        playsound('hime.mp3')

except Exception as ex:
    print(ex)