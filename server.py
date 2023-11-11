from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detection_endpoint():
    # Get the input text from the request
    text_to_analyze = request.args.get("textToAnalyze")

    # Use the emotion_detector function to get emotion predictions
    emotion_predictions = emotion_detector(text_to_analyze)

    dominant_emotion = emotion_predictions.get('dominant_emotion')

    if dominant_emotion is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    # Format the response
    response = {
        "anger": emotion_predictions['anger'],
        "disgust": emotion_predictions['disgust'],
        "fear": emotion_predictions['fear'],
        "joy": emotion_predictions['joy'],
        "sadness": emotion_predictions['sadness'],
        "dominant_emotion": dominant_emotion
    }

    # Display the response in the specified format
    output_message = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return jsonify(output_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
