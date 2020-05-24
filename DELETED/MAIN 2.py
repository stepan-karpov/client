import speech_recognition as sr
import pyttsx3
from TextPreparation import *
import pyautogui as p
import time

def speak(Text):
    Text = Text.lower()
    speak_engine = pyttsx3.init()
    CNG = {"(wa)": "", "raspberry": "rasbery", "/": "делить на", "*": "умножить на", "-alpha": "Альфа",
           "red": "красный", "white": "Белый", "gray": "Серый", "black": "чёрный", "orange": "оранжевый",
           "green": "зелёный", "yellow": "жёлтый", "aqua": "аква",
           "WolframAlpha Error": "Похоже, вольфрам альфа не может обработать запрос", "windows": "виндовс"
           }
    for k, v in CNG.items():
        Text = Text.replace(k, v).strip()
    speak_engine.say(Text)
    speak_engine.runAndWait()
    speak_engine.stop()


def Main():
    try:
        with m as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        result = r.recognize_google(audio, language="ru-RU")
        request = result.capitalize()
        request = PrepareAnswer(request)
        return result, request
    except sr.UnknownValueError:
        return "", ""

def WriteDialog(result, request):
    ds = open("FILES/DialogStory.txt", mode='a')
    ds.write(result + "\n")
    ds.write(request + "\n")
    ds.write("\n")
    ds.close()

if __name__ == "__main__":
    r = sr.Recognizer()
    m = sr.Microphone(device_index=1)
    speak_engine = pyttsx3.init('sapi5')

    while 1:
        p.hotkey("ctrl", "s")
        f = open('Listen.txt', mode='r', encoding='utf-8')
        content = f.read()
        if content != "":
            content = content.strip(' ')
            answer = PrepareAnswer(content)

            WriteDialog(content.capitalize(), answer)
            speak(answer)
            print(content)
            print(answer)
        f.close()
        p.hotkey("ctrl", 'a')
        p.hotkey('del')
        p.keyUp
        time.sleep(.9)
