import json


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
    word = input()
    show_region(get_category(word))
