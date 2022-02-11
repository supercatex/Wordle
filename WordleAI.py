from Wordle import Wordle
import random
import matplotlib.pyplot as plt


class WordleAI(Wordle):
    def __init__(self, words_path: str):
        super().__init__(words_path)

    def get_guess(self) -> str:
        return random.choice(self.possible_words)

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
    def show_barchart(cls, save_path: str, skip: int = 10):
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
                plt.ylim(0, max(y) + 20)
                for j in range(1, len(x)):
                    plt.text(x[j] - .25, y[j] + 5, str(y[j]), color="blue")
                plt.text(0, max(y) + 20, "Sum: %d, Avg: %.4f, Less than 6: %.2f%%" % (
                    sum(y), sum_y / (i + 1), sum(y[:7]) / sum(y) * 100
                ), color="blue")
                plt.pause(0.01)
        plt.ioff()
        plt.show()


if __name__ == "__main__":
    game = WordleAI("./res/words.txt")
    game.auto_play("data_random.txt", 1000)
    game.show_barchart("data_random.txt")
