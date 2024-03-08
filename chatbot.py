import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    (
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi, how can I help you?"]
    ),
    (
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm good, thanks for asking.", "All good on this side!"]
    ),
    (
        r"What is your name ?",
        ["You can call me ChatBot.", "I'm ChatBot, nice to meet you!"]
    ),
    (
        r"quit|bye|goodbye",
        ["Goodbye!", "It was nice talking to you. Bye!", "See you later!"]
    ),
    (
        r"(.*) your name?",
        ["My name is ChatBot.", "I'm ChatBot, nice to meet you!"]
    ),
    (
        r"(.*) (age|old) ?",
        ["I'm just a program, I don't have an age.", "Age is just a number for me!"]
    ),
    (
        r"(.*) (created|made) you ?",
        ["I was created by a human programmer.", "I'm a product of programming."]
    ),
    (
        r"(.*) (location|city) ?",
        ["I exist in the digital realm, no physical location for me.", "I'm everywhere and nowhere."]
    ),
    (
        r"how (.*) health(.*)",
        ["I'm just a chatbot, so I don't have health concerns like humans do."]
    ),
    (
        r"(.*) (weather|temperature) ?",
        ["I'm sorry, I can't provide weather updates at the moment."]
    ),
    (
        r"(.*)",
        ["Sorry, I didn't understand that.", "Could you please rephrase that?", "I'm not sure I follow."]
    )
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hello! I'm ChatBot. How can I assist you today?")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("ChatBot:", response)
    if user_input.lower() in ["quit", "bye", "goodbye"]:
        break
