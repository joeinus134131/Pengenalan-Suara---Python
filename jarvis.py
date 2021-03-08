# importing pyttsx3
import os
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
from playsound import playsound
# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            # returning none if there are errors
            return "None"
    # returning audio as text
    import time
    time.sleep(2)
    return Query
    
# creating Speak() function to giving Speaking power
# to our voice assistant 
def Speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()


# Driver Code
if __name__ == '__main__':
    # using while loop to communicate infinitely
    while True:
        command = take_commands()
        if "exit" in command:
            Speak("Sure sir! as your wish, bai")
            break
        if "insta" in command:
            Speak("Best python page on instagram is pythonhub")
        if "learn" in command:
            Speak("copyassignment website is best to learn python")
        if "code" in command:
            Speak("You can get this code from copyassignment website")

        if "hello" in command:
            Speak("Hai sir, How are you today?")

        if "play a music" in command:
            playsound('hime.mp3')

        if "shut down" in command:
            Speak("Do you want to shutdown your computer sir?")
            while True:
                command = take_commands()
                if "no" in command:
                    Speak("Thank u sir I will not shut down the computer")
                    break
                if "yes" in command:
                    # Shutting down
                    Speak("Shutting the computer")
                    os.system("shutdown /s /t 10")
                    break
            Speak("Say that again sir")
        if "I'm fine" in command:
            Speak("nice sir, i want you in health condition")