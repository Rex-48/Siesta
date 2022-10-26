# text to speech
import pyttsx3
from textToSpeech import *


# Speech recognition
from vosk import Model , KaldiRecognizer
import pyaudio
import os
import SpeechEngine as SE


# random integer generation function module
import random







# Function to Open THe Driectories through Python Script
def unfold(route):
    os.startfile(route)

# function to work on terminal commands
def terminal(command):
    os.sys(command)

# Affirmation for completing a task
def affirmative():
    x = random.randint(0,5)
    if x == 1 :
        speak("okay master")
    elif x == 2 :
        speak("Affirmative")
    elif x == 3:
        speak("got it")
    elif x == 4:
        speak("done")
    elif x == 5:
        speak("on it sir")
    else:
        speak("done")





# locations for all the applications
google = "X:\Programming\Luxion-Ai\Traces\Google Chrome.lnk"
settings = "X:\Programming\Luxion-Ai\Traces\Settings.lnk"
vscode = "X:\Programming\Luxion-Ai\Traces\Visual Studio Code.lnk"
vlc = "X:\Programming\Luxion-Ai\Traces\VLC media player.lnk"
sublime = "X:\Programming\Luxion-Ai\Traces\Sublime Text.lnk"

thispc = "This PC"
idm = "X:\Programming\Luxion-Ai\Traces\Internet Download Manager.lnk"
gitbash = "X:\Programming\Luxion-Ai\Traces\Git Bash.lnk"
photoshop = "X:\Programming\Luxion-Ai\Traces\Adobe Photoshop CC 2019.lnk"
godot = "X:\Programming\Luxion-Ai\Traces\GODOT Engine.exe - Shortcut.lnk"
intellij = "X:\Programming\Luxion-Ai\Traces\IntelliJ IDEA Community Edition 2022.1.lnk"


# root locations of main files
music = "Music - Shortcut.lnk"
anime = "Amvs - Shortcut.lnk"
download = "Downloads - Shortcut.lnk"
picture = "Pictures - Shortcut.lnk"





# Main Loop

'''
while True:
    user_input = SE.speechInput()
    if user_input == None:
        continue
    else:

        user = user_input.lower()
        print("user : ",user)

        if wordPresent(user, "open"):
            if wordPresent(user, "google") or wordPresent(user, "chrome"):
                affirmative()
                unfold(google)

            elif wordPresent(user, "setting"):
                affirmative()
                unfold(settings)

            elif wordPresent(user, "vs code") or wordPresent(user, "code"):
                affirmative()
                unfold(vscode)
            
            elif wordPresent(user, "vlc") or wordPresent(user, "media player"):
                affirmative()
                unfold(vlc)
                
            elif wordPresent(user, "sublime"):
                affirmative()
                unfold(sublime)

            elif wordPresent(user, "this pc") or wordPresent(user, "root directory"):
                affirmative()
                unfold(thispc)

            elif wordPresent(user, "idm") or wordPresent(user, "download manager"):
                affirmative()
                unfold(route)

        elif wordPresent(user, "activate"):
            pass

        elif wordPresent(user, "fire"):
            pass

        elif wordPresent(user, "launch"):
            pass

        elif wordPresent(user, "run"):
            pass

        elif wordPresent(user, "execute"):
            pass
        

        elif wordPresent(user, "search"):
            pass
        

        elif wordPresent(user, "i wish"):
            engine.setProperty('rate', rate-10)
            speak(" As your dear kettle ! I couldn't agree more  ,my dear pot.")
        
        elif wordPresent(user, "shutdown"):
            if wordPresent(user, "system"):
                terminal("shutdown /s")
            if wordPresent(user, "core program"):
                terminal("exit")

        elif wordPresent(user, "power down"):
            break

        elif type(user) == str :
            x = random.randint(0, 4)
            if x == 1 :
                speak("cannot compute : ")
            elif x==2 :
                speak("cannot comprehend : ")
            elif x==3 :
                speak("hey , master could u repeat that : ")
            else : 
                speak("cannot compute : ")
                speak("cannot comprehend : ")

'''


speak("lu-kcion")

























