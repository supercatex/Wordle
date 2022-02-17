import random


class Wordle(object):
    def __init__(self, words_path: str):
        self.words: [str] = self.read_words__(words_path)
        self.possible_words: [str] = None
        self.n_guess: int = 0
        self.answer: str = ""
        self.guess: str = ""

    def new_game(self):
        self.possible_words = self.words.copy()
        self.n_guess = 0
        self.set_answer()
        self.guess = ""

    def set_answer(self, answer: str = ""):
        if '?' in answer or answer in self.words:
            self.answer = answer
        else:
            self.answer = random.choice(self.words)

    def get_guess(self) -> str:
        guess: str = input("Guess:")
        while guess != "quit" and guess not in self.words:
            print("Not in word list!")
            guess = input("Guess again:")
        if guess == "quit": exit(1)
        return guess

    def set_guess(self):
        self.guess = self.get_guess()

    def get_pattern(self) -> str:
        return self.get_pattern__(self.guess, self.answer)

    def filter_possible_words(self, pattern: str):
        self.possible_words = self.get_possible_words__(self.guess, pattern, self.possible_words)

    def play(self) -> int:
        while self.guess != self.answer:
            self.set_guess()
            self.n_guess += 1
            pattern: str = self.get_pattern()
            self.filter_possible_words(pattern)

            print("%d. %s | %s | %s" % (self.n_guess, self.guess, pattern, self.possible_words[:0]))
        return self.n_guess

    @classmethod
    def get_possible_words__(cls, guess: str, pattern: str, words: [str]) -> [str]:
        possible_words: [str] = []
        for word in words:
            if Wordle.get_pattern__(guess, word) == pattern:
                possible_words.append(word)
        return possible_words

    @classmethod
    def get_pattern__(cls, guess: str, answer: str) -> str:
        pattern: [str] = [''] * 5
        paired_pos = set()

        for i in range(len(answer)):
            if guess[i] == answer[i]:
                pattern[i] = 'A'
                paired_pos.add(i)

        for i in range(len(guess)):
            if pattern[i] == '':
                for j in range(len(answer)):
                    if guess[i] == answer[j] and j not in paired_pos:
                        pattern[i] = 'B'
                        paired_pos.add(j)
                        break
                else:
                    pattern[i] = 'X'

        return "".join(pattern)

    @classmethod
    def read_words__(cls, words_path: str) -> [str]:
        with open(words_path, "r") as f:
            words = [x.strip() for x in f.readlines()]
        return words


if __name__ == "__main__":
    game = Wordle("../res/words.txt")
    game.new_game()
    game.play()
