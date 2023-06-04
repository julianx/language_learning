import random
import subprocess
import sys
import threading
from random import randint
from random import shuffle


class Word(object):
    x = 0
    y = 0
    value = ""
    meaning = ""

    def __init__(self, value: str = "", meaning: str = ""):
        self.x = randint(1, 100)
        self.value = value
        if meaning:
            self.meaning = meaning
        else:
            self.meaning = self.value


def populate_word_list():
    hiragana = ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ", "た", "ち", "つ",
                "て", "と", "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", "ま", "み", "む", "め", "も", "ら",
                "り", "る", "れ", "ろ", "わ", "を", "や", "ゆ", "よ", "ん", ]
    simple_words = [["これ", "this thing"], ["この", "this person"], ["それ", "that/it thing"], ["その", "that person"],
                    ["あれ", "That over there"], ["あの", "That thing/person over there"], ["私", "わたし"], ["僕", "ぼく"],
                    ["彼", "かれ, he"], ["彼女", "かのじょ, She"], ["私たち", "わたしたち, we"], ["彼ら", "かれら, they"], ]

    result = hiragana + simple_words
    random.shuffle(result)
    return result


def thread_function(value):
    if len(value) == 1:
        subprocess.run(["say", value])
    else:
        command = ["say"] + value.split()
        subprocess.run(command)


def main(argv):
    game_list = []
    word_list = populate_word_list()
    for word in word_list:
        if len(word) == 2:
            instance = Word(value=word[0], meaning=word[1])
        else:
            instance = Word(value=word)
        game_list.append(instance)

    done = False
    score = 0
    max_score = 100
    print("Japanese practice game! Type in the word you see, mirroring the output. Try getting to 100.")
    while not done and score < max_score:
        for challenge in game_list:
            print(f"Score: {score}")
            thread = threading.Thread(target=thread_function, args=(challenge.value,))
            answer = input(challenge.value)
            if answer in ["q", "Q", "quit"]:
                done = True
            elif answer == challenge.value:
                score += 1
                print("Correct")
            else:
                score -= 10
                print("Wrong!", challenge.value, challenge.meaning)
            thread.start()
            if score >= max_score:
                print("Congrats! You have reached the target score.")
                print(f"Score: {score}")
                done = True
                break
        shuffle(game_list)



if __name__ == "__main__":
    main(sys.argv[1:])
