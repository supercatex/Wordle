from src.Wordle import Wordle
import random
import matplotlib.pyplot as plt


class WordleAI(Wordle):
    def __init__(self, words_path: str, human_player: bool = False, human_checker: bool = False):
        super().__init__(words_path)
        self.human_player: bool = human_player
        self.human_checker: bool = human_checker

    def get_guess(self) -> str:
        if self.human_player:
            return super().get_guess()
        else:
            return random.choice(self.possible_words)

    def get_pattern(self) -> str:
        if self.human_checker:
            pattern: str = input("Pattern:")
            while len(pattern) != len(self.answer) or not set(pattern).issubset({'A', 'B', 'X'}):
                print("Pattern only contain 'A', 'B', 'X' characters!")
                pattern = input("Pattern again:")
            return pattern
        else:
            return super().get_pattern()

    def auto_play(self, save_path: str, times: int):
        with open(save_path, "a+"): pass
        with open(save_path, "r") as f: t: int = len(f.readlines())
        while times == 0 or t < times:
            t = t + 1
            self.new_game()
            print("Game %d (%s):" % (t, self.answer))
            n_guess: int = self.play()
            with open(save_path, "a") as f: f.write("%d\n" % n_guess)

    @classmethod
    def show_barchart(cls, save_path: str, skip: int = 10, x_lim: int = 0, y_lim: int = 0):
        with open(save_path, "r") as f:
            data: [int] = [int(x.strip()) for x in f.readlines()]
        x: [int] = []
        y: [int] = []
        for i in range(max(data) + 2):
            x.append(i)
            y.append(0)

        sum_y: int = 0
        plt.ion()
        plt.cla()
        for i in range(len(data)):
            y[data[i]] += 1
            sum_y += data[i]
            if i % skip == 0 or i == len(data) - 1:
                plt.cla()
                plt.bar(x[1:], y[1:], color="b")
                plt.xlim(0, len(x) + 1 if x_lim == 0 else x_lim)
                plt.ylim(0, max(y) + 30 if y_lim == 0 else y_lim)
                for j in range(1, len(x)):
                    plt.text(x[j] - .3, y[j] + 20, str(y[j]), color="blue")
                plt.text(0, (max(y) if y_lim == 0 else y_lim) + 10,
                         "Sum: %d, Avg: %.4f, Win: %.2f%%" % (
                             sum(y), sum_y / (i + 1), sum(y[:7]) / sum(y) * 100
                ), color="blue")
                plt.pause(0.01)
        plt.ioff()
        plt.show()


if __name__ == "__main__":
    game = WordleAI("../res/words.txt")
    game.auto_play("./data/data_random_selection.txt", 1000)
    game.show_barchart("./data/data_random_selection.txt", 10, 16, 550)
