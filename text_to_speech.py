import pyttsx3
import requests

def speak(text):
    corrected_text = check_grammar(text)
    if corrected_text:
        corrected_text = corrected_text.lower()
        engine = pyttsx3.init()
        engine.say(corrected_text)
        engine.runAndWait()


def check_grammar(text):
    url = "https://api.languagetool.org/v2/check"
    playload = {
        "text": text,
        "language": "en-US"
    }
    response = requests.post(url, data=playload)
    result = response.json()

    if result["matches"]:
        corrected_text = text
        for match in result["matches"]:
          if match["replacements"]:
              incorrect_part = match["context"]["text"][match["offset"]:match["offset"] + match["length"]]
              correction = match["replacements"][0]["value"]
              corrected_text = corrected_text.replace(
                  incorrect_part, correction, 1)
        return corrected_text
    else:
        return text
