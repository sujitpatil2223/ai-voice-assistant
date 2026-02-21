import speech_recognition as sr
import os
import webbrowser


def say(text):
    os.system(f'powershell -Command "Add-Type –AssemblyName System.Speech; '
              f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\');"')

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language = "en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:

            print("Could not understand audio")
            return ""
        except sr.RequestError:
            print("Could not request results from Google")
            return ""

if __name__ == '__main__':
    say("Hello, I am your AI assistant.")
    while True:
        print("Listening....")
        query = takecommand()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],
                 ["google","https://www.google.com"],["spotify","https://www.spotify.com"],
                 ["facebook","https://www.facebook.com"],["instagram","https://www.instagram.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir....")
                webbrowser.open(site[1])
                #say(text)