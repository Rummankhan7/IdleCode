import spacy
from datetime import datetime
from random import choice

nlp = spacy.load("en_core_web_sm")

chat_responses = {
    "greetings": ["Hey there!", "Hi! How can I assist you?", "Hello! Ready to chat?"],
    "farewell": ["See you later!", "Take care!", "Bye!"],
    "mood": ["I'm functioning perfectly!", "Feeling like code on a sunny server!"],
    "identity": ["I'm AlphaBoT, your chatbot assistant.", "You can call me AlphaBoT."],
    "support": ["I can answer your questions or tell you a joke!", "Just ask me something!"],
    "humor": [
        "Why did the developer go broke? Because they used up all their cache.",
        "Why dont robots panic? They,ve got nerves of steel!",
        "Debugging: where you fix one bug and get two more."
    ],
    "weather_info": ["I'm not connected to the internet, so I can't check the weather "],
    "current_time": [f"It's {datetime.now().strftime('%H:%M:%S')} right now."],
    "today_date": [f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."]
}

intent_map = {
    "greetings": ["hi", "hello", "hey"],
    "farewell": ["bye", "goodbye", "see you"],
    "mood": ["how are you", "what's up", "how's it going"],
    "identity": ["who are you", "your name", "what are you"],
    "support": ["help", "what can you do", "how can you help"],
    "humor": ["tell a joke", "make me laugh", "say something funny"],
    "weather_info": ["weather", "is it raining", "what's the weather"],
    "current_time": ["what is the time now", "current time", "show time"],
    "today_date": ["what is the date today", "today's date", "which day is today"]
}

print("AlphaBoT: Hey! I'm AlphaBoT, your friendly chatbot. Type 'bye' to exit the chat.")

while True:
    user_msg = input("You: ").strip().lower()
    processed_msg = nlp(user_msg)

    matched_intent = None

    for tag, trigger_list in intent_map.items():
        if any(trigger in user_msg for trigger in trigger_list):
            matched_intent = tag
            break

    if matched_intent:
        if matched_intent == "current_time":
            print("AlphaBoT:", f"It's {datetime.now().strftime('%H:%M:%S')}.")
        elif matched_intent == "today_date":
            print("AlphaBoT:", f"Today is {datetime.now().strftime('%A, %B %d, %Y')}.")
        else:
            print("AlphaBoT:", choice(chat_responses[matched_intent]))

        if matched_intent == "farewell":
            break
    else:
        print("AlphaBoT: I'm not sure I follow. Could you ask that differently?")
