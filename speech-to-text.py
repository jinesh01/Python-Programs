import speech_recognization as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("SPEAK....")
    audio = r.listen(source)
print(r.recognize.google(audio))
