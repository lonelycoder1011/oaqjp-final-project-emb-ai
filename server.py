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
    and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    try:
        response = emotion_detector(text_to_analyze)
        
        # Extract emotion scores and the dominant emotion
        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = response['joy']
        sadness = response['sadness']
        dominant_emotion = response['dominant_emotion']

        # Check if the dominant emotion is None
        if dominant_emotion is None:
            return "Invalid text! Please try again."
        
        # Return a formatted string with the emotion scores and the dominant emotion
        return "For the given statement, the system response is: Anger: " + str(anger) + \
               ", Disgust: " + str(disgust) + \
               ", Fear: " + str(fear) + \
               ", Joy: " + str(joy) + \
               ", and Sadness: " + str(sadness) + \
               ". The dominant emotion is " + str(dominant_emotion) + "."
    
    except Exception as e:
        # Handle specific exception and return a message
        return f"An error occurred: {str(e)}"

@app.route("/")
def render_index_page():
    """
    Renders the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)