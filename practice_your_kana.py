#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:00:16 2020

Hello time traveler. The code below is taken from a Yiutube channel called "The Morpheus Tutorials"
--> https://www.youtube.com/watch?v=jUcQGAvtSCc
When I have mastered the kana I will implement the kana signs intio the code.
Now I will eat a banana. Tasty.

@author: snake-earthrunner
"""
import random

class Entry:
    def __init__(self, sound, hiragana):
        self.sound = sound
        self.hiragana = hiragana
    def toString(self):
        return self.sound + " - " + self.hiragana
        
kana = [Entry("Katze", "neko")]

def eingabe():
    while True:
        sound = input("Type the sound: ")
        if sound == "#fertig":
            return
        hiragana = input("Type the Hiragana: ")
        if hiragana == "#fertig":
            return
        kana.append(Entry(sounds, hiraganas))

def test():
    while True:
        i = random.randint(0, len(kana)-1)
        hiragana = input("Sound Übersetzung von " + kana[i].sound + ":  ")
        if hiragana == "#fertig":
            return
        if kana[i].hiragana == hiragana_input:
            print ("korrekt")
        else:
            print ("Leider falsch. Richtige Antwort: " + kana[i].hiragana)
        
def printall():
    for item in kana:
        print (item.toString())
       
        
while True:
    
    command = input("Command: ")
    if command == "eingabe":
        eingabe()
    elif command == "test":
        test()
    elif command == "beenden":
        break
    elif command == "ausgabe":
        printall()
    else:
        print( "keine bekannte Aushabe. Tippe eingabe, test, ausgabe oder beenden")

