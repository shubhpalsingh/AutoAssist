import json
import os
from modules.logger import log_interaction
from modules.voice_support import get_voice_input
from gui.chatbot_gui import start_gui

with open('car_bot_data.json', 'r', encoding='utf-8') as f:
    car_bot_data = json.load(f)

def get_response(user_msg):
    user_msg = user_msg.lower()
    for key, section in car_bot_data.items():
        patterns = section.get("patterns", [])
        for pattern in patterns:
            pattern_str = str(pattern).lower()  # Convert pattern to string
            if pattern_str in user_msg:
                responses = section.get("responses", [])
                if responses:
                    return responses[0]
    # Fallback response
    return car_bot_data.get("fallback", {}).get("responses", ["Sorry, I didn't understand."])[0]


def main():
    bot_data = car_bot_data()
    print("CarBot (type 'voice' for microphone input, 'exit' to quit):")

    while True:
        user_msg = input("You: ")
        if user_msg.strip().lower() == "exit":
            print("CarBot: Goodbye!")
            break
        elif user_msg.strip().lower() == "voice":
            user_msg = get_voice_input()
            if not user_msg:
                continue
        
        responses = get_response(user_msg, bot_data)
        response = responses[0]
        print(f"CarBot: {response}")
        log_interaction(user_msg, response)

if __name__ == "__main__":
    # Optionally, launch GUI instead of CLI
    # Uncomment the line below to use the GUI
    start_gui()
    #main()
