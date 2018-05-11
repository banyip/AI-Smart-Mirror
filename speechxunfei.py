# speechxunfei.py
# speechrecognition, pyaudio, brew install portaudio
import speech_recognition as sr
import os
import requests
import stt
import tts
from pydub import AudioSegment
from pydub.playback import play


class Speechxunfei(object):
    def __init__(self, launch_phrase="mirror mirror", debugger_enabled=False):
        self.launch_phrase = launch_phrase
        self.debugger_enabled = debugger_enabled
        self.__debugger_microphone(enable=False)

    def xunfei_speech_recognition(self, audio):
        speech = None
        try:
            speech = stt.speech_to_text(audio)
            print("Google Speech Recognition thinks you said " + speech)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return speech

 
    def listen_for_micaudio(self):
        audio = input_from_mic()
        return audio


    def is_call_to_action(self, recognizer, audio):
        speech = self.google_speech_recognition(recognizer, audio)

        if speech is not None and self.launch_phrase in speech.lower():
            return True

        return False

    def is_call_to_action(self, audio):
        speech = self.xunfei_speech_recognition( audio)

        if speech is not None and self.launch_phrase in speech.lower():
            return True

        return False

    def synthesize_text(self, text):
        tts.text_to_speech(text,"tmp.wav")
        song = AudioSegment.from_wav("tmp.mp3")
        play(song)
        os.remove("tmp.mp3")

    def __debugger_microphone(self, enable=True):
        if self.debugger_enabled:
            try:
                r = requests.get("http://localhost:8080/microphone?enabled=%s" % str(enable))
                if r.status_code != 200:
                    print("Used wrong endpoint for microphone debugging")
            except Exception as e:
                print(e)