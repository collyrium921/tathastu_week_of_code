import webbrowser as wb
import speech_recognition as sr
from tkinter import *
from time import ctime
import time
import os
from gtts import gTTS
import pygame
from pygame import mixer

def speak(audioString):
    global x
    b = audioString
    if len(b) == 0:
        #w1 = Label(root, text="No input!").pack()
        return
    tts = gTTS(text=b, lang='en-in')
    tts.save("voice%s.mp3"%(x))
    pygame.init()
    pygame.display.set_mode((2, 1))
    mixer.music.load("voice%s.mp3" % (x))
    mixer.music.play(0)

    x += 1

    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)

def recordingAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Speak...")
        audio = r.listen(source)
        print("Okay! heard...")
    data = ""
    try:
    # Uses the default API key
    # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said : " + data )
    except sr.UnknownValueError:
        print("Sorry! Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Sorry! not able to request results from Google Speech Recognition service; {0}".format(e))
    return data

def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    elif "what time is it" in data:
        speak(ctime())

    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Kajal, I will show you where " + location + " is.")
        wb.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;")
    else :
        speak("Sorry! I did not get what you said !")


print("let's begin.............")
speak("Hi Kajal, how can I help you?")
data = recordingAudio()
jarvis(data)
speak("Turning off the program.")
print("Run completed")
