#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author            : Kinda Lam
# email             : LamKinUn@gmail.com
# date              : 2022-02-11
# license           : MIT
# py version        : 3.8.10

"""

Wordle: https://www.powerlanguage.co.uk/wordle/

Using Entropy Information Theory
https://en.wikipedia.org/wiki/Entropy_(information_theory)
https://hackmd.io/@sXG2cRDpRbONCsrtz8jfqg/ry-0k0PwH

    (E)xpected value, (P)robability, (I)nformation value, (b)ase
    I(E) = log(1/P(E), b)
         = -log(P(E), b)
    Entropy(X) = E[I(X)] = E[-log(P(X), b)]
               = -sum(P(xi) * log(P(xi), b)

"""

from src.Wordle import Wordle
from src.WordleAI import WordleAI
from src.WordleEntropyAI import WordleEntropyAI


if __name__ == "__main__":
    _words_path: str = "./res/words.txt"

    print("""There are 6 modes for you:
0. Normal play. 
1. Normal play with hints. 
2. Play and check by yourself. 
3. Show random selection barchart.
4. Show using Information Theory with 3s calculating time barchart.
5. Show using Information Theory with 30s calculating time barchart.""")
    _mode: int = int(input("Mode:"))

    if _mode == 0:      # Normal play.
        game: Wordle = Wordle(_words_path)
        game.new_game()
        game.play()
    elif _mode == 1:    # Normal play with hints.
        game: WordleEntropyAI = WordleEntropyAI(_words_path, 3, True, False)
        game.new_game()
        game.play()
    elif _mode == 2:    # Play and check by yourself.
        game: WordleEntropyAI = WordleEntropyAI(_words_path, 3, True, True)
        game.new_game()
        game.play()
    elif _mode == 3:    # Show random selection barchart.
        game: WordleAI = WordleAI(_words_path)
        game.auto_play("./data/data_random_selection.txt", 1000)
        WordleAI.show_barchart("./data/data_random_selection.txt", 10, 16, 550)
    elif _mode == 4:    # Show using Information Theory with 3s calculating time barchart.
        game: WordleEntropyAI = WordleEntropyAI(_words_path, 3)
        game.auto_play("./data/data_information_theory_3s.txt", 1000)
        WordleEntropyAI.show_barchart("./data/data_information_theory_3s.txt", 10, 16, 550)
    elif _mode == 5:    # Show using Information Theory with 30s calculating time barchart.
        game: WordleEntropyAI = WordleEntropyAI(_words_path, 30)
        game.auto_play("./data/data_information_theory_30s.txt", 1000)
        WordleEntropyAI.show_barchart("./data/data_information_theory_30s.txt", 10, 16, 550)
