import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import transformers
import pyttsx3

# Build the AI
class ChatBot():
    def __init__(self, name):
        print("--- starting up", name, "---")
        self.text= ""
        self.name = name
    # Run the AI
    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio= recognizer.listen(mic)
            try:
                self.text = recognizer.recognize_google(audio, language="es-ES")
                print("me --> ", self.text)
            except:
                print("me --> ERROR")
    def wake_up(self, text):
        return True if self.name in text.lower() else False
    @staticmethod
    def text_to_speech(text):
        print("ai --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        os.system("start res.mp3") #macbook->afplay | windows->start
        os.remove("res.mp3")

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')

if __name__ == "__main__":
    ai = ChatBot(name="Smart Gym")
    #nlp = transformers.pipeline("conversational",model="microsoft/DialoGPT-medium")
    #chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
    #res = str(chat)
    #res = res[res.find("bot >> ")+6:].strip()
    res = "Hola que tal, soy SmartGym, tu asistente personal. ¿En que puedo ayudarte?"
    ai.text_to_speech(res)
    while True:
        ai.speech_to_text()
        ## wake up
        if ai.wake_up(ai.text) is True:
            res = "Hola que tal, soy SmartGym, tu asistente personal. ¿En que puedo ayudarte?"
            ai.text_to_speech(res)
        elif "tiempo" in ai.text:
            res = ai.action_time()
            ## respond politely
        elif any(i in ai.text for i in ["gracias"]):
            res = np.random.choice(
            ["No hay de que!","Sin problemas!",
            "Genial!",
            "Estoy aqui para lo que necesites!"])
            ai.text_to_speech(res)