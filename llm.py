from app.config import client, conversation_history


def get_llm_response(user_text):
    """
    Send text to LLM and get response
    """

    messages = list(conversation_history)

    messages.append({
        "role": "user",
        "content": user_text
    })

    response = client.chat.completions(
        model="sarvam-m",
        messages=messages
    )

    assistant_text = response.choices[0].message.content

    conversation_history.append({
        "role": "user",
        "content": user_text
    })

    conversation_history.append({
        "role": "assistant",
        "content": assistant_text
    })

    return assistant_text
