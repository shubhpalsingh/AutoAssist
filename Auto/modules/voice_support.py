import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("Listening... (speak now)")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You (voice): {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not catch that. Please repeat.")
        return None
    except sr.RequestError:
        print("Could not access the speech recognition service.")
        return None
