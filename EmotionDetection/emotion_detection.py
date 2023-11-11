import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers=header)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = response.json()

    # Extracting emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
  
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    max_emotion = max(emotions, key=emotions.get)

    formated_dict_emotions = {
                            'anger': anger_score,
                            'disgust': disgust_score,
                            'fear': fear_score,
                            'joy': joy_score,
                            'sadness': sadness_score,
                            'dominant_emotion': max_emotion
                            }
    return formated_dict_emotions