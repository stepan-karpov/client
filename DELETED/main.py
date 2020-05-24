# -*- coding: utf-8 -*-
import os
import subprocess
import requests
import speech_recognition as sr
from text_preparation import prepare_answer, write_request


"""

hello, anybody!
You're looking on VoiceHelper code written by me
It's easy to start in from this point IF YOU HAVE ALL PACKAGES INTALLED
Warning: this code is working only under Linux, running from Windows can cause some problems (for example, with music)

"""

def speak(Text):
    Text = Text.replace("(", "\(").replace(")", "\)").replace("'", "").lower()
#    print(dir FILES/audio_answers/)
    dir = subprocess.check_output("ls FILES/audio_answers/", shell=True).decode("utf-8")
#    print(dir)
    if not Text in dir:
        print("should be downloaded")
        os.system('./speech.sh ' + Text)
        os.system("./download_file.sh " + Text)
        print("downloading complete")
 #       print("not")
    else:
        print("file already exists")
        try:
            os.system("omxplayer FILES/audio_answers/" + Text.replace(" ", "\ ") + ".mp3")
        except:
           os.system('./speech.sh ' + Text)
           os.system("./download_file.sh " + Text)

r = sr.Recognizer()
speech = sr.Microphone(device_index=2)

if __name__ == "__main__":
    request = "doesn't matter what text is here :)"
    speak("i am ready to work")
    #os.system("./speech.sh I am ready to work")
    while request != "stop":
        with speech as source:
            print("say something!…")
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            request = r.recognize_google(audio, language = 'en-US')
            print("request: " + request)
            try:
                answer = prepare_answer(request)
                print("answer: " + answer)
                write_request(request, answer)
            except:
                answer = "Error with text preparation module"
            #answer = "This is redefinition of answer varible to check text synthesis"
            if answer == "goodbye":
                os.system("./speech.sh bye")
                exit()
                break
            speak(answer)

        except:
            pass


