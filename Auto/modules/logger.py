'''
import os
import datetime

LOG_PATH = os.path.join("logs", "chat_history.txt")

def log_interaction(user_msg, bot_response):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] User: {user_msg}\n")
        f.write(f"[{timestamp}] CarBot: {bot_response}\n\n")

'''
import os
import datetime

LOG_PATH = os.path.join("logs", "chat_history.txt")  # Adjust path if needed

def log_interaction(user_msg, bot_response):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] User: {user_msg}\n")
        f.write(f"[{timestamp}] CarBot: {bot_response}\n\n")
