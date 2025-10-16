from django.shortcuts import render
from .models import purpose
import speech_recognition as sr
import pyttsx3
import subprocess
import pywhatkit as pwk
import webbrowser
import urllib.parse
import datetime
import qrcode


# Create your views here.
def jarvis(request):
    command = ""   # for showing in template
    data = purpose.objects.all()

    if request.method == "POST":
        if request.POST.get("display"):
            return render(request, "index.html", {"data": data, "command": command})

        if request.POST.get("javis"):   # when image clicked
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            recognizer = sr.Recognizer()

        
        def cmd():
            with sr.Microphone() as source:
                print("your background noise is cleaning... please wait")
                recognizer.adjust_for_ambient_noise(source,duration=0.5)
                print("Speak anything...")
                audio=recognizer.listen(source)
                return audio
                
        try:
            audio=cmd()
            command=recognizer.recognize_google(audio,language="en-Us")
            command=command.lower()
            print("you said",command)
        except Exception as ex:
                print("error",ex)
                command=""

        if 'chrome' in command:
            engine.say("open the chrome")
            engine.runAndWait()
            webbrowser.open("https://www.chrome.com")

                

        elif "google" in command:
            engine.say("open the google")
            engine.runAndWait()
            webbrowser.open("https://www.google.com")

        elif "youtube" in command:
            engine.say("open the youtube")
            engine.runAndWait()
            webbrowser.open("http://www.youtube.com")
        elif "flipkart" in command:
            engine.say("open the flipkart")
            engine.runAndWait()
            webbrowser.open("https://www.flipkart.com")
        elif "amazon" in command:
                engine.say("ope the amazon")
                engine.runAndWait()
                webbrowser.open("https://www.amazon.in")
            
        elif "whatsapp" in command:
                engine.say("open the whatsapp")
                engine.runAndWait()
                webbrowser.open('https://web.whatsapp.com/')
        elif "zepto" in command:
                engine.say("open the zepto")
                engine.runAndWait()
                webbrowser.open("https://www.zepto.com")
        elif "instagram" in command:
                engine.say("open the instagram")
                engine.runAndWait()
                webbrowser.open("https://www.instagram.com")

        elif "facebook" in command:
                engine.say("open the facebook")
                engine.runAndWait()
                webbrowser.open("https://www.facebook.com")
            # elif "wikipedia" in command:
            #     engine.say("open the wikipedia")
            #     engine.runAndWait()
            #     webbrowser.open("https://en.wikipedia.org/wiki/Mahatma_Gandhi")
            #     webbrowser.open('https://en.wikipedia.org/wiki/mahabharata')
            #     webbrowser.open('https://en.wikipedia.org/wiki/ramayana')
            #     webbrowser.open('https://en.wikipidia.org/wiki/remeo_and_julliet')

        elif "wikipedia" in command:
            if "gandhi" in command:
                engine.say("open the  Mahatma Gandhi Wikipedia page")
                engine.runAndWait()
                webbrowser.open("https://en.wikipedia.org/wiki/Mahatma_Gandhi")

        elif "mahabharata" in command:
            engine.say("open the  Mahabharata Wikipedia page")
            engine.runAndWait()
            webbrowser.open("https://en.wikipedia.org/wiki/Mahabharata")

        elif "ramayana" in command:
            engine.say("open the  Ramayana Wikipedia page")
            engine.runAndWait()
            webbrowser.open("https://en.wikipedia.org/wiki/Ramayana")

        elif "romeo and juliet" in command:   # note: fixed spelling of wikipedia + romeo/juliet
            engine.say("open the  Romeo and Juliet Wikipedia page")
            engine.runAndWait()
            webbrowser.open("https://en.wikipedia.org/wiki/Romeo_and_Juliet")

        # else:
        #     engine.say("Which Wikipedia page should I open?")
        #     engine.runAndWait()


        elif "songs" in command:
            if "telugu" in command:
                engine.say("Opening Telugu songs" or "play the telugu songs")
            if "volume up" in command:
                engine.setProperty("volume",1.0)
            else:
                engine.setProperty("volume",0.5)
                engine.runAndWait()
                webbrowser.open("https://www.youtube.com/results?search_query=telugu+songs")    
                                

        elif "hindi" in command:
            engine.say("Opening Hindi songs" or "play the hindi songs")
            engine.runAndWait()
            webbrowser.open("https://www.youtube.com/results?search_query=hindi+songs")

        elif "english" in command:
            engine.say("Opening English songs" or "play the english  songs")
            engine.runAndWait()
            webbrowser.open("https://www.youtube.com/results?search_query=english+songs")

        elif "kannada" in command:
            engine.say("Opening kannada songs" or"play the kannada songs")
            engine.runAndWait()
            webbrowser.open("https://www.youtube.com/results?search_query=kannada+songs")
        elif "malayalam" in command:
            engine.say("Opening malayalam songs" or"play the malayalam songs")
            engine.runAndWait()
            webbrowser.open("https://www.youtube.com/results?search_query=malayalam+songs")
        elif "tamil" in command:
            engine.say("Opening tamil songs" or"play the tamil songs")
            engine.runAndWait()
            webbrowser.open("https://www.youtube.com/results?search_query=tamil+songs")

        elif "songs" in command:
            if "telugu" in command:
                engine.say("Opening Telugu songs" )
            if "volume up" in command:
                engine.setProperty("volume",1.0)
            else:
                engine.setProperty("volume",0.5)
                engine.runAndWait()
                webbrowser.open("https://www.youtube.com/results?search_query=telugu+songs")

                

        elif "redbus" in command:
            engine.say("open the redbus")
            engine.runAndWait()
            webbrowser.open("https://www.redbus.in")

        elif "abhibus" in command:
            engine.say("open the abhibus")
            engine.runAndWait()
            webbrowser.open("https://www.abhibus.com")

        elif "myntra" in command:
            engine.say("open the myntra")
            engine.runAndWait()
            webbrowser.open("https://www.myntra.com")

        elif "bookmyshow" in command:
            engine.say("open the bookmyshow")
            engine.runAndWait()
            webbrowser.open("https://in.bookmyshow.com")

        elif "telegram" in command:
            engine.say("open the telegram")
            engine.runAndWait()
            webbrowser.open("https://web.telegram.org")

        elif "gmail" in command:
            engine.say("open the gmail")
            engine.runAndWait()
            webbrowser.open("https://mail.google.com/mail/u/0/inbox")

        elif "snapchat" in command:
            engine.say("open the snapchat")
            engine.runAndWait()
            webbrowser.open("https://www.snapchat.com/l/en-gb/")
        elif "twitter" in command:
            engine.say("open the twitter")
            engine.runAndWait()
            webbrowser.open("https://twitter.com/i/flow/login")

        elif "linkedin" in command:
            engine.say("open the linkedin")
            engine.runAndWait()
            webbrowser.open("https://www.linkedin.com/login")
        elif "naukri" in command:
            engine.say("open the naukri")
            engine.runAndWait()
            webbrowser.open("https://www.naukri.com")


        elif "chargpt" in command:
            engine.say("Open the ChatGPT")
            engine.runAndWait()
            chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open("https://chat.openai.com/")


        elif "rapido" in command:
            engine.say("open the rapido")
            engine.runAndWait()
            webbrowser.open("https://www.rapido.bike/")
        elif "where is my train" in command:
            engine.say("open the whereismytrain")
            engine.runAndWait()
            webbrowser.open("https://whereismytrain.in/")

        elif "accenture" in command:
            engine.say("open the accenture")
            engine.runAndWait()
            webbrowser.open("https://www.accenture.com/in-en")

        elif "swiggy" in command:
            engine.say("open the swiggy")
            engine.runAndWait()
            webbrowser.open("https://www.swiggy.com/")

        elif "zomato" in command:
            engine.say("open the zomato")
            engine.runAndWait()
            webbrowser.open("https://www.zomato.com/")
        elif "map" in command or "maps" in command:
            engine.say("Open the Maps")
            engine.runAndWait()
            webbrowser.open("https://www.google.com/maps")
        elif 'time' in command:
            engine.say("tell me time" or "how much time")
            engine.runAndWait()
            current_time = datetime.datetime.now().strftime("%I:%M %p")  # Example: 09:45 PM
            print(current_time)
            engine.say(f"The time is {current_time}")
            engine.runAndWait()
        elif "live location" in command:
            engine.say("Open the live location")
            engine.runAndWait()
            latitude = 17.3850
            longitude = 78.4867
            url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
            webbrowser.open(url)





        command = ""   # example

        if "volume up" in command:
            engine.setProperty("volume", 1.0)
            engine.say("Volume increased")
            engine.runAndWait()

        elif "volume down" in command:
            engine.setProperty("volume", 0.3)
            engine.say("Volume decreased")
            engine.runAndWait()

        elif "play" in command and "movie songs" in command:
            movie = command.replace("play", "").replace("movie songs", "").strip()
            if movie:
                engine.say(f"Play the  {movie} songs")
                engine.runAndWait()
                pwk.playonyt(movie + " movie songs")   # plays directly
            else:
                engine.say("Which movie songs do you want me to play?")
                engine.runAndWait()
                webbrowser.open("{movie},http://www.youtube.com")

        elif "scanner" in command:
            engine.say("open the scanner")
            engine.runAndWait()
            qr=qrcode.make("open the qrccode")
            qr.save("uday.png")
            qr.show()
            


                

    return render(request, "index.html", {"data": data, "command": command})






            
