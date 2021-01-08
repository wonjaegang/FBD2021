import random
import os


magic_num = 31
max_count = 3
default_odds = 0
player_list = []


def calculate_avg(avg0, n, a_n):
    return avg0*(n-1)/n + a_n/n


class Player:
    def __init__(self, name):
        self.name = name
        self.previous_num = 0
        self.last_num = 0
        self.last_nums = []

        self.victory = True
        self.odds_list = []
        self.total_rounds = 0
        self.total_wins = 0

        player_list.append(self)
        self.load_oddsdata()

    def load_oddsdata(self):
        data_sheet = "%s_oddsdata.txt" % self.name
        if not os.path.isfile(data_sheet):
            with open(data_sheet, "w+") as f:
                f.write("total rounds : 0\n")
                f.write("total wins : 0\n")
                for i in range(magic_num):
                    f.write("%03d odds : %f\n" % (i + 1, default_odds))

        with open(data_sheet, "r") as f:
            self.total_rounds = int(f.readline()[len("total rounds : "):])
            self.total_wins = int(f.readline()[len("total wins : "):])

            for line in f:
                self.odds_list.append(float(line[len(" odds : ") + 3:]))

    def pick_lastnum(self):
        index = self.previous_num
        odds_slice = self.odds_list[index: index + max_count]
        max_odds = max(odds_slice)
        finest_count = [i + 1 for i, j in enumerate(odds_slice) if j == max_odds]
        count_up = random.choice(finest_count)
        self.last_num = self.previous_num + count_up
        self.last_nums.append(self.last_num)

    def print_nums(self):
        print("%s :" % self.name, end='')
        print(list(range(self.previous_num + 1, self.last_num + 1)))

    def play_turn(self):
        self.pick_lastnum()
        self.print_nums()

    def adjust_statics(self):
        pass
