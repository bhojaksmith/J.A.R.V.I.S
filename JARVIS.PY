import os 
import platform
# from gtts import gTTS 
# from mpyg321.mpyg321 import MPyg321Player()
import speech_recognition as sr 
import pyttsx3  
import threading 
import subprocess
t = {'1':1,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}

    #remove inside later
  

language = 'en-IN'
#player = MPyg321Player()
engine = pyttsx3.init()
#player.play_song("/path/to/some_mp3.mp3")
    
r = sr.Recognizer()  
platf=platform.system()
r.energy_threshold = 300
r.pause_threshold = 0.5
def SpeakText(command): 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
activ=False
with sr.Microphone() as source2: 
    r.adjust_for_ambient_noise(source2, duration=1)
    while(1):    
        #print("simon come back") 
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
                print("\nThings you can say \n Search \n Set a timer \n Open Calculator \n Open Browser \n see help.txt for all commands")
              
                query = r.listen(source2,timeout=3) 
                
                print("\n\nProcessing...\n\n")
  
                text = r.recognize_google(query) 
                print('\n\nProcessed!\n\n')
                text = text.lower() 

                print("\n\nDid you say '"+text+"'\n\n")

                if('search' in text):
                    print('\n\nWhat do you want to search?....\n\n')
                    SpeakText('What do you want to search')
                    searchQuery = r.listen(source2,timeout=3) 
                    print("Processing...")
                    
                    text = r.recognize_google(searchQuery) 
                    text = text.lower() 
                    SpeakText('Searching for '+text+' on the web')
                    
                    #print("Searching for  '"+text+"'")
            
                    os.system("start www.google.com/search?q="+text)
                    exit()
                elif(text=='good night'):
                    print('PC shutting down....')
                    #playsound('caged_goodnight.mp3')
                    if(platf=="Linux"):
                        os.system("shutdown")
                        print("shutdown scheduled after 1 minute...")
                    else:
                        os.system("shutdown /s /t 2")
                        exit()

                
                
                elif('timer' in text):
                    print("\n\nHow many minutes?\n\n")
                    SpeakText('How many minutes?')
                    searchQuery = r.listen(source2,timeout=3) 
                    print("\n\nProcessing...\n\n")
                    
                    text = r.recognize_google(searchQuery) 
                    text = text.lower() 
                    
                    print("\n\nDid you say '"+text+"'\n\n")

                    def timerX(): 
                        print("\n\nTimer Expired\n") 
                        

                    if(text.isdigit()):
                        print('\n\nSetting a timer for '+  text +'Minutes\n\n')
                        SpeakText('Setting a timer for '+  text +'Minutes') 
                        
                        timer = threading.Timer(int(text)*60, timerX) 
                        timer.start() 
                    else:
                        try:    
                            print('\n\nSetting a timer for '+  t[text] +' Minutes\n\n')
                            SpeakText('Setting a timer for '+  t[text] +' Minutes') 
                            timer = threading.Timer(t[text], timerX) 
                            timer.start()
                        except KeyError:
                            print('Please Try again')
                            SpeakText('Invalid Value , Please Try again')        
 
                    
                    # print('Say Cancel to cancel timer')
                    # SpeakText('Say Cancel to cancel timer')
                    
                    # searchQuery = r.listen(source2,timeout=4) 
                    # print("Processing Cancel...")
                    
                    # text = r.recognize_google(searchQuery) 
                    # text = text.lower() 
                    # if(text=="cancel"):
                    #     print("Cancelling timer\n") 
                    #     timer.cancel() 
                    
                        
                    
                # Windows Only
                elif('browser' in text):
                    os.system('start www.google.com')
                elif('calculator' in text):
                    os.system('calc')
                elif('calendar' in text):
                    os.system('calc')
                elif('camera' in text):
                    os.system('start microsoft.windows.camera:')
                elif('photos' in text):
                    os.system('start ms-ph:')        
                elif('exit' in text):
                    print("Good bye sir !")
                    SpeakText('Good Bye ....... Sir')
                    exit()
                #print('Simon Go back')
            
        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 
                
        except sr.UnknownValueError: 
            print("Couldn't Understand please try again !")
            SpeakText('Could not Understand please try again')
        
