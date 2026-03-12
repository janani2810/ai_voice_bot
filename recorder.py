import io
import numpy as np
import sounddevice as sd
import soundfile as sf

buffer = io.BytesIO()

def record_audio(duration=5, sample_rate=16000):
    """
    Record audio from microphone
    """

    print("🎙 Recording audio...")

    audio_data = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype=np.float32
    )

    sd.wait()

    print("Processing audio...")

    return audio_data, sample_rate


def save_audio(audio_data, sample_rate):
    """
    Save recorded audio into memory buffer
    """

    sf.write(buffer, audio_data, sample_rate, format="WAV")

    buffer.seek(0)

    buffer.name = "audio.wav"

    return buffer
