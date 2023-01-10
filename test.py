from deepgram import Deepgram
import json

import deepl

deepgram = Deepgram("72d4a1c3292e4ff6273104e6047ea5cb38dfc691") 
translator = deepl.Translator("b37c4b9a-b2c4-677a-56f6-f1d2d0069cfb:fx")

def Transcript_Audio_To_Text(path):

     # Open the audio file
    with open(path, 'rb') as audio:
        # ...or replace mimetype as appropriate
        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        response = deepgram.transcription.sync_prerecorded(source, {'punctuate': True})
        
        return response["results"]["channels"][0]['alternatives'][0]['transcript']


def TranslateText(text,language):
    print(text)    
    result = translator.translate_text(text, target_lang=language) 
    return  result.text
    

__name__ == '__main__'

print(Transcript_Audio_To_Text("exem2.mp3"))
text=Transcript_Audio_To_Text("exem2.mp3")
print(TranslateText(text,"FR"))

