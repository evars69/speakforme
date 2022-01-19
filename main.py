import pyttsx3
friend = pyttsx3.init()
speech = input ("bolo bhai")
friend.say(speech)
friend.runAndWait()
