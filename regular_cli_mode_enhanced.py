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
    challenge_str = ""

    def __init__(self, kwargs):
        if "kanji" in kwargs.keys():
            self.kanji = kwargs.get("kanji")
            # self.challenge = self.kanji
        if "hiragana" in kwargs.keys():
            self.hiragana = kwargs.get("hiragana")
        if "meaning" in kwargs.keys():
            self.meaning = kwargs.get("meaning")

        if self.hiragana and self.kanji:
            self.challenge_str = f"{self.kanji} / {self.hiragana} "
        elif self.hiragana:
            self.challenge_str = f"{self.hiragana} "

        if not self.challenge:
            if self.hiragana:
                self.challenge = self.hiragana
            else:
                self.challenge = self.kanji

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

        {"hiragana": "が"},
        {"hiragana": "ぎ"},
        {"hiragana": "ぐ"},
        {"hiragana": "げ"},
        {"hiragana": "ご"},
        {"hiragana": "ざ"},
        {"hiragana": "じ"},
        {"hiragana": "ず"},
        {"hiragana": "ぜ"},
        {"hiragana": "ぞ"},
        {"hiragana": "だ"},
        {"hiragana": "ぢ"},
        {"hiragana": "づ"},
        {"hiragana": "で"},
        {"hiragana": "ど"},
        {"hiragana": "ば"},
        {"hiragana": "び"},
        {"hiragana": "ぶ"},
        {"hiragana": "べ"},
        {"hiragana": "ぼ"},
        {"hiragana": "ぱ"},
        {"hiragana": "ぴ"},
        {"hiragana": "ぷ"},
        {"hiragana": "ぺ"},
        {"hiragana": "ぽ"},

        {"hiragana": "きゃ"},
        {"hiragana": "きゅ"},
        {"hiragana": "きょ"},
        {"hiragana": "しゃ"},
        {"hiragana": "しゅ"},
        {"hiragana": "しょ"},
        {"hiragana": "ちゃ"},
        {"hiragana": "ちゅ"},
        {"hiragana": "ちょ"},
        {"hiragana": "にゃ"},
        {"hiragana": "にゅ"},
        {"hiragana": "にょ"},
        {"hiragana": "ひゃ"},
        {"hiragana": "ひゅ"},
        {"hiragana": "ひょ"},
        {"hiragana": "みゃ"},
        {"hiragana": "みゅ"},
        {"hiragana": "みょ"},
        {"hiragana": "りゃ"},
        {"hiragana": "りゅ"},
        {"hiragana": "りょ"},
        {"hiragana": "ぎゃ"},
        {"hiragana": "ぎゅ"},
        {"hiragana": "ぎょ"},
        {"hiragana": "じゃ"},
        {"hiragana": "じゅ"},
        {"hiragana": "じょ"},
        {"hiragana": "びゃ"},
        {"hiragana": "びゅ"},
        {"hiragana": "びょ"},
        {"hiragana": "ぴゃ"},
        {"hiragana": "ぴゅ"},
        {"hiragana": "ぴょ"},

        {"katakana": "ア"},
        {"katakana": "イ"},
        {"katakana": "ウ"},
        {"katakana": "エ"},
        {"katakana": "オ"},
        {"katakana": "カ"},
        {"katakana": "キ"},
        {"katakana": "ク"},
        {"katakana": "ケ"},
        {"katakana": "コ"},
        {"katakana": "サ"},
        {"katakana": "シ"},
        {"katakana": "ス"},
        {"katakana": "セ"},
        {"katakana": "ソ"},
        {"katakana": "タ"},
        {"katakana": "チ"},
        {"katakana": "ツ"},
        {"katakana": "テ"},
        {"katakana": "ト"},
        {"katakana": "ナ"},
        {"katakana": "ニ"},
        {"katakana": "ヌ"},
        {"katakana": "ネ"},
        {"katakana": "ノ"},
        {"katakana": "ハ"},
        {"katakana": "ヒ"},
        {"katakana": "フ"},
        {"katakana": "ヘ"},
        {"katakana": "ホ"},
        {"katakana": "マ"},
        {"katakana": "ミ"},
        {"katakana": "ム"},
        {"katakana": "メ"},
        {"katakana": "モ"},
        {"katakana": "ヤ"},
        {"katakana": "ユ"},
        {"katakana": "ヨ"},
        {"katakana": "ラ"},
        {"katakana": "リ"},
        {"katakana": "ル"},
        {"katakana": "レ"},
        {"katakana": "ロ"},
        {"katakana": "ワ"},
        {"katakana": "ヲ"},
        {"katakana": "ン"},
        {"katakana": "ガ"},
        {"katakana": "ギ"},
        {"katakana": "グ"},
        {"katakana": "ゲ"},
        {"katakana": "ゴ"},
        {"katakana": "ザ"},
        {"katakana": "ジ"},
        {"katakana": "ズ"},
        {"katakana": "ゼ"},
        {"katakana": "ゾ"},
        {"katakana": "ダ"},
        {"katakana": "ヂ"},
        {"katakana": "ヅ"},
        {"katakana": "デ"},
        {"katakana": "ド"},
        {"katakana": "バ"},
        {"katakana": "ビ"},
        {"katakana": "ブ"},
        {"katakana": "ベ"},
        {"katakana": "ボ"},
        {"katakana": "パ"},
        {"katakana": "ピ"},
        {"katakana": "プ"},
        {"katakana": "ペ"},
        {"katakana": "ポ"},
        {"katakana": "キャ"},
        {"katakana": "キュ"},
        {"katakana": "キョ"},
        {"katakana": "シャ"},
        {"katakana": "シュ"},
        {"katakana": "ショ"},
        {"katakana": "チャ"},
        {"katakana": "チュ"},
        {"katakana": "チョ"},
        {"katakana": "ニャ"},
        {"katakana": "ニュ"},
        {"katakana": "ニョ"},
        {"katakana": "ヒャ"},
        {"katakana": "ヒュ"},
        {"katakana": "ヒョ"},
        {"katakana": "ミャ"},
        {"katakana": "ミュ"},
        {"katakana": "ミョ"},
        {"katakana": "リャ"},
        {"katakana": "リュ"},
        {"katakana": "リョ"},
        {"katakana": "ギャ"},
        {"katakana": "ギュ"},
        {"katakana": "ギョ"},
        {"katakana": "ジャ"},
        {"katakana": "ジュ"},
        {"katakana": "ジョ"},
        {"katakana": "ビャ"},
        {"katakana": "ビュ"},
        {"katakana": "ビョ"},
        {"katakana": "ピャ"},
        {"katakana": "ピュ"},
        {"katakana": "ピョ"},

    {"hiragana": "これ", "meaning": "This thing"},
        {"hiragana": "この", "meaning": "This person"},
        {"hiragana": "それ", "meaning": "That/it thing"},
        {"hiragana": "その", "meaning": "That person"},
        {"hiragana": "あれ", "meaning": "That over there"},
        {"hiragana": "あの", "meaning": "That thing/person over there"},
        {"kanji": "私", "hiragana": "わたし", "meaning": "I"},
        {"hiragana": "あなた", "meaning": "You"},
        {"kanji": "僕", "hiragana": "ぼく", "meaning": "me"},
        {"kanji": "彼", "hiragana": "かれ", "meaning": "He"},
        {"kanji": "彼女", "hiragana": "かのじょ", "meaning": "She"},
        {"kanji": "私たち", "hiragana": "わたしたち", "meaning": "We"},
        {"kanji": "彼ら", "hiragana": "かれら", "meaning": "They"},

        {"kanji": "今日", "hiragana": "きょう", "meaning": "Today"},
        {"kanji": "明日", "hiragana": "あした", "meaning": "Tomorrow"},
        {"kanji": "昨日", "hiragana": "きのう", "meaning": "Yesterday"},
        {"kanji": "今", "hiragana": "いま", "meaning": "Now"},
        {"kanji": "前に", "hiragana": "まえに", "meaning": "Before"},
        {"kanji": "後で", "hiragana": "あとで", "meaning": "Later"},

        {"hiragana": "する", "meaning": "To do"},
        {"hiragana": "です", "meaning": "To be"},
        {"hiragana": "なる", "meaning": "To become"},
        {"hiragana": "ある", "meaning": "There is (inanimate)"},
        {"hiragana": "いる", "meaning": "There is (living)"},
        {"kanji": "行く", "hiragana": "いく", "meaning": "To go"},
        {"kanji": "言う", "hiragana": "いう", "meaning": "To say"},
        {"kanji": "見る", "hiragana": "みる", "meaning": "To see"},
        {"kanji": "来る", "hiragana": "くる", "meaning": "To come"},
        {"kanji": "食べる", "hiragana": "たべる", "meaning": "To eat"},
        {"kanji": "遊ぶ", "hiragana": "あそぶ", "meaning": "to play"},
        {"kanji": "寝る", "hiragana": "ねる", "meaning": "to sleep"},
        {"kanji": "走る", "hiragana": "はしる", "meaning": "to run"},
        {"kanji": "飛ぶ", "hiragana": "とぶ", "meaning": "to jump"},
        {"kanji": "泣く", "hiragana": "なく", "meaning": "to cry"},
        {"kanji": "笑う", "hiragana": "わらう", "meaning": "to laugh"},
        {"kanji": "読む", "hiragana": "よむ", "meaning": "to read"},
        {"kanji": "書く", "hiragana": "かく", "meaning": "to write"},
        {"kanji": "描く", "hiragana": "かく", "meaning": "to draw"},

        {"kanji": "飲む", "hiragana": "のむ", "meaning": "to drink"},
        {"kanji": "起きる", "hiragana": "おきる", "meaning": "to wake up"},
        {"kanji": "歩く", "hiragana": "あるく", "meaning": "to walk"},
        {"kanji": "聞く", "hiragana": "きく", "meaning": "to listen"},
        {"kanji": "待つ", "hiragana": "まつ", "meaning": "to wait"},
        {"kanji": "泳ぐ", "hiragana": "およぐ", "meaning": "to swim"},
        {"kanji": "歌う", "hiragana": "うたう", "meaning": "to sing"},
        {"kanji": "音楽を聞く", "hiragana": "おんがくをきく", "meaning": "to listen to music"},
        {"kanji": "絵を描く", "hiragana": "えをかく", "meaning": "to draw a picture"},
        {"kanji": "洗う", "hiragana": "あらう", "meaning": "to wash"}


    ]

    random.shuffle(result)
    return result


def thread_function(value):
    if value.hiragana:
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
            answer = input(word.challenge_str)
            if answer in ["q", "Q", "quit"]:
                done = True
            elif answer == word.hiragana:
                score += 1
                print("Correct", word)
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
