import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    myobj = { "raw_document": { "text": text_to_analyze } }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Error handling
    if response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, 
        "joy": None, "sadness": None, "dominant_emotion": None}

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    emotion_scores = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }

    # Find the dominant emotion
    dominant_emotion = max(emotion_scores, key=lambda emotion: emotion_scores[emotion])

    # Add dominant emotion to dictionary
    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores