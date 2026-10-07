# JARVIS

A small voice assistant I wrote in Python, inspired by JARVIS from Iron Man. It listens through the microphone, turns what you say into text, sends it to an OpenAI model, and prints the reply (and tries to read it out loud).

## How it works

Everything is in `jarvis.py`:

1. `record_text()` uses the SpeechRecognition library to listen on the microphone and convert speech to text with Google's free speech recognition.
2. The text is added to a running list of messages, which starts with a prompt asking the model to act like JARVIS. Keeping the list means the model sees the earlier conversation.
3. `send_to_chatGPT()` sends the messages to OpenAI with `openai.ChatCompletion.create` (max 100 tokens, temperature 0.5) and adds the reply to the history.
4. `convert_text()` is meant to speak the reply with pyttsx3, and the reply is printed to the console.

## Tech

Python, OpenAI API, SpeechRecognition, pyttsx3, python-dotenv

## Running it

```bash
pip install -r requirements.txt
```

Create a `.env` file next to `jarvis.py` (it is gitignored):

```
OPENAI_KEY=your-key-here
```

Then run:

```bash
python jarvis.py
```

You need a working microphone. PyAudio is needed for microphone input and can be fiddly to install on some systems.

## Limitations

This was an early learning project and it has some known problems:

- It uses the old `openai.ChatCompletion` interface, so it needs `openai` older than 1.0.
- The default model (`text-davinci-edit-001`) has been retired by OpenAI, so it needs to be changed to a current chat model to work.
- `convert_text()` calls `engine.say()` without passing the text, so the reply is printed but not spoken yet.
- It runs in an endless loop until you stop it with Ctrl+C.
