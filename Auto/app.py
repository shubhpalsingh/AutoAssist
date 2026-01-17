from flask import Flask, render_template, request, jsonify
import json
from modules.logger import log_interaction
import re

app = Flask(__name__)

# Load your bot data from JSON
with open('car_bot_data.json', 'r', encoding='utf-8') as f:
    car_bot_data = json.load(f)

# Function to generate response based on user message
def get_response(user_msg):
    user_msg = user_msg.lower()
    for key, section in car_bot_data.items():
        patterns = section.get("patterns", [])
        for pattern in patterns:
            pattern_str = str(pattern).lower()  # Convert pattern to string
            if re.search(rf"\b{re.escape(pattern)}\b", user_msg):
                responses = section.get("responses", [])
                if responses:
                    return responses[0]
    # Fallback response
    return car_bot_data.get("fallback", {}).get("responses", ["Sorry, I didn't understand."])[0]

# Route for displaying the web chat page
@app.route('/')
def home():
    return render_template('index.html')

# API route to handle chat messages
@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json['message']
    response = get_response(user_msg)
    log_interaction(user_msg, response) 
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
