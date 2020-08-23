#for ubuntu install "sudo apt install libespeak1"

import os
import speech_recognition as sr 
import pyttsx3  
import platform
import threading 
from pyttsx3 import drivers
import inspect
import time

print("============================================================")
print("\n\n****\t\t\t JARVIS 1.0\t\t\t****\n\n")
print("============================================================")



# print([m[0] for m in inspect.getmembers(pyttsx3, inspect.isclass) if m[1].__module__ == 'pyttsx3'])

def SpeakText(command): 
    engine = pyttsx3.init()                          #
    engine.say(command)  
    engine.runAndWait()


language = 'en-IN'
platf=platform.system()

text=''
engine = pyttsx3.init('dummy')
platf=platform.system()


timerMap = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}
# While setting timer if speechrecognition picks up numbers as words


r = sr.Recognizer()  

r.energy_threshold = 300
# (150-4000) Higher value if it tries to recognize when it shouldn’t, and a lower value if it doesn’t recognize when it should.

r.pause_threshold = 0.5
#Represents the minimum length of silence (in seconds) that will register as the end of a phrase.

 


#feature functions
def browser():
    print("Opening web browser\n")
    if(platf=="Linux"):
        os.system("gio open https://www.google.com &")
    else:
        os.system("start https://www.google.com")
def calculator():
    print("Opening calculator\n")
    if(platf=="Linux"):
        os.system("gnome-calculator &")
    else:
        os.system('calc')
def calendar():
    print("Opening calendar\n")
    if(platf=="Linux"):
        os.system('gnome-calendar &')
    else:
        os.system("start outlookcal:")
def photos():
    print("Opening photos\n")
    if(platf=="Linux"):
        print("Not Available !")
    else:
        os.system('start ms-photos:')
def screenshot():
    print("Taking screenshot\n")
    if(platf=="Linux"):
        os.system("gnome-screenshot")
    else:
        os.system('start ms-screenclip:')
def mail():
    print("Opening mail\n")
    if(platf=="Linux"):
        os.system("thunderbird")
    else:
        os.system('outlookmail:')
        
def search():
    print('What do you want to search?....\n\n')
    SpeakText('What do you want to search')
    
    searchQuery = r.listen(source2) 
    # The timeout parameter is the maximum number of seconds 
    # that it will wait for a phrase to start before giving up 
    # and throwing a TimeoutException exception. If Value not specified, it will wait indefinitely.

    print("Processing...")
    
    text = r.recognize_google(searchQuery, language='en-IN') 
    text = text.lower() 
    SpeakText('Searching for '+text+' on the web')
    
    #print("Searching for  '"+text+"'")
    if(platf=="Linux"):
        os.system("gio open https://www.google.com/search?q="+text)
    else:
        os.system("start www.google.com/search?q="+text)
    
def shutdown():
    print('PC shutting down....')
    #playsound('caged_goodnight.mp3')
    if(platf=="Linux"):
        os.system("shutdown")
        print("shutdown scheduled after 1 minute...")
    else:
        os.system("shutdown /s /t 2")
        exit()
def timerX():
    print("\n\nHow many minutes?\n\n")
    SpeakText('How many minutes?')
    searchQuery = r.listen(source2) 
    print("\n\nProcessing...\n\n")
    
    text = r.recognize_google(searchQuery, language='en-IN') 
    text = text.lower() 

    print("\n\nDid you say '"+text+"'\n\n")
    timerStarted = False
    def timerExpired(): 
        print("\n\nTimer Expired\n") 

    if not timerStarted:
        if(text.isdigit()):
            print('\n\nSetting a timer for '+  text +' Minutes\n\n')
            SpeakText('Setting a timer for '+  text +' Minutes') 
            
            timer = threading.Timer(int(text)*60, timerExpired) 
            timer.start() 
        else:
            try:    
                print('\n\nSetting a timer for '+  timerMap[text] +' Minutes\n\n')
                SpeakText('Setting a timer for '+  timerMap[text] +' Minutes') 
                timer = threading.Timer(timerMap[text]*60, timerExpired) 
                timerStarted = True
                timer.start()
                
            except KeyError:
                print('Please Try again')
                SpeakText('Invalid Value , Please Try again') 
            
    else:
        print('Say Cancel to cancel timer')
        SpeakText('Say Cancel to cancel timer')
        
        searchQuery = r.listen(source2) 
        print("Processing Cancel...")
        
        text = r.recognize_google(searchQuery, language='en-IN') 
        text = text.lower() 
        if('cancel' in text):
            print("Cancelling timer\n") 
            timer.cancel() 
                

    
       
functionDict = {
    'browser':browser,
    'open browser':browser,
    'open web browser':browser,
    'calculator':calculator,
    'open calculator':calculator,
    'calendar':calendar,
    'open calendar':calendar,
    'photos':photos,
    'open photos':photos,
    'good night':shutdown,
    'shutdown':shutdown,
    'search':search,
    'search for':search,
    'screenshot':screenshot,
    'take a screenshot':screenshot,
    'set a timer':timerX,
    'set timer':timerX,
    'timer':timerX,
    'cancel timer':timerX
}
activ=False
with sr.Microphone() as source2: 
    r.adjust_for_ambient_noise(source2, duration=2)
    while(1):    
        try:
            if not activ :
                 # print("kem palty")
                print("Say \"Hey Jarvis\" or \"Jarvis\" to speak to Jarvis... ")           
                SpeakText("Speak hey jarvis to activate")
                audio2 = r.listen(source2) 
                print("Processing...\n")
                

                text = r.recognize_google(audio2, language='en-IN') 
                text = text.lower() 
                print("you said '"+text+"'")
            if 'hey jarvis' in text or 'jarvis' in text:
                print("Listening now!\n")
                #SpeakText("Listening for your command ...")
                activ=True
            if activ:
                print("What do you want to do? ... ")

                SpeakText("What do you want to do\n")
                time.sleep(3)
                print("\nThings you can say \n  Open Calculator \n  Open web browser \n  Shutdown OR Good night \n  Set a timer")
                print("  Open Calendar \n  Take a screenshot \n  Search  \n  Open Photos")
                print("see help.txt for all commands")
                # try:
                query = r.listen(source2) 
                # except Exception as e:
                #     print(e)
                #     query = None
                    
                # print(type(query))
                if(query!=None):
                    print("\nProcessing...")

                    text = r.recognize_google(query, language='en-IN') 
                    print('\nProcessed!\n')
                    text = text.lower() 

                    #calling function dynamically 
                    try:
                        functionDict[text]()
                    except KeyError as e:
                        print("Did you say '"+text+"'\n\n")
                        print("Sorry, we don't do that here !")
                        #https://i.imgur.com/RUdPyQP.jpg


        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 
                
        except sr.UnknownValueError: 
            print("Couldn't Understand please try again !")
            #SpeakText('Could not Understand please try again')

        print("=======================================================================================")
