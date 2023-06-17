import random
import subprocess
import sys
import threading
from random import shuffle


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Word(object):
    def __init__(self, word, meaning=""):
        self.word = word
        self.meaning = meaning
        self.challenge_str = f"{self.word} "

    def __str__(self):
        if self.meaning:
            return f"{self.challenge_str} {self.meaning}　"
        else:
            return f"{self.word}"

    def check(self, answer):
        self.pronounce()
        return answer == self.word

    def pronounce(self):
        thread = threading.Thread(target=self.thread_function, args=())
        thread.start()

    def thread_function(self):
        if len(self.word) == 1:
            subprocess.run(["say", self.word])
        else:
            command = ["say"] + self.word.split()
            subprocess.run(command)


class KanjiWord(Word):
    def __init__(self, kanji, word, meaning):
        super().__init__(word=word, meaning=meaning)
        self.kanji = kanji

        if self.kanji and self.word:
            self.challenge_str = f"{self.kanji} / {self.word} "


def populate_word_list():
    result = [
        Word(word="あ"), Word(word="い"), Word(word="う"), Word(word="え"), Word(word="お"),
        Word(word="か"), Word(word="き"), Word(word="く"), Word(word="け"), Word(word="こ"),
        Word(word="さ"), Word(word="し"), Word(word="す"), Word(word="せ"), Word(word="そ"),
        Word(word="た"), Word(word="ち"), Word(word="つ"), Word(word="て"), Word(word="と"),
        Word(word="な"), Word(word="に"), Word(word="ぬ"), Word(word="ね"), Word(word="の"),
        Word(word="は"), Word(word="ひ"), Word(word="ふ"), Word(word="へ"), Word(word="ほ"),
        Word(word="ま"), Word(word="み"), Word(word="む"), Word(word="め"), Word(word="も"),
        Word(word="ら"), Word(word="り"), Word(word="る"), Word(word="れ"), Word(word="ろ"),
        Word(word="わ"), Word(word="を"), Word(word="や"), Word(word="ゆ"), Word(word="よ"),
        Word(word="ん"),

        Word(word="が"), Word(word="ぎ"), Word(word="ぐ"), Word(word="げ"), Word(word="ご"),
        Word(word="ざ"), Word(word="じ"), Word(word="ず"), Word(word="ぜ"), Word(word="ぞ"),
        Word(word="だ"), Word(word="ぢ"), Word(word="づ"), Word(word="で"), Word(word="ど"),
        Word(word="ば"), Word(word="び"), Word(word="ぶ"), Word(word="べ"), Word(word="ぼ"),
        Word(word="ぱ"), Word(word="ぴ"), Word(word="ぷ"), Word(word="ぺ"), Word(word="ぽ"),

        Word(word="きゃ"), Word(word="きゅ"), Word(word="きょ"),
        Word(word="しゃ"), Word(word="しゅ"), Word(word="しょ"),
        Word(word="ちゃ"), Word(word="ちゅ"), Word(word="ちょ"),
        Word(word="にゃ"), Word(word="にゅ"), Word(word="にょ"),
        Word(word="ひゃ"), Word(word="ひゅ"), Word(word="ひょ"),
        Word(word="みゃ"), Word(word="みゅ"), Word(word="みょ"),
        Word(word="りゃ"), Word(word="りゅ"), Word(word="りょ"),
        Word(word="ぎゃ"), Word(word="ぎゅ"), Word(word="ぎょ"),
        Word(word="じゃ"), Word(word="じゅ"), Word(word="じょ"),
        Word(word="びゃ"), Word(word="びゅ"), Word(word="びょ"),
        Word(word="ぴゃ"), Word(word="ぴゅ"), Word(word="ぴょ"),

        Word(word="ア"), Word(word="イ"), Word(word="ウ"), Word(word="エ"), Word(word="オ"),
        Word(word="カ"), Word(word="キ"), Word(word="ク"), Word(word="ケ"), Word(word="コ"),
        Word(word="サ"), Word(word="シ"), Word(word="ス"), Word(word="セ"), Word(word="ソ"),
        Word(word="タ"), Word(word="チ"), Word(word="ツ"), Word(word="テ"), Word(word="ト"),
        Word(word="ナ"), Word(word="ニ"), Word(word="ヌ"), Word(word="ネ"), Word(word="ノ"),
        Word(word="ハ"), Word(word="ヒ"), Word(word="フ"), Word(word="ヘ"), Word(word="ホ"),
        Word(word="マ"), Word(word="ミ"), Word(word="ム"), Word(word="メ"), Word(word="モ"),
        Word(word="ヤ"), Word(word="ユ"), Word(word="ヨ"), Word(word="ラ"), Word(word="リ"),
        Word(word="ル"), Word(word="レ"), Word(word="ロ"), Word(word="ワ"), Word(word="ヲ"),
        Word(word="ン"), Word(word="ガ"), Word(word="ギ"), Word(word="グ"), Word(word="ゲ"),
        Word(word="ゴ"), Word(word="ザ"), Word(word="ジ"), Word(word="ズ"), Word(word="ゼ"),
        Word(word="ゾ"), Word(word="ダ"), Word(word="ヂ"), Word(word="ヅ"), Word(word="デ"),
        Word(word="ド"), Word(word="バ"), Word(word="ビ"), Word(word="ブ"), Word(word="ベ"),
        Word(word="ボ"), Word(word="パ"), Word(word="ピ"), Word(word="プ"), Word(word="ペ"),
        Word(word="ポ"),
        Word(word="キャ"), Word(word="キュ"), Word(word="キョ"),
        Word(word="シャ"), Word(word="シュ"), Word(word="ショ"),
        Word(word="チャ"), Word(word="チュ"), Word(word="チョ"),
        Word(word="ニャ"), Word(word="ニュ"), Word(word="ニョ"),
        Word(word="ヒャ"), Word(word="ヒュ"), Word(word="ヒョ"),
        Word(word="ミャ"), Word(word="ミュ"), Word(word="ミョ"),
        Word(word="リャ"), Word(word="リュ"), Word(word="リョ"),
        Word(word="ギャ"), Word(word="ギュ"), Word(word="ギョ"),
        Word(word="ジャ"), Word(word="ジュ"), Word(word="ジョ"),
        Word(word="ビャ"), Word(word="ビュ"), Word(word="ビョ"),
        Word(word="ピャ"), Word(word="ピュ"), Word(word="ピョ"),

        Word(word="これ", meaning="This thing"),
        Word(word="この", meaning="This person"),
        Word(word="それ", meaning="That/it thing"),
        Word(word="その", meaning="That person"),
        Word(word="あれ", meaning="That over there"),
        Word(word="あの", meaning="That thing/person over there"),
        Word(word="あなた", meaning="You"),
        KanjiWord(word="わたし", kanji="私", meaning="I"),
        KanjiWord(word="ぼく", kanji="僕", meaning="me"),
        KanjiWord(word="かれ", kanji="彼", meaning="He"),
        KanjiWord(word="かのじょ", kanji="彼女", meaning="She"),
        KanjiWord(word="わたしたち", kanji="私たち", meaning="We"),
        KanjiWord(word="かれら", kanji="彼ら", meaning="They"),

        KanjiWord(word="きょう", kanji="今日", meaning="Today"),
        KanjiWord(word="あした", kanji="明日", meaning="Tomorrow"),
        KanjiWord(word="きのう", kanji="昨日", meaning="Yesterday"),
        KanjiWord(word="いま", kanji="今", meaning="Now"),
        KanjiWord(word="まえに", kanji="前に", meaning="Before"),
        KanjiWord(word="あとで", kanji="後で", meaning="Later"),

        Word(word="する", meaning="To do"),
        Word(word="です", meaning="To be"),
        Word(word="なる", meaning="To become"),
        Word(word="ある", meaning="There is (inanimate)"),
        Word(word="いる", meaning="There is (living)"),
        KanjiWord(word="いく", kanji="行く", meaning="To go"),
        KanjiWord(word="いう", kanji="言う", meaning="To say"),
        KanjiWord(word="みる", kanji="見る", meaning="To see"),
        KanjiWord(word="くる", kanji="来る", meaning="To come"),
        KanjiWord(word="たべる", kanji="食べる", meaning="To eat"),
        KanjiWord(word="あそぶ", kanji="遊ぶ", meaning="to play"),
        KanjiWord(word="ねる", kanji="寝る", meaning="to sleep"),
        KanjiWord(word="はしる", kanji="走る", meaning="to run"),
        KanjiWord(word="とぶ", kanji="飛ぶ", meaning="to jump"),
        KanjiWord(word="なく", kanji="泣く", meaning="to cry"),
        KanjiWord(word="わらう", kanji="笑う", meaning="to laugh"),
        KanjiWord(word="よむ", kanji="読む", meaning="to read"),
        KanjiWord(word="かく", kanji="書く", meaning="to write"),
        KanjiWord(word="かく", kanji="描く", meaning="to draw"),
        KanjiWord(word="のむ", kanji="飲む", meaning="to drink"),
        KanjiWord(word="おきる", kanji="起きる", meaning="to wake up"),
        KanjiWord(word="あるく", kanji="歩く", meaning="to walk"),
        KanjiWord(word="きく", kanji="聞く", meaning="to listen"),
        KanjiWord(word="まつ", kanji="待つ", meaning="to wait"),
        KanjiWord(word="およぐ", kanji="泳ぐ", meaning="to swim"),
        KanjiWord(word="うたう", kanji="歌う", meaning="to sing"),
        KanjiWord(word="おんがくをきく", kanji="音楽を聞く", meaning="to listen to music"),
        KanjiWord(word="えをかく", kanji="絵を描く", meaning="to draw a picture"),
        KanjiWord(word="あらう", kanji="洗う", meaning="to wash")
    ]

    random.shuffle(result)
    return result


def main(argv):
    word_list = populate_word_list()

    done = False
    score = 0
    max_score = 100
    print("Japanese practice game! Type in the word you see, mirroring the output. Try getting to 100.")
    while not done and score < max_score:
        for word in word_list:
            print(f"Score: {score}")
            answer = input(word)
            if answer in ["q", "Q", "quit"]:
                done = True
            elif word.check(answer=answer):
                score += 1
                print(bcolors.OKGREEN, "Correct", word, bcolors.ENDC)
            else:
                score -= 10
                print(bcolors.FAIL, "Wrong!", bcolors.ENDC)
            if score >= max_score:
                print(bcolors.OKCYAN, "Congrats! You have reached the target score.", f"Score: {score}", bcolors.ENDC)
                done = True
                break
        shuffle(word_list)


if __name__ == "__main__":
    main(sys.argv[1:])
