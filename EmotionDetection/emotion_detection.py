import requests
import json

def emotion_detector(text_to_analyze):
    # If the input is blank, return None for all emotion scores
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    for _ in range(3):
        try:
            response = requests.post(url, json=myobj, headers=header)
            response.raise_for_status()
            
            # If the response is 400, return None for all emotions
            if response.status_code == 400:
                return {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
                }

            data = json.loads(response.text)
            emotions = data['emotionPredictions'][0]['emotion']

            anger = emotions.get('anger', 0)
            disgust = emotions.get('disgust', 0)
            fear = emotions.get('fear', 0)
            joy = emotions.get('joy', 0)
            sadness = emotions.get('sadness', 0)

            dominant_emotion = max(emotions, key=emotions.get)

            return {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': dominant_emotion
            }
        except requests.RequestException:
            pass

    raise ConnectionError("All retry attempts failed.")