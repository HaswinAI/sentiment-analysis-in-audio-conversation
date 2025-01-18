from flask import Blueprint, request, jsonify, render_template
import speech_recognition as sr
from textblob import TextBlob
import pyttsx3
import pandas as pd
from datetime import datetime

conversation_bp = Blueprint('conversation', __name__)

log_file = "conversation_log.xlsx"  # Define log file location

def analyze_sentiment_and_respond(text):
    """
    Analyze sentiment of the given text and generate a response.
    """
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0.1:
        sentiment = "positive 😊"
        details = "The sentiment is positive, indicating a good mood."
    elif sentiment_score < -0.1:
        sentiment = "negative 😔"
        details = "The sentiment is negative, indicating dissatisfaction."
    else:
        sentiment = "neutral 😐"
        details = "The sentiment is neutral, indicating no strong opinions."

    response_text = f"Sentiment is {sentiment}. {details}"
    return response_text, sentiment

def save_conversation(user_input, response_text, sentiment):
    """
    Save conversation logs to an Excel file.
    """
    conversation_data = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'user_input': user_input,
        'response_text': response_text,
        'sentiment': sentiment
    }
    
    # Load existing Excel file if exists, otherwise create a new one
    try:
        df = pd.read_excel(log_file)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['timestamp', 'user_input', 'response_text', 'sentiment'])

    # Create a new DataFrame for the new conversation entry
    new_data = pd.DataFrame([conversation_data])

    # Concatenate the new data with the existing DataFrame
    df = pd.concat([df, new_data], ignore_index=True)

    # Save the updated DataFrame to Excel
    df.to_excel(log_file, index=False)

def speak_text(text):
    """
    Convert the given text to speech using pyttsx3.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

@conversation_bp.route("/")
def index():
    """
    Render the home page.
    """
    return render_template("conversation.html")

@conversation_bp.route("/start_conversation", methods=["POST"])
def start_conversation():
    """
    Start the conversation and speak 'Hello, audio is listening.'
    """
    speak_text("Hello, audio is listening. Let me know your reviews.")
    return jsonify({"response": "Hello, audio is listening."})

@conversation_bp.route("/listen", methods=["POST"])
def listen():
    """
    Capture audio, process it for sentiment, and respond with audio.
    """
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening for audio...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

        # Transcribe the audio to text
        transcribed_text = recognizer.recognize_google(audio)
        print(f"User said: {transcribed_text}")

        # Check for termination keyword
        if "stop" in transcribed_text.lower():
            response_text = "Conversation terminated. Goodbye!"
            speak_text(response_text)
            return jsonify({"end": True, "response": response_text, "user_input": transcribed_text})

        # Perform sentiment analysis and generate a response
        response_text, sentiment = analyze_sentiment_and_respond(transcribed_text)
        print(f"Response: {response_text}")

        # Save conversation to log file
        save_conversation(transcribed_text, response_text, sentiment)

        # Speak the response (only the output, not the user input)
        speak_text(response_text)

        # After each response, say "Audio is listening" to indicate it's ready for the next input
        speak_text("Audio is listening")

        return jsonify({"end": False, "response": response_text, "sentiment": sentiment, "user_input": transcribed_text})

    except sr.UnknownValueError:
        error_message = "Could not understand the audio. Please try again."
        speak_text(error_message)  # Speak the error message
        speak_text("Audio is listening")  # Indicate it's ready for the next input
        return jsonify({"end": False, "response": error_message, "user_input": ""})

    except sr.RequestError as e:
        error_message = f"Speech Recognition API error: {str(e)}"
        speak_text(error_message)
        speak_text("Audio is listening")
        return jsonify({"end": False, "response": error_message, "user_input": ""})

    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        speak_text(error_message)
        speak_text("Audio is listening")
        return jsonify({"end": False, "response": error_message, "user_input": ""})