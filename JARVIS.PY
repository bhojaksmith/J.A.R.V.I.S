import speech_recognition as sr 
import pyttsx3  
import platform
import threading 
import os

language = 'en-IN'

text=''
engine = pyttsx3.init()
platf=platform.system()
timerMap = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}
    
r = sr.Recognizer()  

r.energy_threshold = 300
# (150-4000) Higher value if it tries to recognize when it shouldn’t, and a lower value if it doesn’t recognize when it should.

r.pause_threshold = 0.5
#Represents the minimum length of silence (in seconds) that will register as the end of a phrase.

def SpeakText(command): 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 


#feature functions
def browser():
    os.system('start www.google.com')
def calculator():
    os.system('calc')
def calendar():
    os.system('start outlookcal:')
def photos():
    os.system('start ms-photos:')
def screenshot():
    os.system('start ms-screenclip:')
def mail():
    os.system('outlookmail:')    
def search():
    print('\n\nWhat do you want to search?....\n\n')
    SpeakText('What do you want to search')
    
    searchQuery = r.listen(source2,timeout=6) 
    # The timeout parameter is the maximum number of seconds 
    # that it will wait for a phrase to start before giving up 
    # and throwing a TimeoutException exception. If Value not specified, it will wait indefinitely.

    print("Processing...")
    
    text = r.recognize_google(searchQuery) 
    text = text.lower() 
    SpeakText('Searching for '+text+' on the web')
    
    #print("Searching for  '"+text+"'")

    os.system("start www.google.com/search?q="+text)
    exit()
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
    searchQuery = r.listen(source2,timeout=6) 
    print("\n\nProcessing...\n\n")
    
    text = r.recognize_google(searchQuery) 
    text = text.lower() 
    
    print("\n\nDid you say '"+text+"'\n\n")
    timerStarted = False
    def timerExpired(): 
        print("\n\nTimer Expired\n") 
        SpeakText('Timer Expired')
    if not timerStarted:
        if(text.isdigit()):
            print('\n\nSetting a timer for '+  text +'Minutes\n\n')
            SpeakText('Setting a timer for '+  text +'Minutes') 
            
            timer = threading.Timer(int(text), timerExpired) 
            timer.start() 
        else:
            try:    
                print('\n\nSetting a timer for '+  timerMap[text] +' Minutes\n\n')
                SpeakText('Setting a timer for '+  timerMap[text] +' Minutes') 
                timer = threading.Timer(timerMap[text], timerExpired) 
                timerStarted = True
                timer.start()
            except KeyError:
                print('Please Try again')
                SpeakText('Invalid Value , Please Try again') 
            
    else:
        print('Say Cancel to cancel timer')
        SpeakText('Say Cancel to cancel timer')
        
        searchQuery = r.listen(source2,timeout=6) 
        print("Processing Cancel...")
        
        text = r.recognize_google(searchQuery) 
        text = text.lower() 
        if('cancel' in text):
            print("Cancelling timer\n") 
            timer.cancel() 
                

    
       
functionDict = {
    'browser':browser,
    'Open browser':browser,
    'Open web browser':browser,
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
    'screenshot':search,
    'take a screenshot':search,
    'set a timer':timerX,
    'timer':timerX,
    'cancel timer':timerX
}
activ=False
with sr.Microphone() as source2: 
    r.adjust_for_ambient_noise(source2, duration=1)
    while(1):    
        try:
            if not activ :
                 # print("kem palty")
                print("Say \"Hey Jarvis\" to speak to Jarvis... ")           
                audio2 = r.listen(source2,timeout=None) 
                print("Processing...\n")
                

                text = r.recognize_google(audio2) 
                text = text.lower() 
                print("you said '"+text+"'")
            if 'hey jarvis' in text or 'jarvis' in text:
                print("Listening now!\n")
                #SpeakText("Listening for your command ...")
                activ=True
            if activ:
                print("What do you want to do? ... ")
                SpeakText("What do you want to do\n")
                print("\nThings you can say \n  Open Calculator \n Open Browser \n see help.txt for all commands")
                
                query = r.listen(source2,timeout=6) 
                
                print("\n\nProcessing...\n\n")

                text = r.recognize_google(query) 
                print('\n\nProcessed!\n\n')
                text = text.lower() 

                
                print("\n\nDid you say '"+text+"'\n\n")
                
                #calling function dynamically 
                functionDict[text]()
            

        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 
                
        except sr.UnknownValueError: 
            print("Couldn't Understand please try again !")
            SpeakText('Could not Understand please try again')
