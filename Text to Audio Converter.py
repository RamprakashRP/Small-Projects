from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'en'
sp = gTTS(text=input("Enter The Text You Want To Convert To Audio File :"), lang=language, slow=False)

sp.save(audio)
playsound(audio)
