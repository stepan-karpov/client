import pyaudio
import speech_recognition as sr
import subprocess
from text_preparation import prepare_answer, write_request
import math
import struct
import wave
import time
import os
from datetime import datetime

Threshold = 10

SHORT_NORMALIZE = (1.0/32768.0)
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2

TIMEOUT_LENGTH = .3

f_name_directory = r'FILES/audio/'

class Recorder:

    @staticmethod
    def rms(frame):
        count = len(frame) / swidth
        format = "%dh" % (count)
        shorts = struct.unpack(format, frame)

        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE
            sum_squares += n * n
        rms = math.pow(sum_squares / count, 0.5)

        return rms * 1000

    def recognize(self):
        r = sr.Recognizer()

        hellow=sr.AudioFile(self.filename)
        start_time = datetime.now()
        with hellow as source:
            audio = r.record(source)
        try:
            s = r.recognize_google(audio)
            print("[ log ] recognition time: " + str(datetime.now() - start_time))
            return (s)
        except Exception as e:
            return ""



    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=chunk)

    def record(self):
        print('Noise detected, recording beginning')
        rec = []
        current = time.time()
        end = time.time() + TIMEOUT_LENGTH

        while current <= end:

            data = self.stream.read(chunk)
            if self.rms(data) >= Threshold: end = time.time() + TIMEOUT_LENGTH

            current = time.time()
            rec.append(data)
        self.write(b''.join(rec))

        self.request = self.recognize()
        return self.request



    def write(self, recording):
#        print(recording)
        n_files = len(os.listdir(f_name_directory))

        self.filename = os.path.join(f_name_directory, '{}.wav'.format(n_files))

        print(self.filename)
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(recording)
        wf.close()
        print('Written to file: {}'.format(self.filename))
        print('Returning to listening')



    def listen(self):
#        print('Listening beginning')
        input = self.stream.read(chunk)
        rms_val = self.rms(input)
        if rms_val > Threshold:
            return self.record()

def speak(text):
    start_time = datetime.now()
    text = text.replace("(", "\(").replace(")", "\)").replace("'", "").lower()
#   print(dir FILES/audio_answers/)
    dir = subprocess.check_output("ls FILES/audio_answers/", shell=True).decode("utf-8").split('\n')
    if not dir.count(text + ".mp3") == 1:
        print("[ log ] should be downloaded")
        print("[ log ] speak time: " + str(datetime.now() - start_time))
        os.system('./speech.sh ' + text)
        file = open(r"FILES/to_write.txt", mode="a")
        if open(r"FILES/to_write.txt").read().find(text) == -1:
            file.write(text + "\n")
        file.close()
#        os.system("./download_file.sh " + Text)
#        print("downloading complete")
#       print("not")
    else:
        print("[ log ] file already exists")
        print("[ log ] speak time: " + str(datetime.now() - start_time))
        os.system("omxplayer FILES/audio_answers/" + text.replace(" ", "\ ") + ".mp3")


a = Recorder()
while True:
    request = str(a.listen()).lower()

    if request != "none" and request != "":
        print("Recognized: " + request)
        start_time = datetime.now()
        try:
            answer = prepare_answer(request)
#            answer = "this is answer"
            write_request(request, answer)
        except:
            answer = "error with text preparation module"
        print("[ log ] text preparation time: " + str(datetime.now() - start_time))
        print("Request: " + request)
        print("Answer: " + answer)
        if answer == "goodbye":
            os.system("./speech.sh bye")
            exit()
        if answer != "":
            speak(answer)



