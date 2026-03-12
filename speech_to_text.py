from app.config import client

def speech_to_text(audio_buffer):
    """
    Convert speech audio into text
    """

    response = client.speech_to_text.transcribe(
        file=audio_buffer,
        language_code="en-IN"
    )

    text = response.text.strip()

    print(f"You: {text}")

    return text
