import json
import speech_recognition as sr
from flask import *

database = json.load(open("dictionary.json"))
app = Flask(__name__, static_url_path='', static_folder='web/static', template_folder='web/templates')


@app.route('/')
def index():
    return render_template('index.html', tactile=database["tactile"]["bool"],
                           visual=database["visual"]["bool"], bodypart=database["bodypart"]["bool"],
                           mental=database["mental"]["bool"], number=database["number"]["bool"],
                           outdoor=database["outdoor"]["bool"], person=database["person"]["bool"],
                           place=database["place"]["bool"], social=database["social"]["bool"],
                           time=database["time"]["bool"], violence=database["violence"]["bool"])


def get_category(text):
    for category in database:
        for word in database[category]["words"]:
            if word in text.lower() or text.lower() in word:
                return category
    return "Not Found"


def add_word(text, category):
    if category in database:
        database[category]["words"].append(text.lower())


def show_region(category):
    if category in database:
        database[category]["bool"] = "true"
        print(category)
    else:
        print("ERROR")


def reset_bools():
    for category in database:
        database[category]["bool"] = "false"


if __name__ == "__main__":
    rec = sr.Recognizer()
    wav_file = "hello.wav"
    with sr.AudioFile(wav_file) as src:
        audio = rec.listen(src)
        word = rec.recognize_google(audio)
    region = get_category(word)
    if region == "Not Found":
        # select new region for word
        region = input("Corresponding category not found. Enter category for " + word + ": ")
        add_word(word, region)
    show_region(region)
    # reset_bools()
    # json.dump(database, open("dictionary.json", "w"), indent=4)
    app.run()
