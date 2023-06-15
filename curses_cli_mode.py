import random
import subprocess
import sys
import threading
from random import randint
from random import shuffle

import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle


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


def init_curses():
    # Do not echo keys back to the client.
    # curses.noecho()

    # Non-blocking or cbreak mode... do not wait for Enter key to be pressed.
    # curses.cbreak()

    # Turn off blinking cursor
    curses.curs_set(False)

    # Enable color if we can...
    if curses.has_colors():
        curses.start_color()

    # Optional - Enable the keypad. This also decodes multi-byte key sequences
    # stdscr.keypad(True)


def end_curses():
    # BEGIN ncurses shutdown/deinitialization...
    # Turn off cbreak mode...
    curses.nocbreak()

    # Turn echo back on.
    curses.echo()

    # Restore cursor blinking.
    curses.curs_set(True)

    # Turn off the keypad...
    # stdscr.keypad(False)

    # Restore Terminal to original state.
    curses.endwin()


def set_footer_message(stdscr, message):
    # Place a caption at the bottom left of the terminal indicating
    # action keys.
    stdscr.addstr(curses.LINES - 1, 0, message)
    stdscr.refresh()


def main(stdscr):
    init_curses()
    # Clear screen
    stdscr.clear()
    stdscr.addstr(0, 0, "hello")
    # stdscr.refresh()
    # stdscr.getkey()
    # exit(0)

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
    set_footer_message(stdscr, message="Japanese practice game! Type in the word you see, mirroring the output.")
    while not done and score < max_score:
        for challenge in game_list:
            stdscr.refresh()
            stdscr.addstr(0, 0, f"Score: {score}")

            thread = threading.Thread(target=thread_function, args=(challenge.value,))
            middle_x = int((curses.COLS - len(challenge.value) / 2))
            middle_y = int(curses.LINES / 2)
            stdscr.addstr(middle_y, middle_x, f"{challenge.value}")  # y, x
            # answer = stdscr.getstr(middle_y + 1, middle_x, len(challenge.value))

            editwin = curses.newwin(5, 30, 2, 1)
            rectangle(stdscr, 1, 0, 1 + 5 + 1, 1 + 30 + 1)
            stdscr.refresh()

            box = Textbox(editwin, insert_mode=True)

            # Let the user edit until Ctrl-G is struck.
            box.edit()

            # Get resulting contents
            answer = box.gather()

            if answer in ["q", "Q", "quit"]:
                done = True
            elif answer == challenge.value:
                score += 1
                stdscr.addstr(middle_y - 1, middle_x, "Correct")
            else:
                score -= 10
                string = f"Wrong! {challenge.value}, {challenge.meaning}"
                stdscr.addstr(middle_y - 1, middle_x, string)
            thread.start()
            if score >= max_score:
                string = f"Congrats! You have reached the target score."
                stdscr.addstr(middle_y - 1, middle_x, string)
                done = True
                break
        shuffle(game_list)

    end_curses()


if __name__ == "__main__":
    wrapper(main)
