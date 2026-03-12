from app.config import SYSTEM_PROMPT, EXIT_PHRASES, conversation_history
from app.llm import get_llm_response
from app.text_to_speech import text_to_speech


def run_voice_bot():
    """
    Main conversation loop
    """

    global conversation_history

    conversation_history.clear()

    conversation_history.append({
        "role": "system",
        "content": SYSTEM_PROMPT
    })

    print("=" * 50)
    print("🤖 AI Voice Bot Ready")
    print("Type exit/quit to stop")
    print("=" * 50)

    greeting = "Hello! I'm your AI assistant. How can I help you today?"

    print(f"Bot: {greeting}")

    text_to_speech(greeting)

    while True:

        try:

            user_text = input("You: ")

            if not user_text:
                print("⚠ No input detected")
                continue

            if any(x in user_text.lower() for x in EXIT_PHRASES):

                farewell = "Goodbye! Have a great day!"

                print(f"Bot: {farewell}")

                text_to_speech(farewell)

                break

            reply = get_llm_response(user_text)

            print(f"Bot: {reply}")

            text_to_speech(reply)

        except KeyboardInterrupt:

            print("Stopped")

            break
