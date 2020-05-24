import requests

print('Beginning file download with requests')

words = "text_to_change"
print("WORDS: " + words)
url = 'http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=' + words.replace(" ", "+") + '&tl=en'
r = requests.get(url)

with open('/home/pi/client/FILES/audio_answers/' + words + ".mp3", 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
