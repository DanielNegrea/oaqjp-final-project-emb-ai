"""
Flask server app for emotion detection
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def emotion_analyzer():
    """Returns emotion detection result"""
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Error handling
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    formatted_response = "For the given statement, the system response is "

    for emotion in response:
        formatted_response += "\'" + emotion + "\': " + str(response[emotion]) + ", "

    return formatted_response

@app.route("/")
def render_index_page():
    """Returns html for default index page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
