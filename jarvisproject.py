import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I am your AI virtual assistant. How can I help you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Please say that again...")
        return "None"
    return query

def getWeather():
    api_key = "your_weather_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("Please tell me the city name")
    city_name = takeCommand().lower()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        speak(f"The temperature in {city_name} is {temperature - 273.15:.2f} degree Celsius with {weather_description} and humidity of {humidity} percent.")
    else:
        speak("City not found. Please try again.")

def getNews():
    api_key = "your_news_api_key"
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    response = requests.get(url)
    news_data = response.json()
    articles = news_data['articles']
    speak("Here are the top news headlines")
    for i, article in enumerate(articles[:5], 1):
        speak(f"Headline {i}: {article['title']}")
        if i < 5:
            speak("Next news...")

if __name__ == "__main__":
    speak("Hello!")
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'your_music_directory'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'weather' in query:
            getWeather()

        elif 'news' in query:
            getNews()

        elif 'exit' in query or 'quit' in query or 'bye' in query:
            speak("Goodbye! Have a great day!")
            break

        else:
            speak("I didn't understand that command. Please try again.")
