import pyttsx3

while True:
    engine = pyttsx3.init()
    text = input("Enter the text you want to convert into speech: ")
    if text=="q":
        break
    engine.say(text)
    engine.runAndWait()