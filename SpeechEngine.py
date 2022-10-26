from vosk import Model , KaldiRecognizer
import pyaudio
import os

model = Model(r"X:\Programming\Luxion-Ai\SpeechEngine-Model\vosk-model-small-en-us-0.15") # here the r reperesents the absolute path 
recognizer = KaldiRecognizer(model , 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format = pyaudio.paInt16 , channels = 1 ,rate = 16000 , input = True , frames_per_buffer = 8192)
stream.start_stream()
os.system("cls")

def speechInput() :
    data = stream.read(4096 , exception_on_overflow = False)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        return text[14:-3]