import json
from difflib import get_close_matches


data = json.load(open("data.json", "r"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead?" % get_close_matches(word, data.keys())[0])
        ans = input("please type yes or no\n")
        if ans == "yes":
            return cdata[get_close_matches(word, data.keys())[0]]
        else:
            return "sorry, we don't know %s" % word
    else:
        return "the word doesn't exsist. Please check it out."


word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for val in output:
        print(val)
else:
    print(output)
