AutoAssist: Smart Car Suggestion Chatbot (Flask Web App)
AutoAssist is an interactive web-based chatbot that helps users get car recommendations, information about car types, brands, and features, and answers to common automotive questions. It supports both text and voice input (microphone), has a modern themeable UI (light/dark), and logs all chats.

Features:
-Conversational chat about car models, suggestions, and car-related topics
-Voice input (microphone support via browser)
-Light/Dark theme toggle for comfortable chatting
-Full-screen, responsive UI for desktop and mobile
-Chat logs saved in logs/chat_history.txt
-Easy customization using car_bot_data.json

Project Structure:
AutoAssist/
│

├ app.py # Flask backend server

├ car_bot_data.json # Chat training data/rules

├ logs/

│ └ chat_history.txt # Conversation history, created automatically

├ modules/

│ └ logger.py # Logger for chat history (used by Flask)

├ templates/

│ └ index.html # Front-end UI (HTML, CSS, JS)

└ README.txt # Project documentation

Setup & Installation:
-Clone or download this repository.
-Install Python dependencies:
pip install flask
-(Optional) Check/Install other packages.
Most features use basic Python and browser APIs. Voice input works best in Google Chrome.
-Running the Application:
-Ensure your structure matches the “Project Structure” above.
-Start the Flask server:
python app.py

-Open your browser and navigate to:
http://127.0.0.1:5000/

Using the Web Chat:
-Type messages, use the mic button, or switch theme in your browser!

Notes on Voice Input:
-Voice recognition is provided by the browser (Web Speech API).
-Best supported in Google Chrome desktop.
-Grant microphone access when prompted.

Customization:
-Edit car_bot_data.json to add or change bot behaviors, car database, or responses.
-Change UI: Edit templates/index.html (HTML/CSS/JS).
-Modify logging: See modules/logger.py.

Example Questions to Try:
-What are the best cars for city driving?
-Tell me about electric cars.
-Which car has the best mileage?
-Recommend a budget car.
-Show me popular car brands.

Troubleshooting:
-No mic access? Use Chrome and allow mic permissions.
-Chat not loading? Make sure app.py is running and no firewall/antivirus is blocking localhost.
-No logs? Ensure the logs/ folder exists or check file permissions.

Credits & License:
-Built with Flask, HTML, CSS, and JavaScript.
-Inspired by user needs for easy car selection chatbots.
-You may modify, deploy, and share; please credit if redistributing.

-Enjoy car chatting with AutoAssist!
