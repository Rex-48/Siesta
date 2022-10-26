import pyttsx3 # importing python text to speech module

# Setting up the engine to initiate
engine = pyttsx3.init()

# seeting the speed rate and engine property
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)

# speech and runAndWait functions
def speak(speech):
    print(speech)
    engine.say(speech)
    engine.runAndWait()


# Function to check Word Present
def wordPresent(word,char):
    if word.find(char)==-1:
        return False
    else:
        return True

