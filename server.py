from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route('/emotion')
def sent_emotion():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # analyse the test using emotion detector function
    result = emotion_detector(text_to_analyze)
    return result

@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4001)