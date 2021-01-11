import game_settings as setting
import os
import random
import itertools


magic_num = setting.magic_num
max_counting = setting.max_counting
number_of_opponents = setting.number_of_players - 1
opponents_counting_min = number_of_opponents * 1
opponents_counting_max = number_of_opponents * max_counting

opponents_counting_odds = []


def load_data_sheet():
    data_sheet = "%s_data_sheet.txt" % "Jaewon_algorithm"
    if not os.path.isfile(data_sheet):
        with open(data_sheet, "w+") as f:
            for _ in range(magic_num):
                for _ in range(opponents_counting_min, opponents_counting_max + 1):
                    f.write("%d " % 0)
                f.write("\n")

    with open(data_sheet, "r") as f:
        for _ in range(magic_num):
            line = f.readline()
            split_int_list = list(map(lambda x: int(x), line.split()))
            opponents_counting_odds.append(split_int_list)


def calculating_odds(previous_num, my_counting):
    my_last_num = previous_num + my_counting
    opponents_counting_list = list(range(opponents_counting_min, opponents_counting_max + 1))

    if previous_num >= magic_num:
        return 1

    elif my_last_num >= magic_num:
        return 0

    winning_odds = 0
    for opponents_counting in opponents_counting_list:
        next_previous_num = my_last_num + opponents_counting
        winning_odds = winning_odds + max(calculating_odds(next_previous_num, 1), calculating_odds(next_previous_num, 2), calculating_odds(next_previous_num, 3)) * opponents_counting_odds[next_previous_num - 1][opponents_counting]

    return winning_odds


def adjust_data_sheet():
    pass


def random_max_index(a):
    max_value = max(a)
    max_index_list = [i for i, j in enumerate(a) if j == max_value]
    return random.choice(max_index_list)


def select_counting(previous_num):
    load_data_sheet()
    win_rate_by_counting = []
    for counting in range(max_counting):
        win_rate_by_counting.append(calculating_odds(previous_num, counting))
    counting = random_max_index(win_rate_by_counting) + 1
    # adjust_data_sheet()
    return counting
