
#download PyAudio and SpeechRecognition
#grouip 7 180DA
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('listening ... ',end='',flush=True)
    audio = r.listen(source)
    print('done listening')
try:
    print("google recognizes:\n" + r.recognize_google(audio))
except sr.UnknownValueError:
    print("google unknown value error")
except sr.RequestError as e:
    print(f'error: {e}')
