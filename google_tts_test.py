import os
from dotenv import load_dotenv
from google.cloud import texttospeech

load_dotenv()

API_KEY = os.environ.get('API_KEY')
PROJECT_ID = os.environ.get('PROJECT_ID')

client = texttospeech.TextToSpeechClient(
    client_options={"api_key": API_KEY, "quota_project_id": PROJECT_ID}
)

input_text = texttospeech.SynthesisInput(text="Testing google text to speech for the Derpies personal assistant project. Derp derp!")

# Note: the voice can also be specified by name.
# Names of voices can be retrieved with client.list_voices().
voice = texttospeech.VoiceSelectionParams(
    # language_code="es-US",
    # name="es-US-Studio-B",
    # language_code="en-AU",
    # name="en-AU-Standard-D",
    language_code="en-IN",
    name="en-IN-Standard-C",
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16,
    speaking_rate=1
)

response = client.synthesize_speech(
    request={"input": input_text, "voice": voice, "audio_config": audio_config}
)

# The response's audio_content is binary.
with open("./output3.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

print('OK')