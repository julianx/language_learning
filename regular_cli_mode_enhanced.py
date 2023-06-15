import random
import subprocess
import sys
import threading
from random import shuffle


class Word(object):
    kanji = ""
    hiragana = ""
    meaning = ""
    challenge = ""

    def __init__(self, kwargs):
        if "kanji" in kwargs.keys():
            self.kanji = kwargs.get("kanji")
            self.challenge = self.kanji
        if "hiragana" in kwargs.keys():
            self.hiragana = kwargs.get("hiragana")
        if "meaning" in kwargs.keys():
            self.meaning = kwargs.get("meaning")

        if not self.challenge:
            if self.hiragana:
                self.challenge = self.hiragana
            else:
                self.challenge = "error"

    def __str__(self):
        return f"{self.kanji} {self.hiragana} {self.meaning}"


def populate_word_list():
    result = [
        {"hiragana": "あ"},
        {"hiragana": "い"},
        {"hiragana": "う"},
        {"hiragana": "え"},
        {"hiragana": "お"},
        {"hiragana": "か"},
        {"hiragana": "き"},
        {"hiragana": "く"},
        {"hiragana": "け"},
        {"hiragana": "こ"},
        {"hiragana": "さ"},
        {"hiragana": "し"},
        {"hiragana": "す"},
        {"hiragana": "せ"},
        {"hiragana": "そ"},
        {"hiragana": "た"},
        {"hiragana": "ち"},
        {"hiragana": "つ"},
        {"hiragana": "て"},
        {"hiragana": "と"},
        {"hiragana": "な"},
        {"hiragana": "に"},
        {"hiragana": "ぬ"},
        {"hiragana": "ね"},
        {"hiragana": "の"},
        {"hiragana": "は"},
        {"hiragana": "ひ"},
        {"hiragana": "ふ"},
        {"hiragana": "へ"},
        {"hiragana": "ほ"},
        {"hiragana": "ま"},
        {"hiragana": "み"},
        {"hiragana": "む"},
        {"hiragana": "め"},
        {"hiragana": "も"},
        {"hiragana": "ら"},
        {"hiragana": "り"},
        {"hiragana": "る"},
        {"hiragana": "れ"},
        {"hiragana": "ろ"},
        {"hiragana": "わ"},
        {"hiragana": "を"},
        {"hiragana": "や"},
        {"hiragana": "ゆ"},
        {"hiragana": "よ"},
        {"hiragana": "ん"},
        {"hiragana": "これ", "meaning": "This thing"},
        {"hiragana": "この", "meaning": "This person"},
        {"hiragana": "それ", "meaning": "That/it thing"},
        {"hiragana": "その", "meaning": "That person"},
        {"hiragana": "あれ", "meaning": "That over there"},
        {"hiragana": "あの", "meaning": "That thing/person over there"},
        {"kanji": "私", "hiragana": "わたし", "meaning": "me"},
        {"kanji": "僕", "hiragana": "ぼく", "meaning": "me"},
        {"kanji": "彼", "hiragana": "かれ", "meaning": "He"},
        {"kanji": "彼女", "hiragana": "かのじょ", "meaning": "She"},
        {"kanji": "私たち", "hiragana": "わたしたち", "meaning": "We"},
        {"kanji": "彼ら", "hiragana": "かれら", "meaning": "They"},
    ]

    random.shuffle(result)
    return result


def thread_function(value):
    if value.kanji:
        value = value.kanji
    elif value.hiragana:
        value = value.hiragana

    if len(value) == 1:
        subprocess.run(["say", value])
    else:
        command = ["say"] + value.split()
        subprocess.run(command)


def main(argv):
    game_list = []
    word_list = populate_word_list()
    for word in word_list:
        instance = Word(word)
        game_list.append(instance)

    done = False
    score = 0
    max_score = 100
    print("Japanese practice game! Type in the word you see, mirroring the output. Try getting to 100.")
    while not done and score < max_score:
        for word in game_list:
            print(f"Score: {score}")
            thread = threading.Thread(target=thread_function, args=(word,))
            answer = input(word.challenge)
            if answer in ["q", "Q", "quit"]:
                done = True
            elif answer == word.hiragana:
                score += 1
                print("Correct")
            else:
                score -= 10
                print("Wrong!", word)
            thread.start()
            if score >= max_score:
                print("Congrats! You have reached the target score.")
                print(f"Score: {score}")
                done = True
                break
        shuffle(game_list)


if __name__ == "__main__":
    main(sys.argv[1:])
