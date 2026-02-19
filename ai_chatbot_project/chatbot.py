from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

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

        print("Bot:", response.choices[0].message.content)

ai_chat()
