import io
import os

# Import the Google Cloud client library
from google.cloud import speech_v1p1beta1 as speech

# Set the path to your audio file
audio_file = 'path/to/your/audio/file.wav'

# Create a Speech-to-Text client
client = speech.SpeechClient()

# Set the audio configuration
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US',
    enable_speaker_diarization=True,
    diarization_speaker_count=5,
)

# Load the audio file into memory
with io.open(audio_file, 'rb') as f:
    content = f.read()

# Send the audio file to the Speech-to-Text API for transcription
audio = speech.RecognitionAudio(content=content)
response = client.recognize(config=config, audio=audio)

# Print the transcript and speaker labels
for result in response.results:
    for alternative in result.alternatives:
        print('Transcript: {}'.format(alternative.transcript))
        if alternative.words:
            for word in alternative.words:
                if word.speaker_tag != 0:
                    print('Speaker {}: {}'.format(word.speaker_tag, word.word))
