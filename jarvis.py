# from speech to text and text to speech
import openai
import speech_recognition as sr
import pyttsx3

import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

openai.api_key = "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"

prompt = 'Jarvis,'

# function to convert  text to speech \


def convert_text(command):
    # init the engine
    engine = pyttsx3.init()
    engine.say()
    engine.runAndWait()


# init the recognizer
r = sr.Recognizer()


def record_text():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("I'm listening")
                audio2 = r.listen(source2)
                print("Recognized Audio:", r.recognize_google(audio2))
                My_Text = r.recognize_google(audio2)
                return My_Text
        except sr.RequestError as e:
            print("couldn't request result: {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred")


def send_to_chatGPT(messages, model="text-davinci-003"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message


messages = [{"role": "user", "content": "please act like JARVIS from Ironman"}]
while (1):
    text = record_text()
    messages.append({"role": "user", "content": text})
    response = send_to_chatGPT(messages)
    convert_text(response)
    print(response)
