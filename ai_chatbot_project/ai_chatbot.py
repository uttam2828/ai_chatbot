from openai import OpenAI

# Paste your API key here
client = OpenAI(api_key="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")

def ai_chat():
    print("🤖 AI Bot Ready! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Bot: Goodbye 👋")
            break

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        reply = response.choices[0].message.content
        print("Bot:", reply)

ai_chat()
