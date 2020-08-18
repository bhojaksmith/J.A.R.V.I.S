import os 
import platform
# from gtts import gTTS 
# from mpyg321.mpyg321 import MPyg321Player()
import speech_recognition as sr 
import pyttsx3  
language = 'en'
#player = MPyg321Player()
engine = pyttsx3.init()
#player.play_song("/path/to/some_mp3.mp3")
    
r = sr.Recognizer()  
    
def SpeakText(command): 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
activ=False
while(1):     
        
    try: 
        with sr.Microphone() as source2: 
            r.adjust_for_ambient_noise(source2, duration=2) 
            if not activ :
                print("Speak \"Jarvis\" to activate ... ")           
                audio2 = r.listen(source2) 
                print("Processing...")
                platf=platform.system()

                text = r.recognize_google(audio2) 
                text = text.lower() 
                #print("Did you say '"+text+"'")
                if text=="jarvis" :
                     print("listening now!")
                     SpeakText("Listening for your commands ...")
                    #  engine.say("Activated")
                    #  engine.runAndWait()

                     activ=True
                if activ:
                    text="A"
                    
                    print("What do you want to do? ... ")
                    SpeakText("What do you want to do?")
                    # engine.say("What do you want to do?")
                    # engine.runAndWait()
            
                    
                    
                              
                    r.adjust_for_ambient_noise(source2, duration=2)
                    audio2 = r.listen(source2) 
                    print("Processing...")
                    SpeakText('Processing')
                    # engine.say("processing")
                    # engine.runAndWait()
                    platf=platform.system()

                    text = r.recognize_google(audio2) 
                    text = text.lower() 
                    #print("Did you say '"+text+"'")
                    if(text=='search'):
                        print('What do you want to search?....')
                        SpeakText('What do you want to search')
                       # engine.say("What do you want to search")
                       # engine.runAndWait()
                        r.adjust_for_ambient_noise(source2, duration=2)
                        audio2 = r.listen(source2) 
                        print("Processing...")
                        SpeakText('Processing')
                        engine.runAndWait()
                        platf=platform.system()

                        text = r.recognize_google(audio2) 
                        text = text.lower() 
                        SpeakText('Searching for '+text+' on the web')
                        
                        #print("Searching for  '"+text+"'")
                
                        os.system("start www.google.com/search?q="+text)
                        #exit()
                    if(text=='good night'):
                        print('pc shutting down....')
                        #playsound('caged_goodnight.mp3')
                        if(platf=="Linux"):
                            os.system("shutdown")
                            print("shutdown scheduled after 1 minute...")
                        else:
                            os.system("shutdown /s /t 2")
                            exit(); 

                    if(text=="sleep"):
                        print("Good bye sir !")
                
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
            
    except sr.UnknownValueError: 
        print("Couldn't Understand please try again !")
        engine.say("Could not Understand please try again")
        engine.runAndWait() 
