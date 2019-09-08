#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:52:13 2019

@author: rishabh
"""

import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    
'''getting microphone input'''
def get_audio():
    '''create a recognizer object from sr module'''
    r = sr.Recognizer() 
    '''use the microphone to get some type of input'''
    with sr.Microphone() as source: 
        '''use our speech recognizer to listen to the source'''
        audio = r.listen(source) 
        said = ""
        
        try:
            '''use google api to recognize what we said'''
            said = r.recognize_google(audio) 
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    
    return said
    
text = get_audio()

if "hello" in text:
    speak("hello motherfucker")

if "hi" in text:
    speak("Fuck off")