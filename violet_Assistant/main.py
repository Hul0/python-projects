import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)


def speak(audio):
    print("Violet: ", audio)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Violet. Please tell me how may I help you ?")


def takeCommand():
    # It takes microphone input from the user and returns string output
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        # listener.adjust_for_ambient_noise(source, duration=5)
        print("Listening...")
        listener.pause_threshold = 1
        audio = listener.listen(source)

    try:
        print("Recognizing...")
        query = listener.recognize_google(audio)

    except Exception as e:
        print("Please try again....")
        return "none"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        command = takeCommand().lower()
        print("User: ", command)

        if 'violet' in command:
            command = command.replace(' violet ', '')
        else:
            command = command
        if command == "none":
            speak("Please Try Again")
            command = takeCommand().lower()
            print("User: ", command)

        if 'what is' in command:
            object = command.replace('what is', '')
            info = wikipedia.summary(object, 1)
            speak(info)
        elif 'open' in command:
            if command == "open youtube":
                webbrowser.open("youtube.com")
            elif command == "open google":
                webbrowser.open("google.com")
            elif command == "open facebook":
                webbrowser.open("facebook.com")
            elif command == "open stack overflow":
                webbrowser.open("stackoverflow.com")
            elif command == "open gmail" or command == "open mail":
                webbrowser.open("mail.google.com")
            elif command == "open spotify":
                webbrowser.open("spotify.com")
            elif command == "open amazon":
                webbrowser.open("amazon.in")
            elif command == "open chess":
                webbrowser.open("chess.com")
            else:
                search = command.replace('open', '')
                pywhatkit.search(search)
            break
        elif 'google' in command:
            searchKey = command.replace('google', '')
            pywhatkit.search(searchKey)
            break
        # elif command == "play music" or command == "play some music":
        #     music_dir = '<//music-directory//>'
        #     songs = os.listdir(music_dir)
        #     os.startfile(os.path.join(music_dir, songs[0]))
        #     break
        elif 'play ' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            break
        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is ", strTime)
        elif command == "open code":
            codePath = "C:\\Users\\INTEL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            break
        elif 'joke' in command:
            speak(pyjokes.get_joke())
        # some fun conversations
        elif 'bye' in command:
            speak("Thank you for using me")
            exit()
        elif 'how are you' in command:
            speak("I am fine. Hope you are doing well too. Thank you for asking")
        elif 'are you doing' in command:
            speak("nothing much. trying to help you a little bit")
        elif command == 'hi' or command == 'hello':
            speak("hello there. I am Violet. I am a tiny AI designed to help you")
        else:
            speak("Sorry I am not yet functioned to understand your command.")
            # pywhatkit.search(command)
            exit()
