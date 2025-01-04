"""
Emotion detection server for analyzing emotions in text using an emotion detector.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Analyzes the emotions in the provided text and returns the emotion scores
    and dominant emotion.9.62
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid input! Please provide text to analyze."

    try:
        response = emotion_detector(text_to_analyze)

        # Extract emotion scores and the dominant emotion
        anger = response.get('anger', 0)
        disgust = response.get('disgust', 0)
        fear = response.get('fear', 0)
        joy = response.get('joy', 0)
        sadness = response.get('sadness', 0)
        dominant_emotion = response.get('dominant_emotion')

        # Check if the dominant emotion is None
        if dominant_emotion is None:
            return (
                "Unable to detect a dominant emotion. Please try with different text."
            )

        # Return a formatted string with the emotion scores and the dominant emotion
        return (
            f"For the given statement, the system response is: Anger: {anger}, "
            f"Disgust: {disgust}, Fear: {fear}, Joy: {joy}, and Sadness: {sadness}. "
            f"The dominant emotion is {dominant_emotion}."
        )

    except (KeyError, ValueError) as specific_error:
        return f"An error occurred: {specific_error}"
    except TimeoutError:
        return "The request to the emotion detection service timed out. Please try again later."

@app.route("/")
def render_index_page():
    """
    Renders the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
