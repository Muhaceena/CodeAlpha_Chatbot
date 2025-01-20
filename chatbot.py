import nltk
import random
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What’s on your mind?", "Hey! How can I assist you?"]
    ],
    [
        r"how are you(.*)?",
        ["I'm doing great! How about you?", "I'm great, thank you! How are you?"]
    ],
    [
        r"can you suggest me one anime to watch now(.*)?",
        [
            "Sure! How about 'Demon Slayer' for a mind-bending experience?",
            "I recommend 'One Piece'—a true classic.",
            "You might enjoy 'Attack on Titan' if you like action!",
        ]
    ],
    [
        r"what is your name(.*)?",
        ["I’m Nikhee, a ChatBot, your friendly assistant.", "You can call me Nikhee!"]
    ],
    [
        r"i need help with (.*)",
        ["I’d love to help you. Can you tell me more?"]
    ],
    [
        r"(.*) motivation (.*)|(.*) motivate (.*)",
        ["Yeah sure, Every expert was once a beginner. Every champion was once a contender. What sets them apart is their refusal to give up.So,don't worry, just don't give up, you can acheive heights."]
    ],
    [
        r"(.*) favorite food(.*)?",
        ["I don’t eat, but I’ve heard pizza is a universal favorite!", "I think I would like ice-cream", "I don't eat but I would like to eat Biriyani!"]
    ],
    [
        r"bye|quit|exit",
        ["Goodbye! Have a wonderful day!", "Bye! Feel free to chat anytime.", "Take care! See you soon."]
    ],
    [
        r"(.*)",
        [
            "I'm not sure I understand that. Could you elaborate?",
            "Sorry, I’d need more information to help you with that.",
        ]
    ],
]
chatbot = Chat(pairs, reflections)
def chatbot_conversation():
    """
    Start a conversation with the chatbot.
    """
    print("ChatBot: Hello! I am your smart assistant. Type 'quit' or 'exit' to end the chat.\n")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["quit", "exit", "bye"]:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        if response:
            print(f"ChatBot: {response}\n")
        else:
            print("ChatBot: Sorry, I didn’t quite catch that. Could you rephrase?\n")
if __name__ == "__main__":
    chatbot_conversation()
