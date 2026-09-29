heydef get_reply(message):
    message = message.lower().strip().strip("?!.")

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I'm ChatBot, a simple rule-based bot."
    elif message == "help":
        return "You can say: hello, how are you, what is your name, bye."
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I know."


def chat():
    print("ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("ChatBot:", reply)

        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    chat()
