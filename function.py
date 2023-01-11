from deepgram import Deepgram

import json
import requests
import deepl
import wave 
import pydub
from pydub import AudioSegment
import io
import base64 



#Clés API
deepgram = Deepgram("72d4a1c3292e4ff6273104e6047ea5cb38dfc691") 
translator = deepl.Translator("b37c4b9a-b2c4-677a-56f6-f1d2d0069cfb:fx")
api_key_eden_ai="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMGE0MWI1MGMtMzZjYS00NDIyLWExY2EtOWFhZDU0OTQ2ZTU4IiwidHlwZSI6ImFwaV90b2tlbiJ9.JOZLa3bEgoMcF2uj19DjZBzaFPjS9py5oBdch_dWD5o"

url = "https://api.edenai.run/v2/audio/text_to_speech"

#Fonction qui transcript un audio à du text 
# 
def Transcript_Audio_To_Text(path,language):

     # Open the audio file
    with open(path, 'rb') as audio:
        # ...or replace mimetype as appropriate
        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        response = deepgram.transcription.sync_prerecorded(source, {'punctuate': True,'language': language})
        
        return response["results"]["channels"][0]['alternatives'][0]['transcript']



#Fonction qui traduit du text en un language X

def TranslateText(text,language):
      
    result = translator.translate_text(text, target_lang=language) 
   
    return  result.text
    
#Fonction qui transcripte du text à un audio en utilisant la voix Google ou IBM

def TextTovoice(text,language):
    payload = {
    "response_as_dict": True,
    "attributes_as_list": False,
    "show_original_response": False,
    "providers": "google,ibm",
    "language": language,
    "text": text,
    "option": "FEMALE"
    }
    
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMGE0MWI1MGMtMzZjYS00NDIyLWExY2EtOWFhZDU0OTQ2ZTU4IiwidHlwZSI6ImFwaV90b2tlbiJ9.JOZLa3bEgoMcF2uj19DjZBzaFPjS9py5oBdch_dWD5o"}
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    
    return result['google']['audio']

#Fonction qui enregistre l'audio en output Mp3
def SaveAudio(audio,path):
    decoded_data=base64.b64decode(audio)
    with io.open("T"+path,"wb") as f:
        f.write(decoded_data)

#Fonction qui effectue toute la tache demandé 
def AllTheprocess(path,languageS,language):
    text=Transcript_Audio_To_Text(path,languageS) 
    print("Le text original de l'audio en input :")
    print(text)
    textT= TranslateText(text,language)
    print("Le text traduit à la langue "+language )
    print(textT)
    
    SaveAudio(TextTovoice(textT,language),path)    

    print("l'AUDIO EST ENREGISTRÉ EN OUTPUT SOUS LE NOM "+"T"+path)   