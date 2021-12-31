# First thing to do 
# Install the following libraries :
# pip install speechrecognition / pip install pyttsx3 /  pip install neuralintents

# Code section 
#from neuralintents import GenericAssisstant 
#import speech_recognition  
#import pyttsx3 as tts  / text to speech 
# import sys 




recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

todo_list = ['Go Shopping', 'Clean Room', 'Record']


def create_note():
    global recognizer

    speaker.say("What do you want to write onto your note?")
    speaker.runAndWait()

    done = False

    while not done: 
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
           
                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Choose a filename!")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                 
                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

assistant = GenericAssisstant('intents.json') 
assistant.train_model()
