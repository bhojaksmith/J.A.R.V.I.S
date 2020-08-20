import speech_recognition as sr 
import pyttsx3  
import os
language = 'en-IN'

engine = pyttsx3.init()

    
r = sr.Recognizer()  
r.energy_threshold = 300
r.pause_threshold = 0.5

def SpeakText(command): 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 



def browser():
    os.system('start www.google.com')
def calculator():
    os.system('calc')
functionDict = {
    'browser':browser,
    'calculator':calculator
}
with sr.Microphone() as source2: 
    r.adjust_for_ambient_noise(source2, duration=1)
    while(1):    
        try:
            
            print("What do you want to do? ... ")
            SpeakText("What do you want to do\n")
            print("\nThings you can say \n  Open Calculator \n Open Browser \n see help.txt for all commands")
            
            query = r.listen(source2,timeout=3) 
            
            print("\n\nProcessing...\n\n")

            text = r.recognize_google(query) 
            print('\n\nProcessed!\n\n')
            text = text.lower() 

            
            print("\n\nDid you say '"+text+"'\n\n")
            
            #calling function dynamically , No if statements !
            functionDict[text]()
            

        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 
                
        except sr.UnknownValueError: 
            print("Couldn't Understand please try again !")
            SpeakText('Could not Understand please try again')
        
