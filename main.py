import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from client import get_generated_text

# agar bada kaam
# form gtts import gTTs
# pip install gTTs
# def speak(text):
#   tts=gTTS(text)
#   tts.save("temp.mp3") 




# import pyttsx3
# engine=pyttsx3.init()
# engine.say("jai shree raam")
# engine.runAndWait()

recognizer = sr.Recognizer()# Recognizer ek class hai jo speech recognitaion me help karengi
engine = pyttsx3.init()
newsapi = "your api"

# Your Hugging Face API token
api_token = "your api"
# Model name you want to use
model_name = "gpt2"
# Prompt text
# prompt = "Once upon a time,"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommmand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open gpt" in c.lower():
        webbrowser.open("https://openai.com/index/chatgpt/")
    elif "open snapchat" in c.lower():
        webbrowser.open("https://www.snapchat.com/")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "open code forces" in c.lower():
        webbrowser.open("https://codeforces.com/")
    elif "open netflix" in c.lower():
        webbrowser.open("https://www.netflix.com/in/")

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link) 

    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=a6f6e8aa733b4fbfb3ad2b0ff17ccb10")
        if r.status_code == 200:
            data = r.json()
    
            headlines = [article['title'] for article in data['articles'][:5]]
            for i, headline in enumerate(headlines, start=1):
                print(f"{i}. {headline}")
                speak(headline)
        else:
          print(f"Failed to retrieve news: {r.status_code}")
        # let open ai handel the ther request
    elif "shut up" in c.lower() or "close" in c.lower():
        speak("turning off")
        exit(0)
    
    else:
        try:
            prompt = c
            generated_text = get_generated_text(api_token, model_name, prompt)
            print("Generated Text:")
            print(generated_text)
            speak(generated_text)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__== "__main__":
    speak("Intializing Jarvis.....")
    while True:
        # audio_file = sr.AudioFile('path_to_your_audio_file.wav')
        r=sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone()as source:
                print("listning...")
                audio=r.listen(source,timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            # print(word)
            if(word.lower()=="jarvis"):
                speak("yes?")
                #listen for command
                with sr.Microphone() as source:
                    print("listning to command...")
                    audio = r. listen(source,timeout=10, phrase_time_limit=10)
                    command = r.recognize_google(audio)   
                    processCommmand(command)


        except sr.UnknownValueError:
            print("Could not understand audio")
            speak("Sorry, I did not catch that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("Sorry, there was an error with the recognition service.")
        except Exception as e: 
            print(f"Jarvis error: {e}")
            speak("An error occurred. Please try again.")
        # except Exception as e:
        #     print("jarvis error : {0}".format(e))

        # except sr.UnknownValueError :
        #     print("jarvis could not understand audio")
        # except sr.WaitTimeoutError:
        #     print("kuch nahi bola")


        # listen for the wake word jarvis
