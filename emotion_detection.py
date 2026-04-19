"""
Author: Vishal Ashok Hegde
Function to perform Sentiment Analysis using Watson-nlp library
"""
import requests
import json

def emotion_detector(text_to_analyse: str):
    """
    Function to analyse the text input and predict the emotion of the text
    Emotions Categorized into :
    :1. Joy
    :2. Sadness
    :3. Anger 
    and so on
    """
    
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)

    emotion_predictions = formatted_response.get('emotionPredictions', [])
    if emotion_predictions:
        prediction = emotion_predictions[0]
    
        if response.status_code == 200:
            emotion_scores = {
                'anger': prediction['emotion']['anger'],
                'disgust': prediction['emotion']['disgust'],
                'fear': prediction['emotion']['fear'],
                'joy': prediction['emotion']['joy'],
                'sadness': prediction['emotion']['sadness']
            }

            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            emotion_scores['dominant_emotion'] = dominant_emotion

        elif response.status_code == 400 or response.status_code == 500:
            emotion_scores = {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
            
    else:
        emotion_scores = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return emotion_scores

import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends text to the Watson NLP service, extracts emotion scores,
    and determines the dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"NOTEBOOK_ID": "Your_Notebook_ID"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send the request to Watson NLP
    response = requests.post(url, json=myobj, headers=header)
    
    # Task 3: Convert the response into a dictionary using the json library
    formatted_response = json.loads(response.text)
    
    # Extract the emotion scores
    # Structure: ['emotionPredictions'][0]['emotion']
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Separate scores for ease of calculation
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Determine the dominant emotion (key with the highest value)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Create the output dictionary in the required format
    output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return output
