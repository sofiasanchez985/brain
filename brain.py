import json
import speech_recognition as sr

database = json.load(open("dictionary.json"))


def get_category(text):
    for category in database:
        for word in database[category]["words"]:
            if word in text.lower() or text.lower() in word:
                return category
    return "Not Found"


def show_region(category):
    print(category + ": " + database[category]["color"])


if __name__ == "__main__":
    rec = sr.Recognizer()
    wav_file = "family.wav"
    with sr.AudioFile(wav_file) as src:
        audio = rec.listen(src)
        word = rec.recognize_google(audio)
    show_region(get_category(word))
