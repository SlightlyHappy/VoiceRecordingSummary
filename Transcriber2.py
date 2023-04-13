import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Load the audio file
with sr.AudioFile('audio.wav') as source:
    audio = r.record(source)

# Use Google Speech Recognition to transcribe the audio
text = r.recognize_google(audio)

print(text)
