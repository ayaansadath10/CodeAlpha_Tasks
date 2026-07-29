
import random

# Predefined replies for known inputs (some have multiple options for variety)
RESPONSES = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "hi": ["Hi there!", "Hello!"],
    "how are you": ["I'm fine, thanks! How about you?", "Doing great, thanks for asking!"],
    "what is your name": ["I'm a simple chatbot built with Python.", "You can call me PyBot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care."],
    "thanks": ["You're welcome!", "No problem!"],
    "thank you": ["You're welcome!", "Anytime!"],
}

DEFAULT_RESPONSES = [
    "Sorry, I don't understand that. Can you rephrase?",
    "I'm not sure what you mean.",
    "Can you say that in a different way?",
]


def get_response(user_input):
    """Match user input against known phrases and return a reply."""
    user_input = user_input.lower().strip()

    # Remove basic punctuation for easier matching
    for punct in ["!", "?", "."]:
        user_input = user_input.replace(punct, "")

    for key in RESPONSES:
        if key in user_input:
            return random.choice(RESPONSES[key])

    return random.choice(DEFAULT_RESPONSES)


def chat():
    print("Chatbot: Hi! I'm PyBot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            print("Chatbot:", random.choice(RESPONSES["bye"]))
            break

        response = get_response(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    chat()