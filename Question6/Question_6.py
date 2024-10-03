import nltk
from nltk.chat.util import Chat, reflections

# Pairs of input and corresponding responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How can I help you today?", ]
    ],
    [
        r"hi|hello|hey",
        ["Hello! How are you today?", ]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Sunita.", ]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How about you?", ]
    ],
    [
        r"(i am|i'm) (not good|sad|unhappy|upset|bad)",
        ["I'm sorry to hear that. Is there anything I can do to make you feel better?", ]
    ],
    [
        r"(i am|i'm) (good|happy|feeling amazing|feeling great|excited)",
        ["That's wonderful to hear! What made your day so great?", ]
    ],
    [
        r"remind me to (.*)",
        ["Sure! I will remind you to %1.", ]
    ],
    [
        r"bye|exit",
        ["Goodbye! Have a nice day.", ]
    ],
    # Add a default response for unrecognized inputs
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Could you rephrase?"]
    ],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
def start_chat():
    print("Chatbot: Hi there!")
    chatbot.converse()

# Run the chatbot
start_chat()
