from groq import Groq

client = Groq(api_key="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")

def chat():
    print("🤖 Free AI Bot Ready! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Bot: Goodbye 👋")
            break

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": user_input}]
        )

        print("Bot:", response.choices[0].message.content)

chat()
