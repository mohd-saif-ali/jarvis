import pyttsx3
import speech_recognition as sr
import datetime
 
engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
print(voice[1].id)
engine.setProperty('voice',voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
         speak("good evening!")

    speak("iam AI virtual assistant")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("listning")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("recognitising.....")

        query=e.recognize_google(audio,language='en-in')

        print("user said:{query}\n")
    except Exception as e:
       # print(e)

        print("please say that again please......")
        return "None"
        return query

if __name__ == "__main__" :
    speak("hello ")
    wishMe()
    takeCommand()