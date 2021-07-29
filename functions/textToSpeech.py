from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat, languageconfig
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from functions.translations import translate
import json


subscription_key = "your subscription_key"
region = "your region"

# Fonctionnelle
def config_sounds(message) :
    en_message = translate(message)
    en_message = json.loads(en_message)
    en_message = en_message[0]["translations"][0]["text"]
    
    fichier = open("ssml.xml", "w")
    ssml_file = "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='fr-FR' xmlns:mstts='http://www.w3.org/2001/mstts' xmlns:emo='http://www.w3.org/2009/10/emotionml'>\n"
    ssml_file+="    <voice name='fr-FR-HenriNeural'>\n"
    ssml_file+="        "+message+"\n"
    ssml_file+="    </voice>\n</speak>"
    fichier.write(ssml_file)
    fichier.close()
    
    textToSpeech(en_message)
    
# Fonctionnelle
def textToSpeech(english_message) :
    speech_config = SpeechConfig(subscription=subscription_key, region=region)
    
    #avec le ssml.xml pour le français
    fr_synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)
    ssml_string = open("ssml.xml", "r").read()
    result = fr_synthesizer.speak_ssml_async(ssml_string).get()
    stream = AudioDataStream(result)
    stream.save_to_wav_file("sounds/french.wav")
    
    #de base en anglais
    en_audio_config = AudioOutputConfig(filename="sounds/english.wav")
    en_synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=en_audio_config)
    en_synthesizer.speak_text_async(english_message)
