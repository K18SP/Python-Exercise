import pyttsx3

names = ["satyen", "satyen","Kushal"]

engine = pyttsx3.init()

for name in names:
    engine.say(f"{name} is very intelligent")

engine.runAndWait()