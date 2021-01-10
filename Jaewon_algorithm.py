import game_settings as setting
import os


def load_data_sheet():
    data_sheet = "%s_data_sheet.txt" % "my_algorithm"
    if not os.path.isfile(data_sheet):
        with open(data_sheet, "w+") as f:
            f.write("total rounds : 0\n")
            f.write("total wins : 0\n")

    with open(data_sheet, "r") as f:
        total_rounds = int(f.readline()[len("total rounds : "):])
        total_wins = int(f.readline()[len("total wins : "):])


def calculating_odds(previous_num, counting):
    magic_num = setting.magic_num
    max_counting = setting.max_counting
    number_of_players = 3
    opponents_count_min = number_of_players * 1
    opponents_count_max = number_of_players * max_counting

    my_last_num = previous_num + counting
    posibilityof2 = 0.5

    winning_odds = (calculating_odds(my_last_num + 2, 1) + calculating_odds(my_last_num + 2, 2) + calculating_odds(my_last_num + 2, 3)) * posibilityof2

    if previous_num == magic_num - 1:
        winning_odds = 0

    return winning_odds


def select_counting(previous_num):
    counting = 3
    return counting



