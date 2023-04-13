from pyannote.audio.features import Pretrained
from pyannote.audio.pipeline import SpeakerDiarization
from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_wav('audio.wav')

# Initialize the speaker diarization pipeline
pretrained = Pretrained(validate_dir=False)
diarization = SpeakerDiarization(feature_extraction=pretrained)

# Transcribe the audio and get the speakers and their respective text
results = diarization({'audio': audio})
for speaker, segments in results['pyannote.speaker'].items():
    for segment in segments:
        start, end = segment.start, segment.end
        text = r.recognize_google(audio[start:end])
        print(f"Speaker {speaker}: {text}")
