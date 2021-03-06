from src.WordleAI import WordleAI
import random
import math
from itertools import product
import time


class WordleEntropyAI(WordleAI):
    def __init__(self, words_path: str, time_limit: float = 3, human_player: bool = False, human_checker: bool = False):
        super().__init__(words_path, human_player, human_checker)
        self.time_limit: float = time_limit

    def get_guess(self) -> str:
        entropy_map: {str, float} = self.get_entropy_map__(self.possible_words, self.words, self.time_limit)
        print("   Suggestions:")
        if len(self.possible_words) <= 2:
            print(self.possible_words)
        else:
            for i, (k, v) in enumerate(entropy_map.items()):
                if i == 3: break
                print("      %d. %s %.4f" % (i + 1, k, v))

        if self.human_player:
            return super().get_guess()
        else:
            if len(self.possible_words) <= 2: return self.possible_words[0]
            return next(iter(entropy_map))

    @classmethod
    def get_entropy__(cls, word: str, possible_words: [str]) -> float:
        entropy: float = 0.0
        for pattern in product(['A', 'B', 'X'], repeat=len(word)):
            new_words: [str] = cls.get_possible_words__(word, "".join(pattern), possible_words)
            px: float = len(new_words) / len(possible_words)
            entropy += -px * math.log(px, math.e) if px != 0 else 0
        return entropy / (len(word) + 1 - len(set(word)))

    @classmethod
    def get_entropy_map__(cls, possible_words: [str], words: [str], time_limit: float) -> {str, float}:
        random.shuffle(words)
        entropy_map: {str, float} = {}
        st: float = time.time()
        for i, word in enumerate(words):
            print("\r#calculating...... %.2fs/%.2fs (%d/%d)" % (time.time() - st, time_limit, i, len(words)), end="")
            entropy_map[word] = cls.get_entropy__(word, possible_words)
            if time_limit != 0 and time.time() - st > time_limit: break
        print("\r", end="")
        entropy_map = dict(sorted(entropy_map.items(), key=lambda x: x[1], reverse=True))
        return entropy_map


if __name__ == "__main__":
    game = WordleEntropyAI("../res/words.txt", 30)
    game.auto_play("./data/data_information_theory_30s.txt", 1000)
    game.show_barchart("./data/data_information_theory_30s.txt", 10, 16, 550)
