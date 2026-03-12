import base64
import numpy as np
import soundfile as sf

from app.config import client


def text_to_speech(text):
    """
    Convert text response into speech audio file
    """

    response = client.text_to_speech.convert(
        text=text,
        target_language_code="en-IN"
    )

    audio_base64 = response.audios[0]

    decoded_audio = base64.b64decode(audio_base64)

    audio_filename = "bot_response.wav"

    with sf.SoundFile(
        audio_filename,
        mode="w",
        samplerate=22050,
        channels=1,
        subtype="PCM_16"
    ) as file:

        file.write(np.frombuffer(decoded_audio, dtype=np.int16))

    print(f"🤖 Bot audio saved to {audio_filename}")
