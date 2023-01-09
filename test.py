from deepgram import Deepgram
import json
deepgram = Deepgram("72d4a1c3292e4ff6273104e6047ea5cb38dfc691") 

def Transcript_Audio_To_Text(path):

     # Open the audio file
    with open(path, 'rb') as audio:
        # ...or replace mimetype as appropriate
        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        response = deepgram.transcription.sync_prerecorded(source, {'punctuate': True})
        
        return response["results"]["channels"][0]['alternatives'][0]['transcript']
       
__name__ == '__main__'

print(Transcript_Audio_To_Text("exem3.mp3"))