import pyttsx3
import speech_recognition as sr


class reco_vocal:
    def __init__(self):
        self.speech  = sr.Recognizer()
        self.mic = sr.Microphone()
        self.av = pyttsx3.init()

    def readText(self,text):
        self.av.say(text)
        self.av.runAndWait()

    def command(self):
        try:
            self.readText("Je vous écoute.")

            with self.mic as source:
                self.speech.pause_threshold = 1
                audio = self.speech.listen(source)
            request = self.speech.recognize_google(audio, language='fr-FR')

            return request

        except Exception as e:
            print(e)
            self.readText("Je n'ai pas compris, pouvez vous répéter ?")
            self.command()
            return None