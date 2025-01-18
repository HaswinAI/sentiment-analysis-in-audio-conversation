# sentiment-analysis-in-audio-conversation
This project is a conversational chatbot with sentiment analysis, featuring a user-friendly interface made using Flask. It allows users to engage in text-based and audio-based conversations, making interactions more convenient and intuitive. The application analyzes user inputs for sentiment and provides AI-generated responses, insights, and suggestions to enhance the experience.

# Features
Text and Audio Interaction: Users can communicate through text or audio input, ensuring accessibility and ease of use.
Sentiment Analysis: Real-time analysis of user input to detect positive, negative, or neutral sentiment with confidence levels.
AI-Powered Responses: Integrates with Groq API and LLaMA models to provide contextual and meaningful responses.
Suggestions for Improvement: Offers actionable suggestions based on sentiment and input analysis.
Conversation Logging: Saves interactions (user input, AI response, sentiment, etc.) into an Excel file for review or analysis.
Interactive Interface: A chat-like design inspired by WhatsApp for a familiar user experience.
# Technologies Used
Python: Core programming language.
Flask: Web framework for building the backend.
TextBlob: For sentiment analysis.
Pandas: To manage and save conversation logs in Excel.
Groq API: For generating AI responses.
HTML/CSS/JavaScript: Frontend technologies for creating the user interface.
dotenv: For managing environment variables securely.
Requests: For making API calls to external services.
# Installation and Setup
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/sentiment-analysis-in-audio-conversation.git
cd sentiment-analysis-in-audio-conversation
Set up a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables: Create a .env file in the root directory with the following:

makefile
Copy
Edit
GROQ_API_KEY=your_groq_api_key
GROQ_API_URL=your_groq_api_url
Run the application:

bash
Copy
Edit
python src/app.py
Access the application: Open your browser and navigate to http://127.0.0.1:5000/.

# How It Works
User Input:

Type or speak your input in the chat interface.
Audio input is transcribed into text.
Sentiment Analysis:

The app uses TextBlob to analyze the input and determine sentiment polarity.
Sentiment is categorized as Positive 😊, Negative 😔, or Neutral 😐 with a confidence percentage.
AI Response:

The app sends the input to the Groq API, which generates an AI response using the LLaMA model.
The response is displayed in the chat interface.
Suggestions:

Based on the sentiment, actionable suggestions are provided to guide the user or enhance their experience.
Conversation Logging:

All interactions are logged into an Excel file (conversation_log.xlsx) for future reference.
# Project Structure
bash
Copy
Edit
sentiment-analysis-in-audio-conversation/
│
├── src/
│   ├── app.py              # Flask application
│   ├── routes.py           # Routes for handling requests and responses
│   ├── templates/
│   │   └── conversation.html # Chat interface template
│   ├── static/
│       ├── css/
│       │   └── styles.css  # Styles for the chat interface
│       ├── js/
│           └── scripts.js  # JavaScript for dynamic interactions
│
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not included in the repo)
├── README.md               # Project documentation
└── conversation_log.xlsx   # Excel file for conversation logs (auto-generated)
# Dependencies
Python 3.8+
Flask
TextBlob
Pandas
Requests
dotenv
# Future Enhancements
Improved Audio Features: Support for real-time audio streaming and analysis.
Multilingual Support: Add sentiment analysis and responses for multiple languages.
Advanced Sentiment Analysis: Incorporate advanced libraries or models for more nuanced sentiment detection.
User Authentication: Allow users to save and retrieve their previous conversations.
# Contributions
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
