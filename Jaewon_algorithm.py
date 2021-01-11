import game_settings as setting
import os
import random


magic_num = setting.magic_num
max_counting = setting.max_counting
number_of_opponents = setting.number_of_players - 1
opponents_count_min = number_of_opponents * 1
opponents_count_max = number_of_opponents * max_counting


def load_data_sheet():
    data_sheet = "%s_data_sheet.txt" % "Jaewon_algorithm"
    if not os.path.isfile(data_sheet):
        with open(data_sheet, "w+") as f:
            for _ in range(magic_num):
                for _ in range(opponents_count_min, opponents_count_max + 1):
                    f.write("%d " % 0)
                f.write("\n")

    with open(data_sheet, "r") as f:
        for _ in range(magic_num):
            line = f.readline()
            split_int_list = list(map(lambda x: int(x), line.split()))
            counting_odds = counting_odds.append(split_int_list)
    return counting_odds


def calculating_odds(previous_num, counting):
    my_last_num = previous_num + counting
    posibilityof2 = 0.5

    winning_odds = (calculating_odds(my_last_num + 2, 1) + calculating_odds(my_last_num + 2, 2) + calculating_odds(my_last_num + 2, 3)) * posibilityof2

    if previous_num == magic_num - 1:
        winning_odds = 0

    return winning_odds


def adjust_data_sheet():
    pass


def random_max_index(a):
    max_value = max(a)
    max_index_list = [i for i, j in enumerate(a) if j == max_value]
    return random.choice(max_index_list)


def select_counting(previous_num):
    counting_odds = load_data_sheet()
    winning_odds_by_counting = []
    for counting in range(max_counting):
        winning_odds_by_counting.append(calculating_odds(previous_num, counting))
    counting = random_max_index(winning_odds_by_counting) + 1
    # adjust_data_sheet()
    return counting



