import random
import os
import game_settings
import Jaewon_algorithm
import Kyeongmin_algorithm
import Kyungho_algorithm
import random_algorithm
import User_input


class Player:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.previous_num = 0
        self.last_num = 0
        self.current_game_data = []
        self.victory = True

        self.total_rounds = 0
        self.total_wins = 0
        self.data_sheet = "%s_data_sheet.txt" % self.name
        self.load_data_sheet()
        player_list.append(self)

    def load_data_sheet(self):
        if not os.path.isfile(self.data_sheet):
            with open(self.data_sheet, "w+") as f:
                f.write("total rounds : 0\n")
                f.write("total wins : 0\n")

        with open(self.data_sheet, "r") as f:
            self.total_rounds = int(f.readline()[len("total rounds : "):])
            self.total_wins = int(f.readline()[len("total wins : "):])

    def select_counting(self):
        counting = self.strategy.select_counting(self.previous_num)
        if counting > max_counting:
            print("Invalid counting from %s" % self.name)

        self.last_num = self.previous_num + counting
        if self.last_num > magic_num:
            self.last_num = magic_num

    def print_nums(self):
        print("%10s :" % self.name, end='')
        print(list(range(self.previous_num + 1, self.last_num + 1)))

    def play_turn(self):
        self.select_counting()
        self.current_game_data.append(self.last_num)
        self.print_nums()

    def adjust_statics(self):
        self.total_rounds = self.total_rounds + 1
        self.total_wins = self.total_wins + self.victory

    def apply_to_data_sheet(self):
        with open(self.data_sheet, "w") as f:
            f.write("total rounds : %d\n" % self.total_rounds)
            f.write("total wins : %d\n" % self.total_wins)

    def __str__(self):
        return "{}, using {} strategy".format(self.name, self.strategy)


def check_game_table(i):
    if len(player_list) > number_of_players:
        print("There are too many players on the game table.")
    elif len(player_list) < number_of_players:
        print("We need more players.")
    else:
        print("< The %dth round >" % (i + 1))


if __name__ == "__main__":

    magic_num = game_settings.magic_num
    max_counting = game_settings.max_counting
    number_of_players = game_settings.number_of_players
    repetitions = game_settings.repetitions

    for game in range(repetitions):

        playing = True
        player_list = []
        P1 = Player("Jaewon", Jaewon_algorithm)
        P2 = Player("Kyeongmin", Kyeongmin_algorithm)
        P3 = Player("Kyeongho", Kyungho_algorithm)
        check_game_table(game)

        last_num = 0
        random.shuffle(player_list)
        while playing:
            for active_player in player_list:
                active_player.previous_num = last_num
                active_player.play_turn()
                last_num = active_player.last_num

                if last_num == magic_num:
                    active_player.victory = False
                    print("%10s lose!" % active_player.name)
                    playing = False
                    break

        for player in player_list:
            player.adjust_statics()
            player.apply_to_data_sheet()
            if 'adjust_data_sheet' in dir(player.strategy):
                player.strategy.adjust_data_sheet(player.current_game_data)
            print("%10s total records: Win : %d, Lose : %d"
                  % (player.name, player.total_wins, player.total_rounds - player.total_wins))
        print("=" * 100)
